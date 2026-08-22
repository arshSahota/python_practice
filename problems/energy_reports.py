reports = [
    {"site": "SiteA", "expected": 100, "actual": 105},
    {"site": "SiteB", "expected": 200, "actual": 190},
    {"site": "SiteC", "expected": 150, "actual": 180},
    {"site": "SiteD", "expected": 120, "actual": 121}
]

def analyze_reports(reports):

    valid = []
    invalid = []
    largest_difference = 0

    for report in reports:
        site = report.get("site", "UNKNOWN")

        if "expected" not in report:
            invalid.append({
                "name": site,
                "reason": "MISSING_EXPECTED"
            })
            continue

        if "actual" not in report:
            invalid.append({
                "site": site,
                "reason": "MISSING_ACTUAL"
            })

            continue

        expected = report["expected"]
        actual = report["actual"]
        
        difference = abs(expected - actual)

        if difference > largest_difference:
            largest_difference = difference


        if difference <= 10:
            valid.append({
                "site": site
            })

        else:
            invalid.append({
                "site": site,
                "difference": difference
            })
    return {
        "valid": valid,
        "invalid": invalid,
        "valid_count": len(valid),
        "invalid_count": len(invalid),
        "largest_difference": largest_difference
    }

print(analyze_reports(reports))