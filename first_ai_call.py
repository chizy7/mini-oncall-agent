from dotenv import load_dotenv
from openai import OpenAI

from tools import TOOL_SCHEMAS

load_dotenv()

client = OpenAI()


response = client.responses.create(
    model="gpt-5.6-luna", 

    instructions=(
        "You are an on-call production engineer. "
        "Investigate production incidents using the available tools."
    ),

    input="Users report that the API is very slow.",

    tools=TOOL_SCHEMAS,

    parallel_tool_calls=False,
)

print("\nMODEL OUTPUT")
print("===========")


for item in response.output:
    if item.type == "function_call":
        print(f"Tool requested: {item.name}")
        print(f"Arguments: {item.arguments}")