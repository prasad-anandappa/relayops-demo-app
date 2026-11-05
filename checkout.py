"""Checkout entry point for the RelayOps demo shop (stdlib only)."""

import traceback

from pricing import total_cents


def checkout(cart, discount=None):
    """Charge a cart. Returns a fake receipt dict, or raises."""
    total = total_cents(cart["items"], discount)
    return {"status": "ok", "charged_cents": total}


if __name__ == "__main__":
    # The failing case from the bug report: customer typed a discount
    # code, the code lookup found nothing, discount stayed None, and
    # checkout still tried to apply it.
    cart = {"items": [{"name": "Switch sticker pack", "price_cents": 1200, "qty": 1}]}
    try:
        print(checkout(cart, discount=None))
    except Exception:
        traceback.print_exc()
