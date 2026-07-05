# Patch Management Agent

[![CI](https://github.com/kogunlowo123/patch-management-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/patch-management-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: IT Operations | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Patch management agent that identifies missing patches, prioritizes by risk and exploitability, schedules deployment windows, manages rollback procedures, and tracks patch compliance across the enterprise.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `scan_missing_patches` | Scan systems for missing security and feature patches |
| `prioritize_patches` | Prioritize patches by CVSS score, exploitability, and asset criticality |
| `schedule_deployment` | Schedule patch deployment during approved maintenance window |
| `execute_rollback` | Roll back a problematic patch deployment |
| `track_compliance` | Track patch compliance percentage across the organization |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/patches/scan` | Scan missing patches |
| `POST` | `/api/v1/patches/prioritize` | Prioritize patches |
| `POST` | `/api/v1/patches/deploy` | Schedule deployment |
| `POST` | `/api/v1/patches/rollback` | Execute rollback |
| `GET` | `/api/v1/patches/compliance` | Track compliance |

## Features

- Patch Identification
- Risk Prioritization
- Deployment Scheduling
- Rollback Management
- Compliance Tracking

## Integrations

- Wsus
- Sccm
- Qualys
- Ivanti
- Automox

## Architecture

```
patch-management-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── patch_management_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**WSUS + SCCM + Qualys + Patch Management Platform**

---

Built as part of the Enterprise AI Agent Platform.
