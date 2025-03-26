"""Megan M's Dictionary Function Tests!"""

__author__: str = "730556813"

from dictionary import invert
from dictionary import count
from dictionary import favorite_color
from dictionary import bin_len
import pytest


def test_invertone() -> None:
    """Use case one for invert function"""
    assert invert({"One": "Two", "Three": "Four"}) == {"Two": "One", "Four": "Three"}


def test_inverttwo() -> None:
    """Use case two for invert function"""
    assert invert({"Chemistry": "A", "Biology": "B"}) == {
        "A": "Chemistry",
        "B": "Biology",
    }


def test_invertthree() -> None:
    """Edge case for invert function"""
    assert invert({}) == {}


with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)


def test_countone() -> None:
    """Use case one for count function"""
    assert count(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}


def test_counttwo() -> None:
    """Use case two for count function"""
    assert count(["green", "purple", "lightblue", "green", "green"]) == {
        "green": 3,
        "purple": 1,
        "lightblue": 1,
    }


def test_countthree() -> None:
    """Edge case for count function"""
    assert count([]) == {}


def test_favorite_colorone() -> None:
    """Use case one for favorite_color function"""
    assert favorite_color({"Jack": "green", "Megan": "blue", "Molly": "blue"}) == {
        "blue"
    }


def test_favorite_colortwo() -> None:
    """Use case two for favorite_color function"""
    assert favorite_color({"Jack": "orange", "Megan": "blue", "Molly": "pink"}) == {
        "orange"
    }


def test_favorite_colorthree() -> None:
    """Edge case for favorite_color function"""
    assert favorite_color({}) == ""


def test_bin_lenone() -> None:
    """Use case one for bin_len function"""
    assert bin_len(["rose", "lily", "hyacinth"]) == {
        4: {"rose", "lily"},
        7: {"hyacinth"},
    }


def test_bin_lentwo() -> None:
    """Use case two for bin_len function"""
    assert bin_len(["yellow", "purple", "red"]) == {3: {"red"}, 6: {"yellow", "purple"}}


def test_bin_lenthree() -> None:
    """Edge case for bin_len function"""
    assert bin_len([]) == {}
