# Contributing to IPIVC Standard

Thank you for your interest in improving the **IPIVC Standard**.
This project is an open-source initiative to bring order to AI-assisted software development.

## How to Contribute

### 1. Improvements to the Protocol
If you have an idea to improve the workflow (e.g., a better way to handle locking):
1.  Open an Issue describing the problem.
2.  Propose a change to `TEAM_WORKFLOW.md` or `README.md`.

### 2. Tooling Enhancements
The scripts in `tools/` are written in Python for portability.
- **Bug Fixes**: Submit a PR directly.
- **New Tools**: Please discuss in an Issue first. We want to keep the core lightweight.

### 3. Server Logic (LokiVector)
Changes to `server/index.js` must be compatible with the existing API used by `session_manager.py`.

## Code of Conduct
- Be respectful.
- This standard assumes a "Human-Centric" approach. Proposals to remove human oversight will likely be rejected.

## License
MIT
