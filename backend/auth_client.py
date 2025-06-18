import requests

BASE_URL = "http://localhost:8000"
LOGIN_URL = f"{BASE_URL}/api/token/"
USERS_URL = f"{BASE_URL}/api/users/"

USERNAME = "root"
PASSWORD = "root"


def get_token(username, password):
    res = requests.post(LOGIN_URL, json={"username": username, "password": password})
    if res.status_code == 200:
        print("✅ Zalogowano!")
        return res.json()["access"]
    else:
        print("❌ Błąd logowania:", res.json())
        return None


def get_protected_resource(token, url):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        return res.json()
    else:
        print(f"❌ Błąd: {res.status_code} -> {res.text}")
        return None


def main():
    token = get_token(USERNAME, PASSWORD)
    if token:
        data = get_protected_resource(token, USERS_URL)
        if data:
            print("📦 Dane:")
            print(data)


if __name__ == "__main__":
    main()
