#! /usr/bin/env python
# -*- coding: utf-8 -*-
from requests import Session
from check_code import check_code
import sys
session = Session()
try:
    is_valid = check_code('/check/vat/',sys.argv[1])
except IndexError:
    print "Use: check_vat.py VAT"
    sys.exit(1)
except:
    sys.exit(2)
print "El DNI {} és {}".format(sys.argv[1], 
    "vàlid" if is_valid else "invàlid")
