class Country:
    name: str
    population: int
    size: float
    region: str
    languages: [str]
    currencies: [str]
    timezones: [str]


def get_random_country() -> Country:
    """
    Returns a random country object from the country API
    """
    pass


def get_country(name: str) -> Country:
    """
    Returns the country that matches the given name string, or None
    if no such country exists.
    """
    pass
