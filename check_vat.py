#! /usr/bin/env python
# -*- coding: utf-8 -*-
from requests import Session
import sys
session = Session()
try:
  vat = sys.argv[1]
except:
  print "Use: check_vat.py VAT"
  sys.exit(1)
api = 'https://api.somenergia.coop/check/vat/'
response = session.get(api+vat)
responseJson= response.json()
print "El DNI {} és {}".format(vat, 
    "vàlid" if responseJson['state'] else "invàlid")
