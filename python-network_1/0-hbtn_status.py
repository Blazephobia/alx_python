import requests

url = 'https://alu-intranet.hbtn.io/status'

try:
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
