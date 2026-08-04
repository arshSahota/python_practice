test_results = [
    {"test": "Login", "status": "PASS"},
    {"test": "Dashboard", "status": "FAIL"},
    {"test": "Reports", "status": "PASS"},
    {"test": "Alarms", "status": "FAIL"},
    {"test": "Users", "status": "PASS"}
]

def analyze_results(test_results):

    pass_count = 0
    fail_count = 0
    failed_tests = []

    for result in test_results:

        if "test" in result and "status" in result:
            test = result["test"]
            status = result["status"]

            if status == "PASS":
                pass_count+=1
            else:
                fail_count+=1
                failed_tests.append(test)

    pass_percentage = (pass_count * 100)/(pass_count+fail_count)

    return {
        "passed":  pass_count,
        "failed": fail_count,
        "pass_rate":  pass_percentage,
        "failed_tests": failed_tests
    }

print(analyze_results(test_results))
