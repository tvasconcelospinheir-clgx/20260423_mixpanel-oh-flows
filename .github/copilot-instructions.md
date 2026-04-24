# Copilot Instructions for Mixpanel Analysis Starter

- Use environment variables for all credentials; do not hardcode secrets.
- Keep scripts in `src/` and outputs in `data/`.
- Prefer incremental analyses and persist intermediate outputs as JSON or CSV.
- When adding new analysis scripts, include a short section in `README.md` with run instructions.
- If adding API calls, include basic error handling and request timeouts.

## Session Bootstrap

- At the start of each new chat in this repository, read `references/README.md` first.
- If the task is Mixpanel implementation quality, identity, or instrumentation, also read `references/onehome-mixpanel-implementation-audit.md` before proposing changes.
- Treat `references/` as project memory for architecture decisions, prior audits, and analytics conventions.
