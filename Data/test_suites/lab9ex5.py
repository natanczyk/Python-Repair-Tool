import pytest

def test_case1():
    d = {
        'Maria': ('F', 34, 1.65, 64),
        'Pedro': ('M', 34, 1.65, 64),
        'Ana': ('F', 54, 1.65, 120),
        'Hugo': ('M', 12, 1.82, 75)
    }
    result = metabolismo(d)
    assert result['Maria'] == pytest.approx(1097.755)
    assert result['Pedro'] == pytest.approx(721.685)
    assert result['Ana'] == pytest.approx(1432.555)
    assert result['Hugo'] == pytest.approx(643.578)

def test_case2():
    d = {'John': ('M', 25, 1.80, 70)}
    result = metabolismo(d)
    expected = 66 + 6.3 * 70 + 12.9 * 1.80 + 6.8 * 25
    assert result['John'] == pytest.approx(expected)

def test_case3():
    d = {'Emma': ('F', 30, 1.70, 60)}
    result = metabolismo(d)
    expected = 655 + 4.3 * 60 + 4.7 * 1.70 + 4.7 * 30
    assert result['Emma'] == pytest.approx(expected)

def test_case4():
    d = {'Maria': ('F', 34, 1.65, 64)}
    result = metabolismo(d)
    assert result['Maria'] == pytest.approx(1097.755)

def test_case5():
    d = {'Pedro': ('M', 34, 1.65, 64)}
    result = metabolismo(d)
    assert result['Pedro'] == pytest.approx(721.685)

def test_case6():
    d = {'A': ('M', 20, 1.75, 70)}
    result = metabolismo(d)
    expected = 66 + 6.3 * 70 + 12.9 * 1.75 + 6.8 * 20
    assert result['A'] == pytest.approx(expected)

def test_case7():
    d = {'B': ('F', 20, 1.75, 70)}
    result = metabolismo(d)
    expected = 655 + 4.3 * 70 + 4.7 * 1.75 + 4.7 * 20
    assert result['B'] == pytest.approx(expected)

def test_case8():
    d = {'Hugo': ('M', 12, 1.82, 75)}
    result = metabolismo(d)
    assert result['Hugo'] == pytest.approx(643.578)

def test_case9():
    d = {'P1': ('M', 40, 1.90, 90), 'P2': ('F', 40, 1.90, 90)}
    result = metabolismo(d)
    assert result['P1'] != pytest.approx(result['P2'])

def test_case10():
    d = {'A': ('F', 34, 1.65, 64)}
    result = metabolismo(d)
    assert isinstance(result, dict)

def test_case11():
    d = {'A': ('M', 34, 1.65, 64), 'B': ('F', 34, 1.65, 64)}
    result = metabolismo(d)
    assert set(result.keys()) == {'A', 'B'}

def test_case12():
    d = {'C': ('M', 50, 1.70, 80)}
    result = metabolismo(d)
    expected = 66 + 6.3 * 80 + 12.9 * 1.70 + 6.8 * 50
    assert result['C'] == pytest.approx(expected)

def test_case13():
    d = {'D': ('F', 50, 1.70, 80)}
    result = metabolismo(d)
    expected = 655 + 4.3 * 80 + 4.7 * 1.70 + 4.7 * 50
    assert result['D'] == pytest.approx(expected)

def test_case14():
    d = {'Ana': ('F', 54, 1.65, 120)}
    result = metabolismo(d)
    assert result['Ana'] == pytest.approx(1432.555)

def test_case15():
    d = {'E': ('M', 30, 2.00, 100)}
    result = metabolismo(d)
    expected = 66 + 6.3 * 100 + 12.9 * 2.00 + 6.8 * 30
    assert result['E'] == pytest.approx(expected)

def test_case16():
    d = {'F': ('F', 25, 1.60, 55)}
    result = metabolismo(d)
    expected = 655 + 4.3 * 55 + 4.7 * 1.60 + 4.7 * 25
    assert result['F'] == pytest.approx(expected)

def test_case17():
    d = {}
    result = metabolismo(d)
    assert result == {}

def test_case18():
    d = {'G': ('M', 1, 0.50, 5)}
    result = metabolismo(d)
    expected = 66 + 6.3 * 5 + 12.9 * 0.50 + 6.8 * 1
    assert result['G'] == pytest.approx(expected)

def test_case19():
    d = {'H': ('M', 34, 1.65, 64)}
    result = metabolismo(d)
    assert result['H'] > 0

def test_case20():
    d = {'I': ('F', 34, 1.65, 64)}
    result = metabolismo(d)
    assert result['I'] > 0
