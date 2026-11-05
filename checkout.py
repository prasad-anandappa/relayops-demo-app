"""Checkout entry point for the RelayOps demo shop (stdlib only)."""

from pricing import total_cents


def checkout(cart):
    """Charge a cart. Returns a fake receipt dict, or raises."""
    total = total_cents(cart["items"])
    return {"status": "ok", "charged_cents": total}


if __name__ == "__main__":
    cart = {"items": [{"name": "Switch sticker pack", "price_cents": 1200, "qty": 1}]}
    print(checkout(cart))
