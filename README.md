# relayops-demo-app

The tiny seeded shop the RelayOps demo triages. Stdlib-only Python.

- `pricing.py` — cart totals.
- `checkout.py` — run it; it prints a receipt for the sample cart:

  ```
  $ python3 checkout.py
  {'status': 'ok', 'charged_cents': 1200}
  ```

Main is the shop as it stands on demo morning: checkout works, and
there is no discount-code support yet. The open PR "Add percentage
discount codes" adds it — and the bug report in the RelayOps demo
(Beat 2 of `DEMO-SCRIPT.md` in the RelayOps repo) is about what that
change does to checkout.
