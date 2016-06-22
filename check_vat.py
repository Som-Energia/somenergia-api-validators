#! /usr/bin/env python
# -*- coding: utf-8 -*-
from requests import Session
import json
import sys
session = Session()
try:
  vat = sys.argv[1]
except:
  print "Use: check_vat.py VAT"
  sys.exit(1)
api = 'https://api.somenergia.coop/check/vat/'
response = session.get(api+vat)
responseJson = json.loads(response.text)
print "El DNI {} és {}".format(vat, 
    "valid" if responseJson['state'] else "invalid")
