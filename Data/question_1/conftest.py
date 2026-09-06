import builtins
import importlib
import sys

def pytest_configure(config):
    sys.path.insert(0, r"D:\Master\MASTER_PROJECT\test_notebooks\test_results\fauxpy_tmp")
    mod = importlib.import_module('wrong_1_001')
    for name in dir(mod):
        if not name.startswith('_'):
            setattr(builtins, name, getattr(mod, name))
