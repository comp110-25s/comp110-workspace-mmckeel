"""File to define Fish class."""


class Fish:
    """Defines the Fish class for the simulation."""

    def __init__(self):
        """Base values of the fish population."""
        self.age: int = 0
        return None

    def one_day(self):
        """Age and hunger score for each fish each day of the week."""
        self.age += 1
        return None
