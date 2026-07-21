# temperatures = [22, 31, 17, 25, 35, 20]

# def validate_temps(temperatures):
#     res = []
#     for temp in temperatures:
#         if 18 <= temp <= 30:
#             res.append("VALID")
#         elif temp > 30:
#             res.append("HIGH_TEMP")
#         else:
#             res.append("LOW_TEMP")

#     return res

# print(validate_temps(temperatures))

# def count_temps(temperatures):
#     counts = {}

#     for temp in temperatures:
#         if 18 <= temp <= 30:
#             counts["valid"] = counts.get("valid", 0) + 1
#         elif temp > 30:
#             counts["high_temp"] = counts.get("high_temp", 0) + 1
#         else:
#             counts["low_temp"] = counts.get("low_temp", 0) + 1

#     return counts

# print(count_temps(temperatures))
