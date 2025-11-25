# src/game/leaderboard_ui.py

from typing import List, Dict, Any

from nicegui import ui


def fetch_leaderboard() -> List[Dict[str, Any]]:
    """Return fake leaderboard data for UI testing."""
    rows: List[Dict[str, Any]] = [
        {
            "entry_id": 1,
            "user_id": "Bob",
            "daily_streak": 3,
            "longest_daily_streak": 7,
            "average_daily_guesses": 4,
            "average_daily_time": "35.2s",
            "longest_survival_streak": 9,
            "high_score": 1234,
        },
        {
            "entry_id": 2,
            "user_id": "Charlie",
            "daily_streak": 1,
            "longest_daily_streak": 5,
            "average_daily_guesses": 3,
            "average_daily_time": "28.0s",
            "longest_survival_streak": 12,
            "high_score": 1450,
        },
        {
            "entry_id": 3,
            "user_id": "Amy",
            "daily_streak": 10,
            "longest_daily_streak": 12,
            "average_daily_guesses": 2,
            "average_daily_time": "19.7s",
            "longest_survival_streak": 20,
            "high_score": 2005,
        },
        {
            "entry_id": 4,
            "user_id": "Dave",
            "daily_streak": 0,
            "longest_daily_streak": 1,
            "average_daily_guesses": 5,
            "average_daily_time": "42.0s",
            "longest_survival_streak": 4,
            "high_score": 980,
        },
    ]

    # sort by score high → low and add rank
    rows.sort(key=lambda e: e["daily_streak"], reverse=True)
    for i, e in enumerate(rows, start=1):
        e["rank"] = i

    return rows


def leaderboard_page() -> None:
    """Build the leaderboard UI with NiceGUI."""

    ui.label("Leaderboard").classes("text-3xl font-bold mb-4")

    columns = [
        {"name": "rank", "label": "Rank", "field": "rank", "sortable": True},
        {"name": "user_id", "label": "User", "field": "user_id", "sortable": True},
        {
            "name": "daily_streak",
            "label": "Daily Streak",
            "field": "daily_streak",
            "sortable": True,
        },
        {
            "name": "longest_daily_streak",
            "label": "Longest Daily Streak",
            "field": "longest_daily_streak",
            "sortable": True,
        },
        {
            "name": "average_daily_guesses",
            "label": "Avg Guesses",
            "field": "average_daily_guesses",
            "sortable": True,
        },
        {
            "name": "average_daily_time",
            "label": "Avg Time",
            "field": "average_daily_time",
            "sortable": True,
        },
        {
            "name": "longest_survival_streak",
            "label": "Survival Streak",
            "field": "longest_survival_streak",
            "sortable": True,
        },
        {
            "name": "high_score",
            "label": "High Score",
            "field": "high_score",
            "sortable": True,
        },
    ]

    # fill table immediately with fake data
    table = ui.table(
        columns=columns,
        rows=fetch_leaderboard(),
        row_key="entry_id",
    ).classes("w-full")

    # optional: refresh button just reloads fake data
    def load_data():
        table.rows = fetch_leaderboard()

    ui.button("Refresh", on_click=load_data).classes("mt-4")


if __name__ in {"__main__", "__mp_main__"}:
    leaderboard_page()
    ui.run()
