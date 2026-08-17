import json
from production import SERVICES

def check_service_health(service):
    print(f"\n[TOOL] Checking health for: {service}")

    service = service.lower()

    if service not in SERVICES:
        return {
            "error": f"Unknown service: {service}"
        }
    result = {
        "service": service,
        "health": SERVICES[service]["health"],
    }

    print("[TOOL RESULT]")
    print(json.dumps(result, indent=2))

    return result


if __name__ == "__main__":
    check_service_health("api")