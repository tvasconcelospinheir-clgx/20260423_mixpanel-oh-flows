# Analytics Lab

This repository uses a self-contained project pattern: each request lives under `projects/YYYYMMDD_project-name/` with its own `data/`, `notebooks/`, and `outputs/` folders.

## Current Project

- `projects/analytics-lab/run.py`: entry point for this request.
- `projects/analytics-lab/data/raw/`: API pulls.
- `projects/analytics-lab/data/processed/`: cleaned/analysis-ready outputs.
- `projects/analytics-lab/notebooks/`: project notebooks.
- `projects/analytics-lab/outputs/`: final artifacts for sharing.

## Shared Code

- `src/connectors/mixpanel.py`: Mixpanel API client and request handling.
- `src/common/export.py`: shared JSON/CSV writers.
- `src/common/qa.py`: reusable quality checks.

## Setup

1. Create `.env` from `.env.example` and fill:
   - `MIXPANEL_PROJECT_ID`
   - `MIXPANEL_SERVICE_ACCOUNT_USERNAME`
   - `MIXPANEL_SERVICE_ACCOUNT_SECRET`
   - `MIXPANEL_VERIFY_SSL=true`
   - `MIXPANEL_CA_BUNDLE=` (optional org CA bundle path)
2. Create environment (Conda):
   - `conda env create -f environment.yml`
   - `conda activate analytics_base`

## Run

- `python projects/analytics-lab/run.py`

Or run the VS Code task `Run Mixpanel Pull`.

## Start Next Request

- `python scripts/run_request.py <project-name>`

Example:
- `python scripts/run_request.py pendo-onboarding`
