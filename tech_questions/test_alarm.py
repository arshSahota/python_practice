# import pytest
# from alarm import alarm_requires_acknowledgement

# @pytest.mark.parametrize(
#     ("severity, acknowledged, expected"),
#     [
#     ("CRITICAL",True, True),
#     ("CRITICAL", False, False),
#     ("WARNING", True, True),
#     ("WARNING", False, True)
#     ]
# )

# def test_alarm_requires_acknowledgement(severity, acknowledged, expected):
#     assert (
#     alarm_requires_acknowledgement(
#         severity,
#         acknowledged
#     ) == expected
# ), (
#     f"Expected {expected} for "
#     f"severity={severity}, "
#     f"acknowledged={acknowledged}"
# )