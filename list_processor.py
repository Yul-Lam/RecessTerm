import csv
import random
import string
from functools import reduce
from pathlib import Path


CSV_FILE = Path("users.csv")
CITIES = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]


def create_mock_user_csv(path=CSV_FILE, rows=1000):
    """Create a mock CSV file with fake user data."""
    with path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Email", "Age", "City", "Purchase_Amount"])

        for i in range(rows):
            name = f"User{i:04d}"
            email = f"{name.lower()}@example.com"
            age = random.randint(18, 75)
            city = random.choice(CITIES)
            purchase_amount = round(random.uniform(10.0, 500.0), 2)
            writer.writerow([name, email, age, city, f"{purchase_amount:.2f}"])

    return path


def load_user_csv(path=CSV_FILE):
    """Load user records from a CSV file into a list of dictionaries."""
    users = []
    with path.open("r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(
                {
                    "Name": row["Name"].strip(),
                    "Email": row["Email"].strip(),
                    "Age": int(row["Age"]),
                    "City": row["City"].strip(),
                    "Purchase_Amount": float(row["Purchase_Amount"]),
                }
            )
    return users


def filter_over_30_spenders(users):
    """Find all users over 30 who spent more than $100."""
    return list(
        filter(
            lambda user: user["Age"] > 30 and user["Purchase_Amount"] > 100,
            users,
        )
    )


def emails_for_users(users):
    """Create a list of email addresses from a list of users."""
    return list(map(lambda user: user["Email"], users))


def new_york_name_age(users):
    """Generate Name: Age strings for users in New York."""
    return [f"{user['Name']}: {user['Age']}" for user in users if user["City"] == "New York"]


def total_purchase_amount(users):
    """Calculate the total purchase amount of the entire dataset."""
    return reduce(
        lambda acc, user: acc + user["Purchase_Amount"],
        users,
        0.0,
    )


def top_oldest_user_names(users, n=5):
    """Sort and return the names of the top N oldest users."""
    sorted_users = sorted(users, key=lambda user: user["Age"], reverse=True)
    return [user["Name"] for user in sorted_users[:n]]


def main():
    if not CSV_FILE.exists():
        print(f"Creating sample CSV file: {CSV_FILE}")
        create_mock_user_csv(CSV_FILE, rows=1000)

    users = load_user_csv(CSV_FILE)

    high_spenders = filter_over_30_spenders(users)
    high_spender_emails = emails_for_users(high_spenders)
    new_york_strings = new_york_name_age(users)
    total_purchase = total_purchase_amount(users)
    oldest_names = top_oldest_user_names(users, n=5)

    print("Users over 30 who spent more than $100:")
    print(f"- Count: {len(high_spenders)}")
    print(f"- Example emails: {high_spender_emails[:10]}")
    print()
    print("Users in New York (Name: Age):")
    print(f"- Count: {len(new_york_strings)}")
    print(f"- Sample: {new_york_strings[:10]}")
    print()
    print(f"Total purchase amount: ${total_purchase:,.2f}")
    print(f"Top 5 oldest users: {oldest_names}")


if __name__ == "__main__":
    main()
