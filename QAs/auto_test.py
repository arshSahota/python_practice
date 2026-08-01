tests = [
    lambda: True,
    lambda: False,
    lambda: True
]

def run_tests(tests):
    passed = 0
    failed = 0

    for test in tests:
        result = test()

        if result:
            passed+=1
        else:
            failed+=1

    return{
        "passed": passed,
        "failed": failed
    }

print(run_tests(tests))