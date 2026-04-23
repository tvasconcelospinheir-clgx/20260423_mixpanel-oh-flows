import json
from pathlib import Path

import pandas as pd

from analysis_ideas import starter_analysis_ideas
from mixpanel_client import MixpanelClient


OUTPUT_DIR = Path("data")


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def main() -> None:
    client = MixpanelClient()

    print("Fetching top events for last 7 days...")
    top_events = client.event_counts_last_n_days(n_days=7, limit=25)
    write_json(OUTPUT_DIR / "top_events_7d.json", top_events)

    if top_events:
        df = pd.DataFrame(top_events)
        df.to_csv(OUTPUT_DIR / "top_events_7d.csv", index=False)

    print("Writing starter analysis ideas...")
    ideas = starter_analysis_ideas()
    write_json(OUTPUT_DIR / "analysis_ideas.json", ideas)

    print("Done. Generated files:")
    print("- data/top_events_7d.json")
    print("- data/top_events_7d.csv (if events returned)")
    print("- data/analysis_ideas.json")


if __name__ == "__main__":
    main()
