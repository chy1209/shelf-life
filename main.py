import json
import os

def add_item():
    name = input("Enter item name: ")
    exp_date = input("Enter expiration date (MM-DD-YYYY): ")

    filename = 'data.json'
    items = []

    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        file = open(filename, 'r')
        items = json.load(file)
        file.close()

    new_item = {
        "name": name,
        "expiration_date": exp_date
    }
    items.append(new_item)

    file = open(filename, 'w')
    json.dump(items, file, indent=4)
    file.close()

    print(f"\nSaved {name} (Expires: {exp_date}) to {filename}.")


def main():
    while True:
        print("\n--- Expiration Date Tracker ---")
        print("1. Add a new item")
        print("2. View all items")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "3":
            print("Goodbye!")
            break
        elif choice == "1":
            add_item()
            break
        # need to implement choice 2 still

if __name__ == "__main__":
    main()