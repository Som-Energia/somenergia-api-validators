#! /usr/bin/env python
# -*- coding: utf-8 -*-
from requests import Session
from check_code import check_code
import sys
try:
    response = check_code('/check/iban/',sys.argv[1])
except IndexError:
    print "Use: check_iban.py IBAN"
    sys.exit(1)
except:
    sys.exit(2)
print u"El IBAN {} és {}".format(sys.argv[1].decode('utf-8'),
    u"vàlid" if response['state'] else u"invàlid",
).encode('utf-8')
if not response['state']:
    sys.exit(3)
