import sys
import getpass

CREDENTIALS = {
    "alice": "secret",
    "bob": "hunter2",
}


def authenticate(username: str, password: str) -> str:
    if username in CREDENTIALS:
        if CREDENTIALS[username] == password:
            return "login successful"
        else:
            return "incorrect password"
    else:
        return "username not found"


def main() -> None:
    if len(sys.argv) >= 3:
        username = sys.argv[1]
        password = sys.argv[2]
    elif len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
        print("Usage: python login_auth.py [username password]\nRun without arguments to prompt interactively.")
        return
    else:
        username = input("Username: ").strip()
        password = getpass.getpass("Password: ").strip()

    # determine result, print it, then exit with a meaningful code
    result = authenticate(username, password)
    print(result)
    # exit codes: 0 = success, 2 = incorrect password, 1 = username not found
    if result == "login successful":
        sys.exit(0)
    elif result == "incorrect password":
        sys.exit(2)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
