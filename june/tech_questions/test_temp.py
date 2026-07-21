# import pytest
# from temp import determine_alarm_state

# @pytest.mark.parametrize(
#     "temp, expected", 
#     [
#         (50, True),
#         (30, False),
#         (35, True),
#         (18, False),
#         (90, True)
#     ]
# )

# def test_determine_alarm_state(temp, expected):
#     assert determine_alarm_state(temp) == expected

# #30 is important because 30 is a boundry value, usually boundary values require special attention because test cases may miss it or test them incorrectly!