SERVICES = {
    "frontend": {
        "health": "healthy",

        "metrics": {
            "cpu_percent": 21,
            "memory_percent": 43,
            "latency_ms": 95,
            "error_rate_percent": 0.1,

        "logs": [
            "INFO GET / 200 91ms",
            "INFO GET /dashboard 200 102ms",
            "INFO frontend health check passed",
        ],
        "dependencies": ["api"],
        },
    },
    "api": {
        "health": "degraded",

        "metrics": {
            "cpu_percent": 34,
            "memory_percent": 58,
            "latency_ms": 4200,
            "error_rate_percent": 11.8,

        "logs": [
            "ERROR request_id=a91 /checkout database timeout while acquiring connection",
            "ERROR request_id=b07 /orders database timeout while acquiring connection",
            "WARN upstream database response exceeded 3000ms",
            "INFO request_id=c22 /health 200 12ms",
        ],
        "dependencies": ["datavase"],
        },
    },
    "database": {
        "health": "degraded",

        "metrics": {
            "cpu_percent": 46,
            "memory_percent": 71,
            "latency_ms": 1200,
            "error_rate_percent": 6.4,
            "active_connections": 99,
            "max_connections": 100,

        "logs": [
            "WARN connection pool usage 99/100",
            "ERROR too many connections",
            "WARN query waiting for available connection",
            "INFO checkpoint complete",
        ],
        "dependencies": [],
        },
    },
}


if __name__ == "__main__":
    print("Prodcution Services")
    print("===================")

    for service, data in SERVICES.items():
        print(
            f"{service}: "
            f"health={data['health']}, "
            f"latency={data['metrics']['latency_ms']}ms")