"""Educational double-entry accounting primitives; not tax or financial advice."""
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal('0.01')

def money(value):
    return Decimal(str(value)).quantize(CENT, rounding=ROUND_HALF_UP)

@dataclass(frozen=True)
class Entry:
    account: str
    debit: Decimal = Decimal('0.00')
    credit: Decimal = Decimal('0.00')

    def __post_init__(self):
        object.__setattr__(self, 'debit', money(self.debit))
        object.__setattr__(self, 'credit', money(self.credit))
        if not self.account or self.debit < 0 or self.credit < 0:
            raise ValueError('Account required; amounts cannot be negative')
        if (self.debit > 0) == (self.credit > 0):
            raise ValueError('Exactly one positive debit or credit is required')


def validate_journal(entries):
    if not entries:
        raise ValueError('Journal must contain entries')
    debit = sum((e.debit for e in entries), Decimal('0.00'))
    credit = sum((e.credit for e in entries), Decimal('0.00'))
    if debit != credit:
        raise ValueError(f'Unbalanced journal: debit={debit}, credit={credit}')
    return True


def calculate_invoice(items, tax_rate='0'):
    rate = Decimal(str(tax_rate))
    if not 0 <= rate <= 1:
        raise ValueError('Tax rate must be between 0 and 1')
    subtotal = Decimal('0.00')
    for item in items:
        qty = Decimal(str(item['quantity']))
        unit_price = Decimal(str(item['unit_price']))
        if qty <= 0 or unit_price < 0:
            raise ValueError('Quantity must be positive; price cannot be negative')
        subtotal += qty * unit_price
    subtotal = money(subtotal)
    tax = money(subtotal * rate)
    return {'subtotal': subtotal, 'tax': tax, 'total': subtotal + tax}


def invoice_journal(invoice):
    """Post a credit sale: AR debit, revenue and output-tax credits."""
    entries = [Entry('Accounts Receivable', debit=invoice['total'])]
    if invoice['subtotal'] > 0:
        entries.append(Entry('Sales Revenue', credit=invoice['subtotal']))
    if invoice['tax'] > 0:
        entries.append(Entry('Output Tax Payable', credit=invoice['tax']))
    validate_journal(entries)
    return entries


def trial_balance(entries):
    validate_journal(entries)
    balances = {}
    for entry in entries:
        row = balances.setdefault(entry.account, {'debit': Decimal('0.00'), 'credit': Decimal('0.00')})
        row['debit'] += entry.debit
        row['credit'] += entry.credit
    return balances
