# "http://www.keyou.site:8000/projects"
# "http://www.keyou.site:8000/user.login/"

import requests
url = 'http://www.keyou.site:8000/user.login/'
data = {
    "username":"lemon1",
    "password":"123456"
}
reps = requests.post(url,data)
print(reps)



url = 'http://www.keyou.site:8000/projects'
reps = requests.get(url)
print(reps)
print(reps.status_code)
print(reps.json())