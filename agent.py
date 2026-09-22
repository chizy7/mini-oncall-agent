import json

from dotenv import load_dotenv
from openai import OpenAI

from tools import TOOL_SCHEMAS, call_tool


load_dotenv()

client = OpenAI()

MODEL = "gpt-5.6-luna"


SYSTEM_PROMPT = """
You are Mini On-Call, a production incident investigation agent.

Your job is to investigate production incidents using the
available tools and identify the most likely root cause.

Rules:

1. Gather evidence before diagnosing a problem.
2. Start with the service mentioned by the user when possible.
3. Use health, metrics, logs, and dependencies as needed.
4. Follow evidence into downstream services when appropriate.
5. Do not invent production data.
6. Do not claim that you restarted or changed anything.
7. Stop once you have enough evidence for a reasonable diagnosis.
8. If there is not enough evidence, say so.

Your final response should contain:

Incident Summary
Evidence
Likely Root Cause
Recommended Next Action
"""


def run_agent(user_message):
    print("\n====================================")
    print("🚨 MINI ON-CALL INCIDENT AGENT")
    print("====================================")

    print(f"\nIncident: {user_message}")

    input_items = [
        {
            "role": "user",
            "content": user_message,
        }
    ]

    max_steps = 8

    for step in range(1, max_steps + 1):
        print(f"\n---------- STEP {step} ----------")

        response = client.responses.create(
            model=MODEL,
            instructions=SYSTEM_PROMPT,
            input=input_items,
            tools=TOOL_SCHEMAS,
            parallel_tool_calls=False,
        )

        input_items += response.output

        function_calls = [
            item
            for item in response.output
            if item.type == "function_call"
        ]

        print(
            f"[AGENT] Tool calls requested: "
            f"{len(function_calls)}"
        )

        if not function_calls:
            print("\n========== FINAL DIAGNOSIS ==========")
            print(response.output_text)
            print("=====================================")

            return response.output_text

        for function_call in function_calls:
            arguments = json.loads(
                function_call.arguments
            )

            print(
                f"[AGENT] Selected tool: "
                f"{function_call.name}"
            )

            print(
                f"[AGENT] Arguments: "
                f"{arguments}"
            )

            result = call_tool(
                function_call.name,
                arguments,
            )

            input_items.append(
                {
                    "type": "function_call_output",
                    "call_id": function_call.call_id,
                    "output": json.dumps(result),
                }
            )

    print("\n[SAFETY STOP]")
    print(
        "Agent reached the maximum number "
        "of investigation steps."
    )

    return None


if __name__ == "__main__":
    run_agent(
        "Users report that the API is very slow."
    )