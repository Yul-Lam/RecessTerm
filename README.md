# Login Auth

Simple Python script demonstrating username/password authentication.

Requirements
- Python 3

Usage

Run with username and password as command-line arguments:

```powershell
python login_auth.py alice secret
```

Or run interactively (password input will be hidden):

```powershell
python login_auth.py
# then enter Username: and Password:
```

Behavior
- Prints `login successful` when username and password match
- Prints `incorrect password` when username exists but password is wrong
- Prints `username not found` when the username does not exist
