# Mixpanel Analysis Starter

This project connects to Mixpanel using a service account and exports starter analytics outputs.

## Architecture (What this is building)

- `src/mixpanel_client.py`: API client that handles authentication, request timeouts, and JSON parsing.
- `src/main.py`: orchestration script that runs a first analysis pull and writes outputs to `data/`.
- `src/analysis_ideas.py`: starter list of analysis questions to guide what to build next.
- `data/`: generated JSON/CSV outputs (kept out of source control).
- `.env`: local secrets/config only.

Design choices:
- Credentials are read from environment variables, never hardcoded.
- Scripts live in `src/`, outputs in `data/`.
- Intermediate outputs are persisted as both JSON and CSV when possible.
- API calls use explicit timeouts and raise errors on non-2xx responses.

## 1) Setup

1. Create a `.env` file from `.env.example`.
2. Fill in:
   - `MIXPANEL_PROJECT_ID`
   - `MIXPANEL_SERVICE_ACCOUNT_USERNAME`
   - `MIXPANEL_SERVICE_ACCOUNT_SECRET`
   - `MIXPANEL_VERIFY_SSL=true`
   - `MIXPANEL_CA_BUNDLE=` (optional path to corporate CA cert bundle)
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 2) Run

```bash
python src/main.py
```

Or run the VS Code task: `Run Mixpanel Pull`.

## SSL troubleshooting (corporate networks)

If you see SSL certificate verification errors:
- Preferred: set `MIXPANEL_CA_BUNDLE` to your org CA bundle path.
- Temporary fallback: set `MIXPANEL_VERIFY_SSL=false` to bypass verification.

Use the fallback only for debugging and switch back to secure verification after fixing CA trust.

## 3) Outputs

- `data/top_events_7d.json`
- `data/top_events_7d.csv` (if data returned)
- `data/analysis_ideas.json`

## 4) Next analyses to build

- Conversion funnel by segment (country/device/channel)
- Retention cohorts by acquisition source
- Time-to-value distribution for newly signed-up users
- Leading indicators of churn
