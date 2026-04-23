from typing import List


def starter_analysis_ideas() -> List[str]:
    return [
        "Activation: % of new users completing key event within 24h.",
        "Onboarding funnel: signup -> first key action -> repeat action (7d).",
        "Retention cohorts: D1, D7, D30 by acquisition source.",
        "Power-user path: event sequences most common among top 10% active users.",
        "Feature adoption depth: median weekly uses per feature among active users.",
        "Conversion predictors: first-session events correlated with paid conversion.",
        "Time-to-value: median hours from signup to first success event.",
        "Churn signals: behavior change in last 14 days before inactivity.",
        "Segment comparison: mobile vs web, geo, or plan tier performance.",
        "Data quality audit: null/missing props, duplicate events, inconsistent naming.",
    ]
