# -*- coding: utf-8 -*-
from check_code import check_code
def check_cnae(cnae):
    response=check_code('/check/cnae/',cnae)
    msg=u"El CNAE {} és {}".format(cnae.decode('utf-8'), 
        u"vàlid i és per {}".format(
            response['data']['description']) if response['state'] else u"invàlid",
    ).encode('utf-8')
    state = response['state']
    return state,msg
