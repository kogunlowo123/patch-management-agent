# Patch Management Agent Architecture

Patch management agent that identifies missing patches, prioritizes by risk and exploitability, schedules deployment windows, manages rollback procedures, and tracks patch compliance across the enterprise.

## Domain Tools

- **scan_missing_patches**: Scan systems for missing security and feature patches
- **prioritize_patches**: Prioritize patches by CVSS score, exploitability, and asset criticality
- **schedule_deployment**: Schedule patch deployment during approved maintenance window
- **execute_rollback**: Roll back a problematic patch deployment
- **track_compliance**: Track patch compliance percentage across the organization