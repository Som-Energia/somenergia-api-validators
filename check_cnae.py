#! /usr/bin/env python
# -*- coding: utf-8 -*-
from requests import Session
from check_code import check_code
import sys
session = Session()
try:
    response = check_code('/check/cnae/',sys.argv[1])
except IndexError:
    print "Use: check_cnae.py CNAE"
    sys.exit(1)
except:
    sys.exit(2)
print u"El CNAE {} és {}".format(unicode(sys.argv[1]), 
    u"vàlid i és per {}".format(
        response['data']['description']) if response['state'] else u"invàlid",
    )
