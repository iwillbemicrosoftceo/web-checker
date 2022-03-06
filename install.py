import requests
print("CHECK IF THE WEBSITE YOU ARE ACCESSING IS UP OR RUNNING!\n")
url = input("URL: ")
if url.startswith(f"https://"): 
    r = requests.get(url)
    if url.startswith("http://"): 
        r = requests.get(url)
else:
    r = requests.get(f"http://{url}")

if r.status_code != 200:
    print("Website is not running :(")
else:
    print("Website is running :)")