"""Test configuration for Patch Management Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "patch-management-agent", "category": "IT Operations"}
