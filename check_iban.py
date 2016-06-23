# -*- coding: utf-8 -*-
from check_code import check_code
def check_iban(iban):
    response = check_code('/check/iban',iban)
    msg = u"El IBAN {} és {}".format(iban.decode('utf-8'),
        u"vàlid" if response['state'] else u"invàlid",
    ).encode('utf-8')
    return state,msg
