#!/bin/bash
set -euo pipefail
echo "Setting up Patch Management Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
