import sys
from pathlib import Path

# Allow running directly (python run.py) without editable install.
# With `pip install -e .` from repo root this sys.path insert is a no-op.
_repo_root = Path(__file__).resolve().parents[2]
if str(_repo_root) not in sys.path:
    sys.path.insert(0, str(_repo_root))

_project_dir = Path(__file__).resolve().parent
if str(_project_dir) not in sys.path:
    sys.path.insert(0, str(_project_dir))

from analysis_ideas import starter_analysis_ideas
from src.common.export import write_csv, write_json
from src.connectors.mixpanel import MixpanelClient

_PROJECT_DIR = Path(__file__).parent
OUTPUT_RAW = _PROJECT_DIR / "data" / "raw"
OUTPUT_PROCESSED = _PROJECT_DIR / "data" / "processed"


def main() -> None:
    client = MixpanelClient()

    print("Fetching top events for last 7 days...")
    top_events = client.event_counts_last_n_days(n_days=7, limit=25)
    write_json(OUTPUT_RAW / "top_events_7d.json", top_events)
    write_csv(OUTPUT_PROCESSED / "top_events_7d.csv", top_events)

    print("Writing starter analysis ideas...")
    ideas = starter_analysis_ideas()
    write_json(OUTPUT_PROCESSED / "analysis_ideas.json", ideas)

    print("Done. Generated files:")
    print(f"  {OUTPUT_RAW}/top_events_7d.json")
    print(f"  {OUTPUT_PROCESSED}/top_events_7d.csv")
    print(f"  {OUTPUT_PROCESSED}/analysis_ideas.json")


if __name__ == "__main__":
    main()
