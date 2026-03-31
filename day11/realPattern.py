users = [
    {"name": "Thomas", "role": "admin", "active": True},
    {"name": "Alice", "role": "viewer", "active": False},
    {"name": "Bob", "role": "editor", "active": True},
]

def get_active_users(users):
    return [u for u in users if u["active"]]

def get_names(users):
    return [u["name"] for u in users]

def find_by_roles(users, role):
    return [u for u in users if u["role"] == role]

active = get_active_users(users)
print(active)

names = get_names(active)
print(names)

admins = find_by_roles(users, "admin")
print(admins)


#This exact pattern is what you'll write when querying a database and transforming results.



def shout(text): return text.upper()
def whisper(text): return text.lower()


def process(text, func):
    return func(text)
print(process("Hello", shout))
print(process("Hello", whisper))

