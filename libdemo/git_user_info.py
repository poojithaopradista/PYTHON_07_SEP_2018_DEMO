
import requests

user = input("Enter git user id:")
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code == 404:
    print("Sorry! User id not found!")
else:
    details = resp.json()
    print("Name      :  ", details["name"])
    print("Company   :  ", details["company"])
    print("Location  :  ", details["location"])


