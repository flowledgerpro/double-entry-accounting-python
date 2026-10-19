import unittest
from decimal import Decimal
from src.accounting import Entry, calculate_invoice, invoice_journal, money, trial_balance, validate_journal

class AccountingTests(unittest.TestCase):
    def test_rounding(self):
        self.assertEqual(money('1.005'), Decimal('1.01'))

    def test_invoice_totals(self):
        result = calculate_invoice([{'quantity': 2, 'unit_price': '150'}, {'quantity': 1, 'unit_price': '75'}], '0.08')
        self.assertEqual(result['subtotal'], Decimal('375.00'))
        self.assertEqual(result['tax'], Decimal('30.00'))
        self.assertEqual(result['total'], Decimal('405.00'))

    def test_balanced_invoice_journal(self):
        invoice = calculate_invoice([{'quantity': 1, 'unit_price': '100'}], '0.10')
        self.assertTrue(validate_journal(invoice_journal(invoice)))

    def test_zero_tax_invoice(self):
        invoice = calculate_invoice([{'quantity': 1, 'unit_price': '20'}])
        self.assertEqual(len(invoice_journal(invoice)), 2)

    def test_unbalanced_journal_rejected(self):
        with self.assertRaises(ValueError):
            validate_journal([Entry('Cash', debit='10'), Entry('Revenue', credit='9')])

    def test_invalid_tax_rate_rejected(self):
        with self.assertRaises(ValueError):
            calculate_invoice([], '1.1')

    def test_negative_quantity_rejected(self):
        with self.assertRaises(ValueError):
            calculate_invoice([{'quantity': -1, 'unit_price': '10'}])

    def test_negative_entry_rejected(self):
        with self.assertRaises(ValueError):
            Entry('Cash', debit='-1')

    def test_double_sided_entry_rejected(self):
        with self.assertRaises(ValueError):
            Entry('Cash', debit='1', credit='1')

    def test_trial_balance(self):
        invoice = calculate_invoice([{'quantity': 1, 'unit_price': '50'}], '0.10')
        balances = trial_balance(invoice_journal(invoice))
        self.assertEqual(balances['Accounts Receivable']['debit'], Decimal('55.00'))
        self.assertEqual(balances['Output Tax Payable']['credit'], Decimal('5.00'))

if __name__ == '__main__':
    unittest.main()
