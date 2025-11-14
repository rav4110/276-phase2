import json
from datetime import datetime

from nicegui import Event, ui

from game.daily import handle_guess

# NiceGUI elements go here

# display the game (guess input, guess feedback, timer, # of guesses, etc.)
"""
game

    - guess entry box
    - guess button
    - guess feedback

    - win/loss popup
"""

# TODO: Replace with data type containing actual guess feedback
guess_graded = Event[str]()
game_ended = Event[bool]()


def try_guess(guess_input, feedback):
    if guess_input.validate():
        handle_guess(guess_input.value)
        guess_input.clear()


@game_ended.subscribe
def display_results(won: bool):
    # TODO: Add pop-up that will display whether you won or lost,
    # your # of guesses and time, and (in future) the leaderboard info
    pass


def content():
    options = []
    with open("src/game/countries.json") as file:
        options = json.load(file)

    with ui.column(align_items="center").classes("mx-auto w-full max-w-md p-4"):
        timer = ui.label()
        # TODO: Replace with actual game timer, not just current time
        ui.timer(1.0, lambda: timer.set_text(f"{datetime.now():%X}"))

        columns = [
            {"name": "name", "label": "Name"},
            {"name": "population", "label": "Population"},
            {"name": "size", "label": "Size"},
            {"name": "region", "label": "Region"},
            {"name": "languages", "label": "Languages"},
            {"name": "currencies", "label": "Currencies"},
            {"name": "timezones", "label": "Timezones"},
        ]
        rows = []
        feedback = ui.table(rows=rows, columns=columns, row_key="name")

        with ui.card(align_items="center"):
            guess_input = ui.input(
                label="Guess",
                placeholder="Enter a country",
                autocomplete=options,
                validation={"Not a valid country!": lambda value: value.lower() in options},
            ).without_auto_validation()
            ui.button("Submit", on_click=lambda: try_guess(guess_input, feedback))


# button to display leaderboards
"""
leaderboard

    - by default, display ~250 entries around the user
    - allow switch to friends-only or global leaderboard
    - allow jumping to top-ranked players
"""

# button to open account management menu
"""
account management

    - create account
    - see account stats
    - edit account info (username/password/email)
    - friends/friend requests
"""
