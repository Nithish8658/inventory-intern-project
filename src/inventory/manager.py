from .models import Item, PerishableItem


class InventoryManager:
    """
    Manages inventory items using a dictionary for fast lookup.
    """

    def __init__(self):
        self.items = {}       # item_id -> Item or PerishableItem
        self.categories = set()  # unique categories

    # ---------------------------------------------------------
    # ADD ITEM
    # ---------------------------------------------------------
    def add_item(self, item):
        if item.item_id in self.items:
            raise KeyError("Item ID already exists.")

        self.items[item.item_id] = item
        self.categories.add(item.category)

    # ---------------------------------------------------------
    # REMOVE ITEM
    # ---------------------------------------------------------
    def remove_item(self, item_id):
        if item_id not in self.items:
            raise KeyError("Item ID not found.")

        item = self.items.pop(item_id)

        # If category becomes empty, remove it from the set
        if not any(i.category == item.category for i in self.items.values()):
            self.categories.discard(item.category)

    # ---------------------------------------------------------
    # UPDATE QUANTITY
    # ---------------------------------------------------------
    def update_quantity(self, item_id, amount):
        if item_id not in self.items:
            raise KeyError("Item ID not found.")

        item = self.items[item_id]
        item.update_quantity(amount)

    # ---------------------------------------------------------
    # SEARCH (BY NAME)
    # ---------------------------------------------------------
    def search_by_name(self, name):
        name = name.lower()
        return [
            item for item in self.items.values()
            if name in item.name.lower()
        ]

    # ---------------------------------------------------------
    # SEARCH (BY CATEGORY)
    # ---------------------------------------------------------
    def search_by_category(self, category):
        return [
            item for item in self.items.values()
            if item.category.lower() == category.lower()
        ]

    # ---------------------------------------------------------
    # LOW STOCK
    # ---------------------------------------------------------
    def low_stock(self, threshold=5):
        return [
            item for item in self.items.values()
            if item.quantity <= threshold
        ]

    # ---------------------------------------------------------
    # TOTAL VALUE OF INVENTORY
    # ---------------------------------------------------------
    def total_value(self):
        return sum(item.get_total_value() for item in self.items.values())

    # ---------------------------------------------------------
    # SUMMARY (for detailed reporting)
    # ---------------------------------------------------------
    def summary(self):
        """
        Returns a tuple containing:
        - number of items
        - number of categories
        - total stock value
        """
        return (
            len(self.items),
            len(self.categories),
            self.total_value()
        )

    # ---------------------------------------------------------
    # GET ALL ITEMS (used by CLI)
    # ---------------------------------------------------------
    def get_all_items(self):
        return list(self.items.values())
