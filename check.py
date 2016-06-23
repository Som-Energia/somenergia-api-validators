#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from importlib import import_module
from check_exceptions import ErpException
from check_exceptions import ConnectionException

if __name__ == '__main__':
    try:
        codename=sys.argv[1]
        code = sys.argv[2]
        module=import_module('check_'+codename)
        methodToCall=getattr(module,'check_'+codename)
        state,msg=methodToCall(code)
        print msg
        output_code = 0 if state else 3
        sys.exit(output_code)
    except IndexError:
        print "Use check.py CODENAME CODE"
        sys.exit(1)
    except ErpException:
        print "ERP is not up"
        sys.exit(5)
    except ConnectionException:
        print "Connection error"
        sys.exit(2)
    except ImportError:
        print "Bad code name"
        sys.exit(4)
