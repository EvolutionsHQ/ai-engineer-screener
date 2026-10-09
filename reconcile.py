"""Intentionally imperfect starter. Synthetic inputs only; no financial actions."""
import json
import sys


def reconcile(expected, observed):
    bank = {row['payment_id']: row for row in observed}
    results = []
    for row in expected:
        other = bank.get(row['payment_id'])
        if other is None:
            status = 'review'
        elif float(row['amount']) == float(other['amount']):
            status = 'matched'
        else:
            status = 'mismatch'
        results.append({'payment_id': row['payment_id'], 'status': status})
    return results


if __name__ == '__main__':
    with open(sys.argv[1], encoding='utf-8') as stream:
        cases = json.load(stream)
    for case in cases:
        print(json.dumps({'case':case['name'], 'results':reconcile(case['expected'], case['observed'])}))
