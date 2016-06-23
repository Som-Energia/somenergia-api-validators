# -*- coding: utf-8 -*-
from check_code import check_code
def check_cups(cups):
    response = check_code('/check/cups/',cups)
    msg=u"El CUPS {} és {}".format(cups.decode('utf-8'), 
        u"invàlid, reason: {}".format(
            response['data']['invalid_fields'][0]['error']) 
        if not response['state'] else u"vàlid",
    ).encode('utf-8')
    state =response['state']
    return state,msg
