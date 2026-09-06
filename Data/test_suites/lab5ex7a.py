import pytest

def test_case1():
    assert valor(100, 0.03, 4) == pytest.approx(100 * 1.03 ** 4)

def test_case2():
    assert valor(100, 0.05, 1) == pytest.approx(105.0)

def test_case3():
    assert valor(100, 0.10, 1) == pytest.approx(110.0)

def test_case4():
    assert valor(200, 0.10, 1) == pytest.approx(220.0)

def test_case5():
    assert valor(100, 0.10, 2) == pytest.approx(121.0)

def test_case6():
    assert valor(100, 0.25, 1) == pytest.approx(125.0)

def test_case7():
    assert valor(400, 0.25, 2) == pytest.approx(625.0)

def test_case8():
    assert valor(1000, 0.05, 3) == pytest.approx(1000 * 1.05 ** 3)

def test_case9():
    assert valor(500, 0.08, 5) == pytest.approx(500 * 1.08 ** 5)

def test_case10():
    assert valor(100, 0.03, 10) == pytest.approx(100 * 1.03 ** 10)

def test_case11():
    assert valor(1, 0.5, 1) == pytest.approx(1.5)

def test_case12():
    assert valor(100, 0.01, 1) == pytest.approx(101.0)

def test_case13():
    assert valor(200, 0.5, 2) == pytest.approx(200 * 1.5 ** 2)

def test_case14():
    with pytest.raises((ValueError, TypeError)):
        valor(0, 0.03, 4)

def test_case15():
    with pytest.raises((ValueError, TypeError)):
        valor(-100, 0.03, 4)

def test_case16():
    with pytest.raises((ValueError, TypeError)):
        valor(100, 0, 4)

def test_case17():
    with pytest.raises((ValueError, TypeError)):
        valor(100, 1, 4)

def test_case18():
    with pytest.raises((ValueError, TypeError)):
        valor(100, 1.5, 4)

def test_case19():
    with pytest.raises((ValueError, TypeError)):
        valor(100, 0.03, 0)

def test_case20():
    with pytest.raises((ValueError, TypeError)):
        valor(100, 0.03, -1)
