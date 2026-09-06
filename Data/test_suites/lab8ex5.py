def test_case1(capsys):
    escreve_matriz([[1]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert len(lines) == 1
    assert '1' in lines[0]

def test_case2(capsys):
    escreve_matriz([[1, 2], [3, 4]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert len(lines) == 2
    assert '1' in lines[0] and '2' in lines[0]
    assert '3' in lines[1] and '4' in lines[1]

def test_case3(capsys):
    escreve_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert len(lines) == 3

def test_case4(capsys):
    escreve_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert '1' in lines[0] and '2' in lines[0] and '3' in lines[0]

def test_case5(capsys):
    escreve_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert '4' in lines[1] and '5' in lines[1] and '6' in lines[1]

def test_case6(capsys):
    escreve_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert '7' in lines[2] and '8' in lines[2] and '9' in lines[2]

def test_case7(capsys):
    escreve_matriz([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert len(lines) == 3
    assert '2' in lines[0] and '4' in lines[0] and '6' in lines[0]

def test_case8(capsys):
    escreve_matriz([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert '8' in lines[1] and '10' in lines[1] and '12' in lines[1]

def test_case9(capsys):
    escreve_matriz([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert '14' in lines[2] and '16' in lines[2] and '18' in lines[2]

def test_case10(capsys):
    escreve_matriz([[10, 20], [30, 40], [50, 60]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert len(lines) == 3

def test_case11(capsys):
    escreve_matriz([[10, 20], [30, 40], [50, 60]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert '10' in lines[0] and '20' in lines[0]

def test_case12(capsys):
    escreve_matriz([[10, 20], [30, 40], [50, 60]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert '50' in lines[2] and '60' in lines[2]

def test_case13(capsys):
    escreve_matriz([[0, 0], [0, 0]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert len(lines) == 2

def test_case14(capsys):
    escreve_matriz([[-1, -2], [-3, -4]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert '-1' in lines[0] and '-2' in lines[0]

def test_case15(capsys):
    escreve_matriz([[-1, -2], [-3, -4]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert '-3' in lines[1] and '-4' in lines[1]

def test_case16(capsys):
    escreve_matriz([[100]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert len(lines) == 1
    assert '100' in lines[0]

def test_case17(capsys):
    escreve_matriz([[1, 2, 3, 4]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert len(lines) == 1
    assert '1' in lines[0] and '4' in lines[0]

def test_case18(capsys):
    escreve_matriz([[1], [2], [3]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert len(lines) == 3
    assert '1' in lines[0]
    assert '2' in lines[1]
    assert '3' in lines[2]

def test_case19(capsys):
    escreve_matriz([[5, 0], [0, 5]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert len(lines) == 2
    assert '5' in lines[0]

def test_case20(capsys):
    escreve_matriz([[1, 2, 3], [4, 5, 6]])
    out = capsys.readouterr().out
    lines = out.strip().split('\n')
    assert len(lines) == 2
    assert '1' in lines[0] and '3' in lines[0]
    assert '4' in lines[1] and '6' in lines[1]
