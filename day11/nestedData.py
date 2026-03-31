# This is what an API response looks like
response = {
    "status": 200,
    "users": [
        {"id": 1, "name": "Thomas", "tags": ["admin", "editor"]},
        {"id": 2, "name": "Alice", "tags": ["viewer"]},
    ]
}

users = response["users"]
for user in users:
    print(f"{user['name']}:")
    for tag in user["tags"]:
        print(f" - {tag}")
        

def get_names(users):
    return[u["name"] for u in users]
print(get_names(users))

def has_tag(users, tag):
    return [u for u in users if tag in u["tags"]]
print(has_tag(users,"viewer"))


def group_by_tags(users):
    result = {}
    for user in users:
        for tag in user["tags"]:
            if tag not in result:
                result[tag] = []
            result[tag].append(user["name"])
    return result

print(group_by_tags(users))