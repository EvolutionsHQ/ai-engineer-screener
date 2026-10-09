"""Starter smoke checks are deliberately incomplete, not acceptance evidence."""
import unittest
from reconcile import reconcile


class SmokeTests(unittest.TestCase):
    def test_ordinary_match(self):
        a={'payment_id':'P-1','account_id':'A-1','currency':'USD','amount':'10.00'}
        self.assertEqual(reconcile([a],[dict(a)]), [{'payment_id':'P-1','status':'matched'}])

    def test_missing_observation(self):
        a={'payment_id':'P-1','account_id':'A-1','currency':'USD','amount':'10.00'}
        self.assertEqual(reconcile([a],[]), [{'payment_id':'P-1','status':'review'}])
