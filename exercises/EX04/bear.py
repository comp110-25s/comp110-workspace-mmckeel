"""File to define Bear class."""


class Bear:
    """Defines the Bear class for the simulation."""

    def __init__(self):
        """Base values of the Bear Class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Age and hunger score for each bear each day of the week."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bear hunger after eating fish."""
        self.hunger_score += num_fish
        return None
