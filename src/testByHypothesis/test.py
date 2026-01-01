from hypothesis import given, strategies as st, settings, Verbosity, Phase
import importlib.util

spec = importlib.util.spec_from_file_location("mysort", "../testCode/mysort.py")
mysort = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mysort)

#没有用例约减的代码(打印详细信息)
@given(st.lists(st.integers()))
@settings(verbosity=Verbosity.verbose,phases=[Phase.explain,Phase.reuse,Phase.generate,Phase.target,Phase.explain])
def test_matches_builtin_noShrink(ls):
    result = mysort.errorSort2(ls)
    expected = sorted(ls)
    assert expected == result

@settings(verbosity=Verbosity.verbose,phases=[Phase.explain,Phase.reuse,Phase.generate,Phase.target,Phase.explain])
@given(st.integers())
def test_num_lt_zero_noShrink(num):
    assert num <50


#有用例约减的代码（打印详细信息）
@settings(verbosity=Verbosity.verbose)
@given(st.integers())
def test_num_lt_zero(num):
    assert num <50


@settings(verbosity=Verbosity.verbose)
@given(st.lists(st.integers(min_value=0, max_value=100)))
def test_list_sum(ls):
    if(sum(ls) > 100 and len(ls)>=2):
        assert len(ls)>=3

@given(st.lists(st.integers()))
@settings(verbosity=Verbosity.verbose)
def test_matches_builtin(ls):
    result = mysort.errorSort(ls)
    expected = sorted(ls)
    assert expected == result


test_num_lt_zero()


