"""Patch Management Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class PatchInfo(BaseModel):
    """PatchInfo for Patch Management Agent."""
    patch_id: str
    title: str
    severity: str
    cvss_score: float
    affected_systems: int
    exploit_available: bool


class PatchCompliance(BaseModel):
    """PatchCompliance for Patch Management Agent."""
    total_systems: int
    patched: int
    compliance_pct: float
    overdue: int
    by_severity: dict

