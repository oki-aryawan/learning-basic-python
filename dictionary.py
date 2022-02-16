user = {
    'id': '001',
    'name': 'oki',
    'email': 'oki271002@protonmail.com',
    'adress': {
        'street': 'Panji Anom',
        'city': 'Singaraja',
        'post-code': '09912'
    }
}



import json
result = json.dumps(user)
print(type(result))
print(result)

with open("result1.json", "w") as file :
    json.dump(user, file)
