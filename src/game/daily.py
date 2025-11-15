import random
from datetime import date, datetime, timedelta, timezone

from nicegui import Event

from phase2.country import Country, get_country, get_random_country

MAX_GUESSES = 5


class RoundStats:
    guesses: int = 0
    max_guesses: int
    round_start: datetime
    guess_graded: Event[str]
    game_ended: Event[bool]
    round_time: timedelta

    def __init__(self):
        self.guesses = 0
        self.max_guesses = MAX_GUESSES
        self.round_start = datetime.now(timezone.utc)

        # TODO: Replace with data type containing actual guess feedback
        self.guess_graded = Event[str]()
        self.game_ended = Event[bool]()
        self.round_time = timedelta()

    def end_round(self):
        self.round_time = datetime.now(timezone.utc) - self.round_start


def get_daily_country() -> Country:
    """
    Gets a country for today's date, deterministically
    """
    today_str = date.today().isoformat()
    random.seed(today_str)  # seed random with date (every daily country is the same)
    return get_random_country()


def handle_guess(input: str, round_stats: RoundStats):
    """
    Assumes input str is a valid country string

    Processes the given input. Ends the game if either end condition is reached
    (reached max guesses or guessed correctly)
    """
    round_stats.guesses += 1
    country = get_country(input)
    daily_country = get_daily_country()

    if compare_countries(country, daily_country):
        end_game(True, round_stats)
        round_stats.end_round()
    elif round_stats.guesses >= MAX_GUESSES:
        end_game(False, round_stats)
        round_stats.end_round()

    # TODO: Pass the comparison result from compare_countries to this call
    round_stats.guess_graded.emit(input)


def compare_countries(guess: Country, answer: Country) -> bool:
    """
    Check if the two countries match.
    If they match, return True.
    If not, compare the following statistics and print feedback:
    - Population
    - Geographical Size
    - Currencies
    - Languages
    - Timezones
    - Region

    Returns True if correct, False otherwise.
    """
    # TODO: Create a data structure to be returned by this function
    # containing guess feedback info

    # Check if countries match (correct guess)
    if guess.name.lower() == answer.name.lower():
        print(f"\nCorrect! The answer is {answer.name}!")
        return True

    # Wrong guess - provide comparison feedback
    print(f"\n{guess.name} is not correct. Here are your hints:\n")

    # Compare population
    if guess.population and answer.population:
        ratio = guess.population / answer.population
        if ratio < 0.5:
            print("Population: The correct answer has MORE THAN DOUBLE the population")
        elif ratio < 0.9:
            print("Population: The correct answer has a HIGHER population")
        elif ratio <= 1.1:
            print("Population: Very close in population!")
        elif ratio <= 2:
            print("Population: The correct answer has a LOWER population")
        else:
            print("Population: The correct answer has LESS THAN HALF the population")

    # Compare size (area)
    if guess.size and answer.size:
        ratio = guess.size / answer.size
        if ratio < 0.5:
            print("Size: The correct answer is MORE THAN DOUBLE the area")
        elif ratio < 0.9:
            print("Size: The correct answer is LARGER in area")
        elif ratio <= 1.1:
            print("Size: Very close in area!")
        elif ratio <= 2:
            print("Size: The correct answer is SMALLER in area")
        else:
            print("Size: The correct answer is LESS THAN HALF the area")

    # Compare region
    if guess.region == answer.region:
        print(f"Region: Correct! Same region ({answer.region})")
    else:
        print(f"Region: Different region (correct answer is in {answer.region})")

    # Compare currencies
    guess_currencies = set(guess.currencies) if guess.currencies else set()
    answer_currencies = set(answer.currencies) if answer.currencies else set()

    if answer_currencies:
        if guess_currencies == answer_currencies:
            print("Currencies: Exact match on all currencies!")
        elif guess_currencies & answer_currencies:  # Has intersection
            shared = ", ".join(guess_currencies & answer_currencies)
            print(f"Currencies: Partial match! Shared: {shared}")
        else:
            print("Currencies: No matching currencies")

    # Compare languages
    guess_languages = set(guess.languages) if guess.languages else set()
    answer_languages = set(answer.languages) if answer.languages else set()

    if answer_languages:
        if guess_languages == answer_languages:
            print("Languages: Exact match on all languages!")
        elif guess_languages & answer_languages:  # Has intersection
            shared = ", ".join(guess_languages & answer_languages)
            print(f"Languages: Partial match! Shared: {shared}")
        else:
            print("Languages: No matching languages")

    # Compare timezones
    guess_timezones = set(guess.timezones) if guess.timezones else set()
    answer_timezones = set(answer.timezones) if answer.timezones else set()

    if answer_timezones:
        if guess_timezones == answer_timezones:
            print("Timezones: Exact match on all timezones!")
        elif guess_timezones & answer_timezones:  # Has intersection
            print("Timezones: Some timezones overlap")
        else:
            print("Timezones: No matching timezones")

    print()  # Empty line for readability
    return False


def end_game(won: bool, round_stats: RoundStats):
    """
    End the game in either a win or a loss, and pass this game's statistics
    on to be processed in statistics.py, and show a breakdown of this game's
    stats to the user
    """
    pass
