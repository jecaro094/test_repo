buildings_1 = [{"store": False}, {"store": False}, {"store": True}]


buildings_2 = [
    {"store": False},
    {"store": True},
    {"store": False},
    {"store": False},
    {"store": True},
    {"store": False},
    {"store": False},
]


buildings_3 = [{"store": True}, {"store": False}, {"store": True}, {"store": False}]


buildings_4 = [{"store": False}, {"store": False}]


test_1_params = {
    "params": "buildings, building, expected_response",
    "values": [
        (buildings_1, "store", [2, 1, 0]),
        (buildings_2, "store", [1, 0, 1, 1, 0, 1, 2]),
        (buildings_3, "store", [0, 1, 0, 1]),
        (buildings_4, "store", None),
    ],
}
