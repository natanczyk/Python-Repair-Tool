import builtins
import importlib
import sys

def pytest_configure(config):
    sys.path.insert(0, r"D:\Master\MASTER_PROJECT\Data_QuixBugs\question_34\code\wrong")
    mod = importlib.import_module('wrong_shunting_yard')
    for name in dir(mod):
        if not name.startswith('_'):
            setattr(builtins, name, getattr(mod, name))
