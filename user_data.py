users = [
    {"name": "A", "balance": 100},
    {"name": "B", "balance": 200}
]

def find_user(name, users):
    for user in users:
        if name == user["name"]:
            return user

    return None

select_user = input("User 'A' or User 'B':").upper()

result = find_user(select_user, users)

if result:
    print("User Found")
    print("Before balance deposit:", result["balance"])

    result["balance"] += 500
    print("After Balance Deposit:", result["balance"])

else:
    print("User Not Found")


