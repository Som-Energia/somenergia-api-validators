#! /usr/bin/env python
# -*- coding: utf-8 -*-
from requests import Session
import sys
session = Session()
try:
    vat = sys.argv[1]
except IndexError:
    print "Use: check_vat.py VAT"
    sys.exit(1)
api = 'https://api.somenergia.coop/check/vat/'
try:
    response = session.get(api+vat)
    response.raise_for_status()
except:
    print "Connection error"
    sys.exit(2)
        
responseJson= response.json()
if responseJson['status'] != 'ONLINE':
    print 'ERP is not up'
    sys.exit(3)
print "El DNI {} és {}".format(vat, 
    "vàlid" if responseJson['state'] else "invàlid")
