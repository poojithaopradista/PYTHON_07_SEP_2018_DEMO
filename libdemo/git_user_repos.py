
import requests

user = input("Enter git user id:")
resp = requests.get(f"https://api.github.com/users/{user}/repos")
if resp.status_code == 404:
    print("Sorry! User id not found!")
else:
    repos = resp.json()
    print("No. of repos  : ", len(repos))
    for repo in repos:
        print("%-30s %s" % (repo["name"], repo["description"]))



