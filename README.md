# Mini On-Call Incident Agent

A minimal Python AI agent that investigates production incidents using health checks, metrics, logs, and service dependencies.

This project is designed as a small educational example for learning how AI agents work while also introducing Production Engineering concepts such as observability, dependency tracing, incident investigation, and root-cause analysis.

## What It Does

A user reports a production issue such as:

```text
Users report that the API is very slow.
```
The agent then investigates the system by deciding which tools to use.