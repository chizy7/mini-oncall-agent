import json

from production import SERVICES


def check_service_health(service):
    print(f"\n[TOOL] Checking health for: {service}")

    service = service.lower()

    if service not in SERVICES:
        result = {
            "error": f"Unknown service: {service}"
        }

        print("[TOOL RESULT]")
        print(json.dumps(result, indent=2))

        return result

    result = {
        "service": service,
        "health": SERVICES[service]["health"],
    }

    print("[TOOL RESULT]")
    print(json.dumps(result, indent=2))

    return result


def get_service_metrics(service):
    print(f"\n[TOOL] Checking metrics for: {service}")

    service = service.lower()

    if service not in SERVICES:
        result = {
            "error": f"Unknown service: {service}"
        }

        print("[TOOL RESULT]")
        print(json.dumps(result, indent=2))

        return result

    result = {
        "service": service,
        "metrics": SERVICES[service]["metrics"],
    }

    print("[TOOL RESULT]")
    print(json.dumps(result, indent=2))

    return result


def get_service_logs(service):
    print(f"\n[TOOL] Getting logs for: {service}")

    service = service.lower()

    if service not in SERVICES:
        result = {
            "error": f"Unknown service: {service}"
        }

        print("[TOOL RESULT]")
        print(json.dumps(result, indent=2))

        return result

    result = {
        "service": service,
        "logs": SERVICES[service]["logs"],
    }

    print("[TOOL RESULT]")
    print(json.dumps(result, indent=2))

    return result


def get_service_dependencies(service):
    print(f"\n[TOOL] Getting dependencies for: {service}")

    service = service.lower()

    if service not in SERVICES:
        result = {
            "error": f"Unknown service: {service}"
        }

        print("[TOOL RESULT]")
        print(json.dumps(result, indent=2))

        return result

    result = {
        "service": service,
        "dependencies": SERVICES[service]["dependencies"],
    }

    print("[TOOL RESULT]")
    print(json.dumps(result, indent=2))

    return result


# Before we add AI let's add a tool router
TOOL_FUNCTIONS = {
    "check_service_health": check_service_health,
    "get_service_metrics": get_service_metrics,
    "get_service_logs": get_service_logs,
    "get_service_dependencies": get_service_dependencies,
}

def call_tool(tool_name, arguments):
    print(f"\n[ROUTER] Executing: {tool_name}")

    function = TOOL_FUNCTIONS.get(tool_name)

    if function is None:
        return {
            "error": f"Unknown tool: {tool_name}"
        }
    return function(**arguments)


# TOOL SCHEMAS
TOOL_SCHEMAS = [
    {
        "type": "function",
        "name": "check_service_health",
        "description": (
            "Check whether a production service is "
            "healthy or degraded."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "enum": [
                        "frontend",
                        "api",
                        "database",
                    ],
                }
            },
            "required": ["service"],
            "additionalProperties": False,
        },
        "strict": True,
    },

    {
        "type": "function",
        "name": "get_service_metrics",
        "description": (
            "Get current production metrics for a service, "
            "including CPU, memory, latency, errors, "
            "and connection usage when available."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "enum": [
                        "frontend",
                        "api",
                        "database",
                    ],
                }
            },
            "required": ["service"],
            "additionalProperties": False,
        },
        "strict": True,
    },

    {
        "type": "function",
        "name": "get_service_logs",
        "description": (
            "Get recent application logs for a production "
            "service. Useful for finding errors, warnings, "
            "and timeouts."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "enum": [
                        "frontend",
                        "api",
                        "database",
                    ],
                }
            },
            "required": ["service"],
            "additionalProperties": False,
        },
        "strict": True,
    },

    {
        "type": "function",
        "name": "get_service_dependencies",
        "description": (
            "Get the downstream production services that "
            "a service depends on."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "enum": [
                        "frontend",
                        "api",
                        "database",
                    ],
                }
            },
            "required": ["service"],
            "additionalProperties": False,
        },
        "strict": True,
    },
]

if __name__ == "__main__":
    # check_service_health("api")
    # get_service_metrics("api")
    # get_service_logs("api")
    # get_service_dependencies("api")
    call_tool (
        "get_service_metrics",
        {"service": "database"},
    )