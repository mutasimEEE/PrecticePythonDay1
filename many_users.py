users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
# print(users.items())
for username, user_info in users.items():
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = user_info['location'].title()
    print(f"\nUsername: {username}")
    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")
    