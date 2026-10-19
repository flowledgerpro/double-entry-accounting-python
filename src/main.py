import argparse
import json
from pathlib import Path
from .accounting import calculate_invoice, invoice_journal, trial_balance


def main():
    parser = argparse.ArgumentParser(description='Demo invoice and double-entry journal')
    parser.add_argument('--invoice', default='examples/invoice.json', help='Path to sample invoice JSON')
    args = parser.parse_args()
    data = json.loads(Path(args.invoice).read_text(encoding='utf-8'))
    result = calculate_invoice(data['items'], data.get('tax_rate', '0'))
    entries = invoice_journal(result)
    print('INVOICE SUMMARY')
    for key, value in result.items():
        print(f'{key}: {value}')
    print('\nJOURNAL ENTRIES')
    for entry in entries:
        print(f'{entry.account}: debit={entry.debit}, credit={entry.credit}')
    print('\nTRIAL BALANCE')
    for account, totals in trial_balance(entries).items():
        print(f'{account}: debit={totals["debit"]}, credit={totals["credit"]}')


if __name__ == '__main__':
    main()
