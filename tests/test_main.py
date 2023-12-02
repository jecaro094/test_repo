import pytest
from conftests import test_1_params

from src.main import get_building_distances, get_max_minimum_distances


@pytest.mark.parametrize(
    test_1_params["params"],
    test_1_params["values"],
)
def test_get_distances(buildings, building, expected_response):
    """
    Considers several input/ expected response
    cases in order to check that we get a list with the
    distances to the building detailed in the string 'building'
    """

    response = get_building_distances(buildings, building)
    assert response == expected_response


def test_get_max_minimum_distances():
    """
    We test the successful output of the function
    'get_max_minimum_distances'
    """

    buildings = [
        {
            "store": False,
            "school": True,
            "university": False,
        },
        {
            "store": False,
            "school": False,
            "university": False,
        },
        {
            "store": False,
            "school": False,
            "university": False,
        },
        {
            "store": True,
            "school": True,
            "university": False,
        },
        {
            "store": True,
            "school": False,
            "university": False,
        },
    ]

    interested_buildings = [
        "store",
        "school",
        "university",
    ]

    res = get_max_minimum_distances(buildings, interested_buildings)
    print(res)
    assert res == [3]
