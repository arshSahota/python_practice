# import pytest
# from controller import determine_controller_status

# @pytest.mark.parametrize(
#     "cpu, memory, expected", 
#     [
#         (45, 50, "HEALTHY"),
#         (80, 40, "WARNING"),
#         (40, 80, "WARNING"),
#         (90, 20, "WARNING"),
#         (91, 20, "CRITICAL"),
#         (20, 91, "CRITICAL")
#     ]
# )

# def test_determine_controller_status(cpu, memory, expected):
#     assert determine_controller_status(cpu, memory) == expected

# #30 is important because 30 is a boundry value, usually boundary values require special attention because test cases may miss it or test them incorrectly!