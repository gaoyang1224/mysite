from jsonpath import jsonpath

json_dict = {'id': 1000394244, 'token': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMDAzOTQyNDQsImV4cCI6MTYxOTYyMDg3OH0.gfomYiwqpeVVr81So0pNmMwkQDZH64xO6mgSLrpKGgKjIiwKShX7iDJxXnXbj0V6qxCJ6e5TYv4mZQnqxhJDkQ', 'leave_amount': 600001.0}
resp = jsonpath(json_dict, '$..id')
print(resp)
