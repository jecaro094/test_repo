import math
import random

import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.weather import get_weather

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def define_random_list(list_size):
    returned_list = []
    for x in range(0, list_size):
        returned_list.append(random.randint(0, 9))
    return returned_list


@app.get("/")
async def root():
    return {"random_number": define_random_list(10)}


@app.get("/weather")
async def get_weather_(city_name: str):   
    if not city_name:
        return {}
    weather_from_city = get_weather(city_name)
    weather_from_city['main'].pop('pressure')
    weather_from_city['main'].pop('humidity')
    for temp_key in ['temp', 'temp_min', 'temp_max', 'feels_like']:
        weather_from_city['main'][temp_key] -= 273.15
    return weather_from_city


def get_building_distances(buildings, building="store"):
    """
    Returns a list of integers.
    Each integer symbolizes the distance of the block with the nearest
    building considered in the function parameter.

    :param buildings: List of blocks with buildings.
    :param building: Name of the building considered, as a string.
    """

    stores = list(map(lambda x: 0 if x[building] else None, buildings))
    indexes_with_buildings = [index for index, x in enumerate(stores) if x == 0]

    if indexes_with_buildings == []:
        return None

    building_distances = []
    for i, index_with_building in enumerate(indexes_with_buildings):
        if i == 0:
            building_distances += format_list(index_with_building, ignore_left=True) + [0]
        else:
            building_distances += format_list(
                index_with_building - indexes_with_buildings[i - 1] - 1
            ) + [0]

    building_distances += format_list(
        len(buildings) - indexes_with_buildings[-1] - 1, ignore_right=True
    )

    return building_distances


def format_list(length_, ignore_left=False, ignore_right=False):
    """
    Creates a function that, given an integer length,
    returns a list with the length specified.

    The lists have a value of '1' at the begginig and at the end
    of the mentioned list.
    In the case that we consider the optional parameters, the
    behaviour is slighly different according to the tests detailed
    below.

    >>> format_list(7)
    [1, 2, 3, 4, 3, 2, 1]

    >>> format_list(3)
    [1, 2, 1]

    >>> format_list(3, ignore_right=True)
    [1, 2, 3]

    >>> format_list(3, ignore_left=True)
    [3, 2, 1]

    >>> format_list(0)
    []

    >>> format_list(3, ignore_left=True, ignore_right=True)
    [0, 0, 0]
    """

    if ignore_left and not ignore_right:
        return list(range(1, length_ + 1))[::-1]
    if ignore_right and not ignore_left:
        return list(range(1, length_ + 1))
    if ignore_left and ignore_right:
        return [0] * length_

    half_lenght = math.floor(length_ / 2)
    half_list = list(range(1, half_lenght + 1))
    if (length_ % 2) == 0:
        return half_list + half_list[::-1]

    return half_list + [half_lenght + 1] + half_list[::-1]


def get_max_minimum_distances(buildings, interested_buildings):
    """
    Returns list of max minimum distance to all buildings specified
    at 'interested_buildings'

    :param buildings: dictionary representation of buildings in the neighborhood
    :param interested_buildings: list of building names we want to be near to
    """

    all_buildings_distances = {}
    for building in interested_buildings:
        building_distances_iter = get_building_distances(buildings, building)
        if building_distances_iter is not None:
            all_buildings_distances[building] = building_distances_iter

    print("all buildings distances: ", all_buildings_distances)

    max_minimum_distance = []
    for i in zip(*all_buildings_distances.values()):
        max_minimum_distance.append(max(i))

    print("max_minimum_distance: ", max_minimum_distance)

    return np.where(max_minimum_distance == np.min(max_minimum_distance))[0].tolist()
