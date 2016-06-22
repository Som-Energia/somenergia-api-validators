#! /usr/bin/env python
# -*- coding: utf-8 -*-
from requests import Session
API_BASE_URL='https://api.somenergia.coop'
def check_code(url,code):
    session = Session()
    try:
        response = session.get(API_BASE_URL+url+code)
        response.raise_for_status()
    except:
        print "Connection error"
        raise
    responseJson= response.json()
    if responseJson['status'] != 'ONLINE':
        print 'ERP is not up'
        raise
    return True if responseJson['state'] else False
