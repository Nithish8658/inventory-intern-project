import json
import csv
from datetime import date
from .models import Item, PerishableItem


# ---------------------------------------------------------
# SAVE TO JSON
# ---------------------------------------------------------
def save_to_json(filepath, items):
    data = [item.to_dict() for item in items]

    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


# ---------------------------------------------------------
# LOAD FROM JSON
# ---------------------------------------------------------
def load_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)

    items = []
    for item_data in data:
        if item_data["type"] == "PerishableItem":
            expiry = date.fromisoformat(item_data["expiry_date"])
            item = PerishableItem(
                item_data["item_id"],
                item_data["name"],
                item_data["quantity"],
                item_data["price"],
                item_data["category"],
                expiry,
            )
        else:
            item = Item(
                item_data["item_id"],
                item_data["name"],
                item_data["quantity"],
                item_data["price"],
                item_data["category"],
            )

        items.append(item)

    return items


# ---------------------------------------------------------
# SAVE TO CSV
# ---------------------------------------------------------
def save_to_csv(filepath, items):
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "item_id", "name", "quantity", "price",
            "category", "type", "expiry_date"
        ])

        for item in items:
            if isinstance(item, PerishableItem):
                expiry = item.expiry_date.isoformat()
                type_ = "PerishableItem"
            else:
                expiry = ""
                type_ = "Item"

            writer.writerow([
                item.item_id,
                item.name,
                item.quantity,
                item.price,
                item.category,
                type_,
                expiry
            ])


# ---------------------------------------------------------
# LOAD FROM CSV
# ---------------------------------------------------------
def load_from_csv(filepath):
    items = []

    with open(filepath, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["type"] == "PerishableItem":
                expiry = date.fromisoformat(row["expiry_date"])
                item = PerishableItem(
                    row["item_id"],
                    row["name"],
                    int(row["quantity"]),
                    float(row["price"]),
                    row["category"],
                    expiry,
                )
            else:
                item = Item(
                    row["item_id"],
                    row["name"],
                    int(row["quantity"]),
                    float(row["price"]),
                    row["category"],
                )

            items.append(item)

    return items
