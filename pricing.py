"""Pricing for the RelayOps demo shop.

Planted bug (for the /triage demo): a cart whose discount was never set
carries discount=None, and checkout dereferences it — the exact failure
the "Add percentage discount codes" PR introduced.
"""


def apply_discount(price_cents: int, discount) -> int:
    """Return the price after applying a percentage discount.

    `discount` is a dict like {"percent": 10} — or None when the cart
    has no discount code.
    """
    # BUG: no None guard — TypeError: 'NoneType' object is not subscriptable
    percent = discount["percent"]
    return price_cents - (price_cents * percent // 100)


def total_cents(items, discount=None) -> int:
    subtotal = sum(item["price_cents"] * item["qty"] for item in items)
    return apply_discount(subtotal, discount)
