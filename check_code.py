#! /usr/bin/env python
# -*- coding: utf-8 -*-
from requests import Session
from check_exceptions import ConnectionException,ErpException
API_BASE_URL='https://api.somenergia.coop'
API_BASE_URL_TESTING='https://testing.somenergia.coop:5001'
#API_BASE_URL=API_BASE_URL_TESTING
def check_code(url,code):
    session = Session()
    try:
        response = session.get(API_BASE_URL+url+code)
        response.raise_for_status()
        response = response.json()
    except:
        raise ConnectionException("")
    if response['status'] != 'ONLINE':
        raise ErpException("")
    return response
