import datetime
from game import daily
from phase2.country import Country, get_country, get_random_country

class TempCountry(Country):
        def __init__(self, name):
            self.name = name
            self.population = 0
            self.size = 0.0
            self.region = ""
            self.languages = []
            self.currencies = []
            self.timezones = []


# temp methods for compare_countries and end_game
def temp_compare_countries(guess, answer):
    return guess.name == answer.name

def temp_end_game(won):
    global end_game_called
    end_game_called = won

daily.compare_countries = temp_compare_countries
daily.end_game = temp_end_game

def test_get_daily_country_same_country_for_same_day(): 
    first_call = daily.get_daily_country()
    second_call = daily.get_daily_country()

    assert isinstance(first_call, Country)
    assert first_call.name == second_call.name


def test_handle_guess_correct():
    global end_game_called
    end_game_called = None
    daily.guesses = 0

    daily_country = TempCountry("Canada")
    user_guess = TempCountry("Canada")

    daily.get_daily_country = lambda: daily_country

    result = daily.handle_guess(user_guess.name)
    assert result is True
    assert daily.guesses == 1
    assert end_game_called is True  # game ended


def test_handle_guess_incorrect():
    global end_game_called
    end_game_called = None
    daily.guesses = 0

    daily_country = TempCountry("Canada")
    user_guess = TempCountry("United States")

    daily.get_daily_country = lambda: daily_country

    result = daily.handle_guess(user_guess.name)
    assert result is False
    assert daily.guesses == 1
    assert end_game_called is None  # game not ended


def test_handle_guess_max_guesses():
    global end_game_called
    end_game_called = None
    daily.guesses = daily.MAX_GUESSES - 1

    daily_country = TempCountry("Canada")
    user_guess = TempCountry("United States")

    daily.get_daily_country = lambda: daily_country

    result = daily.handle_guess(user_guess.name)
    assert result is False
    assert daily.guesses == daily.MAX_GUESSES
    assert end_game_called is False

