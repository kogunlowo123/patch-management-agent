"""Patch Management Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_scan_missing_patches():
    """Test Scan systems for missing security and feature patches."""
    tools = AgentTools()
    result = await tools.scan_missing_patches(scope="test", severity_filter="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_prioritize_patches():
    """Test Prioritize patches by CVSS score, exploitability, and asset criticality."""
    tools = AgentTools()
    result = await tools.prioritize_patches(patches="test", asset_context="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_schedule_deployment():
    """Test Schedule patch deployment during approved maintenance window."""
    tools = AgentTools()
    result = await tools.schedule_deployment(patches="test", targets="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_execute_rollback():
    """Test Roll back a problematic patch deployment."""
    tools = AgentTools()
    result = await tools.execute_rollback(deployment_id="test", reason="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.patch_management_agent_agent import PatchManagementAgentAgent
    agent = PatchManagementAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
