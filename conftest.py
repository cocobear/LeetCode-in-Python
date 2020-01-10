import inspect
import os
import pytest

rootdir = os.path.dirname(__file__)


def pytest_pycollect_makeitem(collector, name, obj):
    if (inspect.isclass(obj) and obj.__name__ == 'Solution' and
            hasattr(obj, 'tests')):
        # can not be ismethod , don't know why
        func, _ = inspect.getmembers(obj, inspect.isfunction)[0]

        cases = obj.tests
        if not cases:
            return

        # Split into (args, expected)
        cases = [(c[:-1], c[-1]) for c in cases]

        @pytest.mark.parametrize(['args', 'expected'], cases)
        def test(args, expected):
            assert getattr(obj(), func)(*args) == expected

        return list(collector._genfunctions('test_' + obj.__module__, test))
