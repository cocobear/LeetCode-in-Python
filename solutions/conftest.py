import inspect
import os
import pytest

rootdir = os.path.dirname(__file__)


def pytest_pycollect_makeitem(collector, name, obj):
    if (inspect.isclass(obj) and obj.__name__ == 'Solution' and
            hasattr(obj, 'tests')):
        # can not be ismethod , don't know why
        funcs = inspect.getmembers(obj, inspect.isfunction)
        cases = obj.tests
        if not cases:
            return
        funcs = [f[0] for f in funcs]
        # Split into (args, expected)
        cases = [(c[:-1], c[-1]) for c in cases]

        # @pytest.mark.parametrize('func', funcs)
        # @pytest.mark.parametrize(['args', 'expected'], cases)
        # def test(func, args, expected):
        #     assert getattr(obj(), func)(*args) == expected

        # return list(collector._genfunctions('test_' + obj.__module__, test))
        test_list = []
        for func in funcs:
            @pytest.mark.parametrize(['args', 'expected'], cases)
            def test(args, expected):
                assert getattr(obj(), func)(*args) == expected

            test_list.extend(list(collector._genfunctions('test_' + func, test)))

        return test_list
