import argparse
from datetime import datetime
from inventory.manager import InventoryManager
from inventory.models import Item, PerishableItem
from inventory.persistence import (
    save_to_json, load_from_json,
    save_to_csv, load_from_csv
)


# Inventory manager instance (shared)
manager = InventoryManager()


# ---------------------------------------------------------
# Add Item (normal)
# ---------------------------------------------------------
def add_item():
    item_id = input("Enter Item ID: ")
    name = input("Enter Item Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    category = input("Enter Category: ")

    item = Item(item_id, name, quantity, price, category)
    manager.add_item(item)

    print("Item added successfully!\n")


# ---------------------------------------------------------
# Add Perishable Item
# ---------------------------------------------------------
def add_perishable_item():
    item_id = input("Enter Item ID: ")
    name = input("Enter Item Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    category = input("Enter Category: ")
    expiry_str = input("Enter Expiry Date (YYYY-MM-DD): ")

    expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d").date()

    item = PerishableItem(item_id, name, quantity, price, category, expiry_date)
    manager.add_item(item)

    print("Perishable item added successfully!\n")


# ---------------------------------------------------------
# List all items
# ---------------------------------------------------------
def list_items():
    items = manager.get_all_items()

    if not items:
        print("Inventory is empty.")
        return

    print("\n=== INVENTORY ITEMS ===")
    for item in items:
        print(
            f"ID: {item.item_id}, Name: {item.name}, Qty: {item.quantity}, "
            f"Price: {item.price}, Category: {item.category}"
        )
    print()


# ---------------------------------------------------------
# Search by name
# ---------------------------------------------------------
def search_by_name(query):
    results = manager.search_by_name(query)

    if not results:
        print("No items found.")
        return

    print("\nSearch Results:")
    for item in results:
        print(f"{item.name} (ID: {item.item_id})")
    print()


# ---------------------------------------------------------
# Update quantity
# ---------------------------------------------------------
def update_quantity(item_id, amount):
    manager.update_quantity(item_id, amount)
    print("Quantity updated successfully!\n")


# ---------------------------------------------------------
# Remove item
# ---------------------------------------------------------
def remove_item(item_id):
    manager.remove_item(item_id)
    print("Item removed successfully!\n")


# ---------------------------------------------------------
# Low stock
# ---------------------------------------------------------
def low_stock(threshold):
    items = manager.low_stock(threshold)

    if not items:
        print("No low-stock items.")
        return

    print("\nLow Stock Items:")
    for item in items:
        print(f"{item.name} (Qty: {item.quantity})")
    print()


# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------
def summary():
    count_items, count_categories, total_value = manager.summary()

    print("\n=== INVENTORY SUMMARY ===")
    print(f"Total Items: {count_items}")
    print(f"Total Categories: {count_categories}")
    print(f"Total Stock Value: {total_value}")
    print()


# ---------------------------------------------------------
# Save / Load JSON / CSV
# ---------------------------------------------------------
def save_json(filepath):
    save_to_json(filepath, manager.get_all_items())
    print("Saved to JSON successfully!\n")


def load_json(filepath):
    items = load_from_json(filepath)
    for i in items:
        manager.add_item(i)
    print("Loaded from JSON successfully!\n")


def save_csv(filepath):
    save_to_csv(filepath, manager.get_all_items())
    print("Saved to CSV successfully!\n")


def load_csv(filepath):
    items = load_from_csv(filepath)
    for i in items:
        manager.add_item(i)
    print("Loaded from CSV successfully!\n")


# ---------------------------------------------------------
# Main CLI using argparse
# ---------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Inventory Management CLI")

    parser.add_argument("command", help="Command to run")
    parser.add_argument("--item_id")
    parser.add_argument("--amount", type=int)
    parser.add_argument("--query")
    parser.add_argument("--threshold", type=int, default=5)
    parser.add_argument("--file")

    args = parser.parse_args()

    # Map commands
    if args.command == "add":
        add_item()
    elif args.command == "add_perishable":
        add_perishable_item()
    elif args.command == "list":
        list_items()
    elif args.command == "search":
        search_by_name(args.query)
    elif args.command == "update":
        update_quantity(args.item_id, args.amount)
    elif args.command == "remove":
        remove_item(args.item_id)
    elif args.command == "low_stock":
        low_stock(args.threshold)
    elif args.command == "summary":
        summary()
    elif args.command == "save_json":
        save_json(args.file)
    elif args.command == "load_json":
        load_json(args.file)
    elif args.command == "save_csv":
        save_csv(args.file)
    elif args.command == "load_csv":
        load_csv(args.file)
    else:
        print("Invalid command!")


if __name__ == "__main__":
    main()
