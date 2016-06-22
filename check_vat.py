#! /usr/bin/env python
# -*- coding: utf-8 -*-
from requests import Session
from check_code import check_code
import sys
session = Session()
try:
    response = check_code('/check/vat/',sys.argv[1])
except IndexError:
    print "Use: check_vat.py VAT"
    sys.exit(1)
except:
    sys.exit(2)
print "El DNI {} és {}".format(unicode(sys.argv[1]),
    "vàlid" if response['state'] else "invàlid")
