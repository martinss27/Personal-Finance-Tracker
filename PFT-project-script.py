from datetime import datetime
#using a list of dictionaries to store transactions
transactions = [
    {"date": "2024-03-05", "amount": -50, "category": "Food"},
    {"date": "2024-03-06", "amount": 2000, "category": "Salary"},
    {"date": "2024-03-04", "amount": -30, "category": "Transport"}
]

#use merge sort to sort transactions by date. Stable algorithm, good for multiple transactions in a day

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def merge_sort(transactions):
    if len(transactions) <= 1:
        return transactions

    mid = len(transactions) // 2
    left_half = merge_sort(transactions[:mid])
    right_half = merge_sort(transactions[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_transactions = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["date"] <= right[j]["date"]:
            sorted_transactions.append(left[i])
            i += 1
        else:
            sorted_transactions.append(right[j])
            j += 1

    sorted_transactions.extend(left[i:])
    sorted_transactions.extend(right[j:])
    return sorted_transactions

# save transactions to a csv file
import csv

def save_transactions(transactions, filename="transactions.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "amount", "category"])
        writer.writeheader()
        writer.writerows(transactions)

#load transactions when I start the program

def load_transactions(filename="transactions.csv"):
    transactions = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append({"date": row["date"], "amount": float(row["amount"]), "category": row["category"]})
    except FileNotFoundError:
        pass
    return transactions

# making the main menu

transactions = load_transactions()

while True:
    print("\nPersonal Finance Tracker")
    print("1. Add Transaction")
    print("2. View Transactions (Sorted by Date)")
    print("3. Search by Category")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            date = input('enter date(YYYY:MM:DD): ')
            if validate_date(date):
                break
            print('invalid date format. Please enter in YYYY-MM-DD format.')

        amount = float(input('enter amount(+ for income, - for expense): '))
        category = input('Enter category: ')

        transactions.append({"date": date, "amount": amount, "category": category})
        save_transactions(transactions)    

    elif choice == "2":
        sorted_transactions = merge_sort(transactions)
        for t in sorted_transactions:
            print(f"{t['date']} | ${t['amount']} | {t['category']}")

    elif choice == "3":
        category = input("Enter category to search: ")
        results = search_by_category(transactions, category)
        for r in results:
            print(f"{r['date']} | ${r['amount']} | {r['category']}")

    elif choice == "4":
        break

    else:
        print("Invalid option. Try again.")
