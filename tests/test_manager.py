import pytest
from datetime import date, timedelta
from inventory.manager import InventoryManager
from inventory.models import Item, PerishableItem
from inventory.persistence import save_to_json, load_from_json
import os


# ---------------------------------------------------------
# FIXTURES (Reusable setup for every test)
# ---------------------------------------------------------
@pytest.fixture
def manager():
    return InventoryManager()


# ---------------------------------------------------------
# TEST 1 — Add and retrieve item
# ---------------------------------------------------------
def test_add_item(manager):
    item = Item("1", "Pen", 10, 5.0, "Stationery")
    manager.add_item(item)

    assert len(manager.items) == 1
    assert manager.items["1"].name == "Pen"


# ---------------------------------------------------------
# TEST 2 — Low stock detection
# ---------------------------------------------------------
def test_low_stock(manager):
    item1 = Item("1", "Pen", 2, 5.0, "Stationery")
    item2 = Item("2", "Book", 20, 50.0, "Stationery")

    manager.add_item(item1)
    manager.add_item(item2)

    low = manager.low_stock(threshold=5)

    assert len(low) == 1
    assert low[0].item_id == "1"


# ---------------------------------------------------------
# TEST 3 — Save and Load JSON
# ---------------------------------------------------------
def test_json_save_and_load(tmp_path):
    filepath = tmp_path / "test_inventory.json"

    # Create temporary items
    expiry = date.today() + timedelta(days=5)
    items = [
        Item("1", "Pen", 10, 5.0, "Stationery"),
        PerishableItem("2", "Milk", 5, 2.5, "Dairy", expiry),
    ]

    # Save the items
    save_to_json(filepath, items)

    # Load the items
    loaded_items = load_from_json(filepath)

    assert len(loaded_items) == 2
    assert isinstance(loaded_items[0], Item)
    assert isinstance(loaded_items[1], PerishableItem)
    assert loaded_items[1].name == "Milk"
