#! /usr/bin/env python
# -*- coding: utf-8 -*-
from requests import Session
from check_code import check_code
import sys
try:
    response = check_code('/check/cups/',sys.argv[1])
except IndexError:
    print "Use: check_cups.py CNAE"
    sys.exit(1)
except:
    sys.exit(2)
print u"El CUPS {} és {}".format(unicode(sys.argv[1]), 
    u"invàlid, reason: {}".format(
        response['data']['invalid_fields'][0]['error']) 
    if not response['state'] else u"vàlid",
    )
