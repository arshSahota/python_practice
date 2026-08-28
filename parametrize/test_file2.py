# import pytest

# def is_healthy_device(status, alarms):

#     return status == "online" and alarms == 0

# @pytest.mark.parametrize(
#     "status, alarms, expected",
#     [
#     ("online", 0, True),
#     ("online", 2, False),
#     ("offline", 0, False),
#     ("offline", 3, False)
#     ]
# )

# def test_is_healthy_device(status, alarms, expected):
#     assert is_healthy_device(status, alarms) == expected