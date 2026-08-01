def fetch_data():
    # sometimes works, sometimes fails
    raise Exception("API failed")

def retry_logic(fetch_data, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            result = fetch_data()
            return result
        except Exception as error:
            print(f"Attempt {attempt+ 1} faile: {error}")

    raise Exception("API Failed after maximum retries")

try:
    data = retry_logic(fetch_data, max_attempts=3)
    print(data)
except Exception as error:
    print(error)