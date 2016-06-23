# -*- coding: utf-8 -*-
from check_code import check_code
def check_vat(vat):
    response = check_code('/check/vat/', vat)
    msg=u"El DNI {} és {}".format(vat.decode('utf-8'),
        u"vàlid" if response['state'] else u"invàlid").encode('utf-8')
    state = response['state']
    return state,msg
