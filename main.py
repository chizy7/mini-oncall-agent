from agent import run_agent


def main():
    print("\n🚨 Mini On-Call Incident Agent")
    print("Type 'exit' to quit.\n")

    while True:
        incident = input(
            "Describe the incident: "
        ).strip()

        if not incident:
            continue

        if incident.lower() in {
            "exit",
            "quit",
        }:
            print("Goodbye.")
            break

        run_agent(incident)

        print()


if __name__ == "__main__":
    main()