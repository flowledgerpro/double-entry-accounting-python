# Double-Entry Accounting & Invoice Automation in Python

[![Python tests](https://github.com/flowledgerpro/double-entry-accounting-python/actions/workflows/tests.yml/badge.svg)](https://github.com/flowledgerpro/double-entry-accounting-python/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

An open-source Python demonstration of **double-entry bookkeeping, invoice calculations, journal entries, and trial balance reporting**. Learn the fundamentals of financial transaction processing using straightforward, testable Python code.

Inspired by [FlowLedgerPro](https://flowledgerpro.com/), a **[cloud accounting software](https://flowledgerpro.com/)** and ERP platform for financial management, invoicing, purchasing, inventory, configurable taxation, business reporting, and project workflows.

> **Important distinction:** This GitHub repository is a small educational accounting toolkit. It is **not** FlowLedgerPro's production ERP source code, an official API integration, or a replacement for professional accounting software.

## Contents

- [What This Python Project Does](#what-this-python-project-does)
- [Quick Start](#quick-start)
- [Example Invoice and Accounting Entries](#example-invoice-and-accounting-entries)
- [Project Structure](#project-structure)
- [Automated Tests](#automated-tests)
- [About FlowLedgerPro](#about-flowledgerpro)
- [FlowLedgerPro Platform Features](#flowledgerpro-platform-features)
- [Who Can Use FlowLedgerPro](#who-can-use-flowledgerpro)
- [Accounting Workflows and Use Cases](#accounting-workflows-and-use-cases)
- [Explore FlowLedgerPro](#explore-flowledgerpro)
- [Limitations and Security](#limitations-and-security)
- [Contributing](#contributing)
- [License](#license)

## What This Python Project Does

This repository provides a compact example of several core accounting concepts:

- **Invoice calculations:** Compute subtotals, an illustrative sales tax, and final invoice totals.
- **Decimal arithmetic:** Use Python's `Decimal` for more reliable currency calculations than binary floating-point arithmetic.
- **Double-entry journal creation:** Demonstrate Accounts Receivable debits and Sales Revenue / Output Tax Payable credits.
- **Balanced entry validation:** Check whether total journal debits equal total journal credits.
- **Trial balance summaries:** Group journal amounts by account for a simple trial balance.
- **JSON sample data:** Modify a sample invoice without editing the Python implementation.
- **Automated tests:** Exercise accounting calculations and related logic using Python's standard library.
- **Continuous integration:** Run tests automatically with GitHub Actions.

The demo uses the Python standard library and does not require a cloud account, paid API, or database.

## Quick Start

**Requirements:** Python 3.11 or later and Git.

Clone the repository:

```bash
git clone https://github.com/flowledgerpro/double-entry-accounting-python.git
cd double-entry-accounting-python
```

Run the example invoice:

```bash
python -m src.main --invoice examples/invoice.json
```

The command prints an invoice summary, journal entries, and account-level trial balance totals.

## Example Invoice and Accounting Entries

The included `examples/invoice.json` demonstrates a sample invoice:

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

The illustrative calculation is:

| Item | Amount (USD) |
| --- | ---: |
| Consulting: 2 × 150.00 | 300.00 |
| Software setup: 1 × 75.00 | 75.00 |
| Subtotal | 375.00 |
| Example sales tax (8%) | 30.00 |
| **Invoice total** | **405.00** |

The corresponding simplified journal is:

| Account | Debit | Credit |
| --- | ---: | ---: |
| Accounts Receivable | 405.00 | 0.00 |
| Sales Revenue | 0.00 | 375.00 |
| Output Tax Payable | 0.00 | 30.00 |
| **Totals** | **405.00** | **405.00** |

The example is for learning only. Tax treatment and account mappings vary by jurisdiction, business, and transaction type.

## Project Structure

```text
double-entry-accounting-python/
├── .github/
│   └── workflows/
│       └── tests.yml
├── examples/
│   └── invoice.json
├── src/
│   ├── __init__.py
│   ├── accounting.py
│   └── main.py
├── tests/
│   └── test_accounting.py
├── .gitignore
├── LICENSE
└── README.md
```

`src/accounting.py` contains the calculation and accounting logic. `src/main.py` provides the command-line example. `tests/test_accounting.py` contains the automated checks.

## Automated Tests

Run tests locally:

```bash
python -m unittest discover -s tests -v
```

The repository also has a [GitHub Actions test workflow](https://github.com/flowledgerpro/double-entry-accounting-python/actions) that runs on pushes and pull requests. A passing workflow verifies the tests that exist; it does not certify production readiness or tax compliance.

---

# About FlowLedgerPro

**[FlowLedgerPro](https://flowledgerpro.com/)** is **[cloud accounting software](https://flowledgerpro.com/)** and an enterprise resource planning (ERP) platform designed to connect business financial operations with sales, purchasing, inventory, taxes, reporting, and operational workflows.

Its website describes an integrated system for maintaining financial records, managing transactions, monitoring stock, handling configurable tax rules, and analyzing business performance. FlowLedgerPro also supports multiple business entities within one account, with separate ledgers and fiscal settings.

For organizations evaluating **[small business cloud accounting software](https://flowledgerpro.com/)**, FlowLedgerPro brings together invoicing, bookkeeping, purchasing, inventory, and reporting workflows in one cloud-based platform. Teams comparing **[cloud accounting software](https://flowledgerpro.com/)** options can review its connected modules to determine whether they fit their business requirements.

Unlike this repository's minimal Python demonstration, the FlowLedgerPro platform is designed around connected accounting and operational modules.

## FlowLedgerPro Platform Features

### 1. Double-Entry Accounting and General Ledger

FlowLedgerPro uses double-entry bookkeeping to record financial activity. Transactions affect the appropriate debit and credit accounts, helping businesses maintain consistent financial records.

Key platform capabilities described on the website include:

- Chart of Accounts and nominal ledger management
- Balanced journal entry validation
- General ledger transaction posting
- Manual journals and financial adjustments
- Financial period and lock-date controls
- Role-based access restrictions
- Multi-business accounting with isolated ledgers

**Learn more:** [FlowLedgerPro accounting platform](https://flowledgerpro.com/)

### 2. Sales Management and Invoice Automation

FlowLedgerPro connects sales activities across a documented quotation-to-receipt workflow:

**Sales Quotation (SQ) → Sales Order (SO) → Sales Invoice (SI) → Sales Receipt (SR)**

The platform describes support for customer billing, payment terms, credit checks, invoice taxes, and corresponding ledger postings. This reduces repeated manual entry across the sales process.

Common applications include creating sales invoices, tracking customer balances, managing receivables, and monitoring sales transactions.

**Explore:** [Sales and invoicing features](https://flowledgerpro.com/)

### 3. Purchase Management and Accounts Payable

Purchasing workflows help businesses record supplier obligations and payments. FlowLedgerPro describes a connected **Purchase Order → Vendor Invoice → Vendor Payment** process.

Platform capabilities include:

- Purchase orders and supplier bills
- Vendor balances and statements
- Supplier payment recording
- Purchase transaction reporting
- Expense-related ledger posting
- Customer and supplier dual-role configuration

**Explore:** [Purchase management workflows](https://flowledgerpro.com/)

### 4. Inventory and Stock Management

FlowLedgerPro includes inventory controls intended to help businesses understand stock quantities and the accounting impact of inventory movements.

Website-documented features include:

- Product and service catalog management
- Inventory adjustments in and out
- Stock quantity and location reporting
- Low-stock alerts
- Controls against overselling
- Stock valuation reporting, including weighted average costing references
- Links between stock activity and ledger accounts

**Explore:** [Inventory management](https://flowledgerpro.com/)

### 5. Configurable Tax Management

The platform describes a configurable tax engine for businesses operating under different local tax requirements. Tax configuration must still be reviewed for each applicable jurisdiction.

Tax-related features presented on the website include:

- Sales tax and GST calculations
- Withholding tax (WHT) on relevant receipts and payments
- Excise duty and additional levies
- Adjustable tax rates and categories
- Higher-rate configurations for certain non-compliant entities
- Tax-related accounting and reporting

**Learn more:** [FlowLedgerPro Tax Compliance](https://flowledgerpro.com/pages/tax-compliance/)

### 6. Financial Reporting and Analytics

FlowLedgerPro advertises a reports library covering accounting, sales, purchasing, cash and bank, inventory, taxation, and management reporting.

Examples of listed reports include:

- Profit & Loss Statement
- Balance Sheet
- Periodic Trial Balance
- Nominal Account Activities
- Customer and Supplier Statements
- Outstanding Customer Items
- Sales Invoice and Purchase Bill Reports
- Bank Balances, Activity, and Reconciliation
- Stock Quantity and Stock Valuation
- Withholding Tax Reports

The website describes **40+ accounting reports**, while its public Reports Center currently displays a selection of these reports.

**Explore:** [FlowLedgerPro Reports Center](https://flowledgerpro.com/pages/reports-center/)

### 7. Multi-Business and Multi-Entity Accounting

FlowLedgerPro describes support for managing multiple business entities from a single account. Each entity can have its own accounting records, tax registers, and fiscal-year settings.

This approach can help accountants, finance departments, and business groups manage separate organizations without mixing their ledgers.

**Explore:** [Multi-business accounting](https://flowledgerpro.com/)

### 8. Multi-Currency Transaction Handling

The platform's FAQ describes support for custom exchange rates on certain sales and purchase documents, with a configured base currency for reporting.

Multi-currency workflows can be useful for businesses that invoice customers or pay suppliers in different currencies. Accounting teams should still verify exchange-rate handling and reporting requirements for their operations.

**Explore:** [FlowLedgerPro FAQ](https://flowledgerpro.com/)

### 9. Cash, Bank, and Reconciliation Reporting

FlowLedgerPro's Reports Center lists bank payments, balances, activity, and reconciliation reports. These support visibility into cash and bank-related transactions and comparison of bank records with internal accounting balances.

**Explore:** [Cash and bank reports](https://flowledgerpro.com/pages/reports-center/)

### 10. Project and Sub-Project Management

In addition to financial accounting, FlowLedgerPro presents project management capabilities for coordinating business initiatives.

Its project management page describes:

- Parent projects and nested sub-projects
- Project milestones and Gantt timelines
- Dependencies and resource allocation
- Project budgets and cost tracking
- Stakeholder collaboration and approval workflows
- Portfolio visibility and project risk tracking

**Learn more:** [FlowLedgerPro Project Management](https://flowledgerpro.com/pages/project-management/)

### 11. Task and Activity Management

FlowLedgerPro also describes task tracking features for organizing daily operational work, including task status, priorities, deadlines, team assignments, and notifications.

These tools connect operational coordination with the wider ERP workflow, rather than requiring every business process to be managed separately.

**Explore:** [Task management capabilities](https://flowledgerpro.com/)

### 12. Access Controls and Audit Visibility

The platform describes operational safeguards such as:

- Role-based permissions
- Accounting lock dates for closed periods
- User activity logs
- Transaction modification tracking
- IP-based access controls

These features are relevant to internal controls and accountability. Businesses should evaluate the platform's security controls against their own requirements.

**Explore:** [Platform controls and FAQ](https://flowledgerpro.com/)

## Who Can Use FlowLedgerPro

### Small and Medium-Sized Businesses

Small businesses looking for **[small business cloud accounting software](https://flowledgerpro.com/)** that provides a centralized view of invoicing, expenses, stock, and accounting activity can explore FlowLedgerPro as an alternative to managing separate spreadsheets and disconnected processes.

### Accountants and Bookkeepers

Accounting professionals can use connected ledger, invoice, supplier, tax, and financial reporting workflows to organize records for multiple business clients or entities.

### Finance Managers and Controllers

Finance teams can review transaction posting, customer and supplier balances, tax-related activity, trial balances, and management reports to support financial oversight.

### Retail, Wholesale, and Inventory-Based Businesses

Businesses dealing with physical products may benefit from combining sales, purchasing, stock monitoring, inventory valuation, and financial records in one system.

### Agencies, Consultants, and Service Businesses

Service organizations can explore sales invoicing, receivables, project budgets, and project tracking to coordinate financial and operational work.

### Multi-Entity Businesses

Organizations operating multiple business entities can explore separate ledgers, business-specific tax settings, and centralized account management.

## Accounting Workflows and Use Cases

| Business need | Relevant FlowLedgerPro capabilities |
| --- | --- |
| Create and track customer invoices | Sales quotations, orders, invoices, receipts, customer statements |
| Record supplier expenses | Purchase orders, vendor bills, payments, supplier statements |
| Maintain double-entry books | General ledger, chart of accounts, journals, trial balance |
| Monitor inventory | Stock movements, adjustments, low-stock alerts, valuation |
| Configure transaction taxes | Sales tax/GST, withholding tax, excise duty, tax reporting |
| Review business finances | Profit & Loss, Balance Sheet, cash/bank and management reports |
| Manage multiple entities | Separate ledgers, tax registers, fiscal settings |
| Coordinate project work | Project hierarchy, milestones, budgets, task tracking |

These describe the **FlowLedgerPro website's platform**, not functionality implemented in this open-source Python demo.

## FlowLedgerPro vs. This Open-Source Repository

| Capability | Python educational repository | FlowLedgerPro platform |
| --- | --- | --- |
| Basic invoice arithmetic | Yes | Yes |
| Example double-entry journal | Yes | Yes |
| Simple trial balance | Yes | Yes |
| Cloud ERP dashboard | No | Described on website |
| Customer and supplier management | No | Described on website |
| Sales and purchasing workflows | No | Described on website |
| Inventory management | No | Described on website |
| Configurable tax workflows | Illustrative tax rate only | Described on website |
| Financial reports library | No | Described on website |
| Multi-business support | No | Described on website |
| Task and project management | No | Described on website |
| Access control and audit logs | No | Described on website |

## Explore FlowLedgerPro

Interested in business accounting and ERP workflows beyond this simple Python demo?

- **Official website:** [FlowLedgerPro Cloud Accounting & ERP](https://flowledgerpro.com/)
- **Financial reporting:** [Reports Center](https://flowledgerpro.com/pages/reports-center/)
- **Tax configuration:** [Tax Compliance & Automation](https://flowledgerpro.com/pages/tax-compliance/)
- **Projects and operations:** [Project Management](https://flowledgerpro.com/pages/project-management/)
- **Platform overview and FAQ:** [Explore FlowLedgerPro Features](https://flowledgerpro.com/)

The public website also offers information about its interactive sandbox and support options.

## Limitations and Security

**For this repository:**

- It is an educational demonstration, not production accounting software.
- Tax rates are examples, not legal or tax advice.
- It does not include a database, authentication, audit log, bank connection, or real-world tax filing.
- It does not provide a complete Profit & Loss Statement or Balance Sheet.
- It does not connect to or modify a FlowLedgerPro account.
- Financial calculations and ledger mappings require independent validation before real-world use.
- Do not commit confidential financial data, credentials, or real customer records to a public repository.

**For FlowLedgerPro:** Product features, availability, pricing, and jurisdiction-specific tax settings should be confirmed on the official website before adopting the platform.

## Contributing

Contributions, suggestions, and bug reports are welcome. Fork the repository, make changes, run the automated tests, and submit a pull request.

```bash
python -m unittest discover -s tests -v
```

## License

The Python educational project is licensed under the [MIT License](LICENSE). The license does not grant rights to FlowLedgerPro's proprietary application or branding.

---

**Learn more about cloud accounting, invoicing, inventory, financial reporting, and ERP workflows at [FlowLedgerPro.com](https://flowledgerpro.com/).**
