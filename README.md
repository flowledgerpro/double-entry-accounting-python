# Double-Entry Accounting & Invoice Automation in Python

[![Python tests](https://github.com/OWNER/double-entry-accounting-python/actions/workflows/tests.yml/badge.svg)](https://github.com/OWNER/double-entry-accounting-python/actions/workflows/tests.yml)

A small, open-source **Python double-entry accounting demo** for developers learning invoice calculations, sales-tax examples, balanced journal entries, and trial balance reporting.

Inspired by the accounting and ERP workflows of [FlowLedgerPro](https://flowledgerpro.com/), a cloud accounting platform for invoicing, inventory, tax configuration, and financial reports. **This is an independent educational demonstration, not FlowLedgerPro's production code or an official integration.**

## Features

- Invoice line calculations with Python `Decimal` for currency-safe arithmetic
- Configurable **example** sales-tax rate
- Automatic sales invoice journal: Accounts Receivable (debit), Sales Revenue (credit), Output Tax Payable (credit)
- Validation of balanced debits and credits
- Basic account-level trial balance totals
- Example invoice JSON
- 10 unit tests and GitHub Actions CI
- Python standard library only; no external packages or API keys

## Quick Start

Requires Python 3.11 or later.

```bash
git clone https://github.com/OWNER/double-entry-accounting-python.git
cd double-entry-accounting-python
python -m src.main --invoice examples/invoice.json
```

Replace `OWNER` in the clone URL and badge with your GitHub username after creating the repository.

## Example Input

Edit `examples/invoice.json`:

```json
{
  "invoice_number": "DEMO-1001",
  "currency": "USD",
  "tax_rate": "0.08",
  "items": [
    {"description": "Consulting service", "quantity": 2, "unit_price": "150.00"},
    {"description": "Software setup", "quantity": 1, "unit_price": "75.00"}
  ]
}
```

The demo produces a subtotal of **375.00**, example tax of **30.00**, and total of **405.00**. Its journal records 405.00 Accounts Receivable debit, 375.00 Sales Revenue credit, and 30.00 Output Tax Payable credit.

## Run Tests

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs tests and the example CLI on pushes and pull requests.

## Project Structure

```text
double-entry-accounting-python/
├── .github/workflows/tests.yml
├── examples/invoice.json
├── src/__init__.py
├── src/accounting.py
├── src/main.py
├── tests/test_accounting.py
├── .gitignore
├── LICENSE
└── README.md
```

## Who Is This For?

- Python learners exploring accounting workflows
- Developers prototyping invoice and ledger logic
- Finance software teams reviewing basic debit/credit concepts
- Small-business owners interested in how bookkeeping automation works

## About FlowLedgerPro

[FlowLedgerPro](https://flowledgerpro.com/) provides cloud-based accounting and ERP workflows, including sales invoicing, purchase management, inventory, configurable taxes, double-entry general ledger, and financial reports. Explore its [Reports Center](https://flowledgerpro.com/pages/reports-center/) and [Tax Compliance features](https://flowledgerpro.com/pages/tax-compliance/).

This repository intentionally implements only a narrow learning example. It **does not** include FlowLedgerPro's ERP platform, live bank integration, inventory operations, user authentication, or regulatory tax filing.

## Important Limitations

- Tax rates are illustrative and **not legal or tax advice**. Actual tax rules vary by jurisdiction.
- No persistent database, audit trail, multi-currency engine, financial statements, or payment reconciliation.
- No production-grade access control or compliance certification.
- Invoice calculations and journal mappings should be independently reviewed before any real-world use.

## Contributing

Issues and pull requests are welcome. Run the tests before submitting changes.

## License

MIT License. See [LICENSE](LICENSE).
