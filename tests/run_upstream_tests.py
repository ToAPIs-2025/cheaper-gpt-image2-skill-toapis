"""Run original offline tests with one trusted SSL context created before env clearing.

SDK 3 on Windows needs a system context even when an upstream fixture clears
all environment variables. No verification is disabled and no live HTTP is sent.
"""
from pathlib import Path
import argparse,sys,ssl,unittest
from unittest.mock import patch
p=argparse.ArgumentParser();p.add_argument('--upstream',type=Path,required=True);a=p.parse_args();sys.path.insert(0,str(a.upstream.resolve()/'src'))
import openai
context=ssl.create_default_context()
target='httpx2._transports.default.create_ssl_context' if int(openai.__version__.split('.')[0])>=3 else 'httpx._transports.default.create_ssl_context'
with patch(target,return_value=context):
    tests=unittest.defaultTestLoader.discover(str(a.upstream/'tests'));result=unittest.TextTestRunner(verbosity=2).run(tests)
raise SystemExit(0 if result.wasSuccessful() else 1)
