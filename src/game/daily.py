import datetime
import random

from phase2.country import Country, get_country, get_random_country

MAX_GUESSES = 5
guesses = 0
# TODO: change from global variable guesses

def get_daily_country() -> Country:
    """
    Gets a country for today's date, deterministically
    """
    today_str = datetime.date.today().isoformat()
    random.seed(today_str) # seed random with date (every daily country is the same)
    return get_random_country()


def handle_guess(input: str) -> bool:
    """
    Assumes input str is a valid country string

    Processes the given input, returning True if the guess was valid
    or False otherwise. Ends the game if either end condition is reached
    (reached max guesses or guessed correctly)
    """
    global guesses
    guesses += 1
    country = get_country(input)
    daily_country = get_daily_country()
    if compare_countries(country, daily_country):
        end_game(True)
        return True
    elif guesses >= MAX_GUESSES:
        end_game(False)
        return False
    else: # continue game
        return False


def compare_countries(guess: Country, answer: Country):
    """
    Check if the two countries, match.
    If not, compare the following statistics for two countries:
    - Population
    - Geographical Size
    - Currencies
    - Languages
    - Timezones
    - Region
    """
    pass


def end_game(won: bool):
    """
    End the game in either a win or a loss, and pass this game's statistics
    on to be processed in statistics.py, and show a breakdown of this game's
    stats to the user
    """
    pass
