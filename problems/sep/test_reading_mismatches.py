# import pytest

# readings = [
#     {"sensor": "Room1", "expected": 22, "actual": 23},
#     {"sensor": "Room2", "expected": 20, "actual": 28},
#     {"sensor": "Room3", "expected": 25, "actual": 25},
#     {"sensor": "Room4", "expected": 18, "actual": 14},
# ]

# tolerance = 3

# def analyze_readings(readings, tolerance):
#     within_tolerance = []
#     out_of_tolerance = []
#     largest_difference = {}
#     invalid = []
#     max_difference = 0

#     for reading in readings:

#         if "expected" not in reading:
#             invalid.append({
#                 "sensor": reading.get("sensor"),
#                 "reason": "MISSING EXPECTED"
#             })
#             continue

#         if "actual" not in reading:
#             invalid.append({
#                 "sensor": reading.get("sensor"),
#                 "reason": "MISSING_ACTUAL"
#             })
#             continue

#         difference = abs(reading["expected"] - reading["actual"])

#         if difference > max_difference:
#             largest_difference["sensor"] = reading.get("sensor")
#             largest_difference["difference"] = difference
#             max_difference = difference

#         if difference <= tolerance:
#             within_tolerance.append({
#                 "sensor": reading.get("sensor"),
#                 "difference": difference
#             })
#         else:
#             out_of_tolerance.append({
#                 "sensor": reading.get("sensor"),
#                 "difference": difference
#             })


#     return {
#         "within_tolerance": within_tolerance,
#         "out_of_tolerance": out_of_tolerance,
#         "within_count": len(within_tolerance),
#         "out_count": len(out_of_tolerance),
#         "largest_difference": largest_difference,
#         "invalid": invalid
#     }

# print(analyze_readings(readings, tolerance))

# def test_within_tolerance():

#     data = [{"sensor": "BLAH", "expected": 21, "actual": 19}]

#     result = analyze_readings(data, 3)

#     assert result["within_tolerance"] == [{"sensor": "BLAH", "difference": 2}]

# def test_out_of_tolerance():

#     data = [{"sensor": "BLAH", "expected": 90, "actual": 15}]

#     result = analyze_readings(data, 3)

#     assert result["out_of_tolerance"] == [{"sensor": "BLAH", "difference": 75}]

# def test_boundary_case():

#     data = [{"sensor": "BLAH", "expected": 3, "actual": 0}]

#     result = analyze_readings(data, 3)

#     assert result["within_tolerance"] == [{"sensor": "BLAH", "difference": 3}]

# def test_missing_actual():

#     data = [{"sensor": "BLAH", "expected": 5}]

#     result = analyze_readings(data, 3)

#     assert result["invalid"] == [{"sensor": "BLAH", "reason": "MISSING_ACTUAL"}]

# def test_largest_difference():

#     data = [{"sensor": "A", "expected": 3, "actual": 0},{"sensor": "B", "expected": 8, "actual": 0}]

#     result = analyze_readings(data, 3)

#     assert result["largest_difference"] == {"sensor": "B", "difference": 8}