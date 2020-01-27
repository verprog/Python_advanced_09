import json

users ={
    'user1' : 'authenticate',
    'user2' : 'autorized',
    'user3' : 'anonym',
}

json_obj = json.dumps(users, indent=3)
result = json_obj

r = json.loads(result)

print(r)

