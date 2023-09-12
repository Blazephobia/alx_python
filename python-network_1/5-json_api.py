import requests
import sys

# Check if the letter argument is provided
if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
data = {'q': q}

try:
    response = requests.post(url, data=data)

    # Check if the response is properly JSON formatted and not empty
    if response.status_code == 200:
        try:
            result = response.json()
            if result:
                print(f"[{result['id']}] {result['name']}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        print("No result")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
