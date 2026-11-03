user = {
    "name": "Kirill",
    "age": 24,
}

if user.get("email") is None:
    raise ValueError("Email not found")

