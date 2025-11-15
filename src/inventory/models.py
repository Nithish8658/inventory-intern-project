from datetime import date


class Item:
    """
    Represents a basic inventory item.
    """

    def __init__(self, item_id, name, quantity, price, category):
        # Basic validation
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if price <= 0:
            raise ValueError("Price must be greater than 0.")

        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def update_quantity(self, amount):
        """
        Adds or subtracts from the current quantity.
        """
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            raise ValueError("Resulting quantity cannot be negative.")

        self.quantity = new_quantity

    def get_total_value(self):
        """
        Returns total value of this item (price * quantity).
        """
        return self.quantity * self.price

    def to_dict(self):
        """
        Converts item to a dictionary (useful for saving to JSON/CSV).
        """
        return {
            "item_id": self.item_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "category": self.category,
            "type": "Item",  # Helps identify type during loading
        }


class PerishableItem(Item):
    """
    Represents items that expire (milk, eggs, vegetables, etc.).
    """

    def __init__(self, item_id, name, quantity, price, category, expiry_date):
        super().__init__(item_id, name, quantity, price, category)

        if not isinstance(expiry_date, date):
            raise ValueError("expiry_date must be a datetime.date object.")

        self.expiry_date = expiry_date

    def is_expired(self):
        """
        Returns True if today's date is after expiry_date.
        """
        return date.today() > self.expiry_date

    def to_dict(self):
        """
        Convert to dictionary with expiry date.
        """
        data = super().to_dict()
        data["expiry_date"] = self.expiry_date.isoformat()
        data["type"] = "PerishableItem"
        return data
