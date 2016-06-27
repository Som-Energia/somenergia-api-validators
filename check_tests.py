#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import b2btest
import sys
from check_cups import check_cups
from check_cnae import check_cnae
from check_iban import check_iban
from check_vat import check_vat

class CheckTest(unittest.TestCase):
    b2bdatapath="b2btests"
    def assert_code(self,fnct,state,code):
        results=fnct(code)
        if state:
            self.assertTrue(results[0])
        else:
            self.assertFalse(results[0])
        self.assertB2BEqual(results[1])

    def test_goodCups(self):
        self.assert_code(check_cups,
            True,
            "ES0987543210987654ZF")
    
    def test_existentCups(self):
        self.assert_code(check_cups,
            False,
            "ES0176002400000026ZQ0F")
    
    def test_badCups(self):
        self.assert_code(check_cups,
            False,
            "XXXX")
    
    def test_unicodeCups(self):
        self.assert_code(check_cups,
            False,
            "ñáéíóúçAXX")

    def test_goodCnae(self):
        self.assert_code(check_cnae,
            True,
            "0111")

    def test_badCnae(self):
        self.assert_code(check_cnae,
            False,
            "0111X")

    def test_unicodeCnae(self):
        self.assert_code(check_cnae,
            False,
            "´ñóñç")

    def test_goodIban(self):
        self.assert_code(check_iban,
            True,
            "ES3320805801143040000499")
        
    def test_badIban(self):
        self.assert_code(check_iban,
            False,
            "ES3320805801143040000499X")
    
    def test_unicodeIban(self):
        self.assert_code(check_iban,
            False,
            "ñóES3320805801143040000499X")

    def test_goodVat(self):
        self.assert_code(check_vat,
            True,
            '49013933J')

    def test_badVat(self):
        self.assert_code(check_vat,
            False,
            '49013933JX')
    
    def test_unicodeVat(self):
        self.assert_code(check_vat,
            False,
            'ñ49013933JX')
        
if __name__ == '__main__':
    if '--accept' in sys.argv:
        sys.argv.remove('--accept')
        unittest.TestCase.acceptMode = True
    unittest.main()
