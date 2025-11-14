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
            shared = ', '.join(guess_currencies & answer_currencies)
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
            shared = ', '.join(guess_languages & answer_languages)
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



def end_game(won: bool):
    """
    End the game in either a win or a loss, and pass this game's statistics
    on to be processed in statistics.py, and show a breakdown of this game's
    stats to the user
    """
    pass
