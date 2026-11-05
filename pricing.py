"""Pricing for the RelayOps demo shop."""


def total_cents(items) -> int:
    """Cart total in cents: sum of price x qty over the items."""
    return sum(item["price_cents"] * item["qty"] for item in items)
