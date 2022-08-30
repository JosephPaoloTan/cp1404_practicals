CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represents a guitar object"""

    def __init__(self, name='', year=0, cost=0):
        """Initialise a guitar instance
        name: string, name of guitar
        year: int, year created
        cost: float, price of guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string of guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculate age"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Check if vintage"""
        return self.get_age() >= VINTAGE_AGE
