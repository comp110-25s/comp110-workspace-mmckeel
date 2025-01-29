"""A program to plan my tea party!"""

__author__: str = "730556813"


def main_planner(guests: int) -> None:
    """Number of guests attending the party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Number of tea bags needed for the party"""
    return 2 * people


def treats(people: int) -> int:
    """Number of treats needed for the party"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How Many Guests Are Attending Your Tea Party?")))
