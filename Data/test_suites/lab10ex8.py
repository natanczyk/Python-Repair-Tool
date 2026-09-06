import os
import tempfile

def _write(content):
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='', encoding='utf-8')
    f.write(content)
    f.close()
    return f.name

def _read_lines(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f.readlines()]

def test_case1():
    fname = _write("Hello World\n")
    try:
        divide(fname, 5)
        lines0 = _read_lines(fname + '0')
        lines1 = _read_lines(fname + '1')
        non0 = [l for l in lines0 if l]
        non1 = [l for l in lines1 if l]
        assert non0[0] == 'Hello'
        assert non1[0] == ' World'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case2():
    fname = _write("abcde\nfghij\n")
    try:
        divide(fname, 3)
        lines0 = _read_lines(fname + '0')
        lines1 = _read_lines(fname + '1')
        non0 = [l for l in lines0 if l]
        non1 = [l for l in lines1 if l]
        assert non0[0] == 'abc'
        assert non1[0] == 'de'
        assert non0[1] == 'fgh'
        assert non1[1] == 'ij'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case3():
    fname = _write("python\njava\n")
    try:
        divide(fname, 2)
        lines0 = _read_lines(fname + '0')
        non0 = [l for l in lines0 if l]
        assert non0[0] == 'py'
        assert non0[1] == 'ja'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case4():
    fname = _write("python\njava\n")
    try:
        divide(fname, 2)
        lines1 = _read_lines(fname + '1')
        non1 = [l for l in lines1 if l]
        assert non1[0] == 'thon'
        assert non1[1] == 'va'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case5():
    fname = _write("abcde\n")
    try:
        divide(fname, 10)
        lines0 = _read_lines(fname + '0')
        non0 = [l for l in lines0 if l]
        assert non0[0] == 'abcde'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case6():
    fname = _write("12345\n")
    try:
        divide(fname, 0)
        lines0 = _read_lines(fname + '0')
        lines1 = _read_lines(fname + '1')
        non1 = [l for l in lines1 if l]
        assert non1[0] == '12345'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case7():
    fname = _write("one two three\nfour five six\n")
    try:
        divide(fname, 7)
        lines0 = _read_lines(fname + '0')
        non0 = [l for l in lines0 if l]
        assert non0[0] == 'one two'
        assert non0[1] == 'four fi'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case8():
    fname = _write("one two three\nfour five six\n")
    try:
        divide(fname, 7)
        lines1 = _read_lines(fname + '1')
        non1 = [l for l in lines1 if l]
        assert non1[0] == ' three'
        assert non1[1] == 've six'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case9():
    fname = _write("ABCDE\nFGHIJ\nKLMNO\n")
    try:
        divide(fname, 3)
        lines0 = _read_lines(fname + '0')
        non0 = [l for l in lines0 if l]
        assert len(non0) == 3
        assert all(len(l) == 3 for l in non0)
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case10():
    fname = _write("ABCDE\nFGHIJ\nKLMNO\n")
    try:
        divide(fname, 3)
        lines1 = _read_lines(fname + '1')
        non1 = [l for l in lines1 if l]
        assert len(non1) == 3
        assert all(len(l) == 2 for l in non1)
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case11():
    fname = _write("line one content\nline two content\n")
    try:
        divide(fname, 4)
        lines0 = _read_lines(fname + '0')
        non0 = [l for l in lines0 if l]
        assert non0[0] == 'line'
        assert non0[1] == 'line'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case12():
    fname = _write("abc\ndef\nghi\n")
    try:
        divide(fname, 1)
        lines0 = _read_lines(fname + '0')
        non0 = [l for l in lines0 if l]
        assert non0 == ['a', 'd', 'g']
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case13():
    fname = _write("abc\ndef\nghi\n")
    try:
        divide(fname, 1)
        lines1 = _read_lines(fname + '1')
        non1 = [l for l in lines1 if l]
        assert non1 == ['bc', 'ef', 'hi']
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case14():
    fname = _write("hello\nworld\n")
    try:
        divide(fname, 5)
        lines0 = _read_lines(fname + '0')
        non0 = [l for l in lines0 if l]
        assert non0[0] == 'hello'
        assert non0[1] == 'world'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case15():
    fname = _write("test\n")
    try:
        divide(fname, 2)
        lines0 = _read_lines(fname + '0')
        lines1 = _read_lines(fname + '1')
        non0 = [l for l in lines0 if l]
        non1 = [l for l in lines1 if l]
        assert non0[0] == 'te'
        assert non1[0] == 'st'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case16():
    fname = _write("aaa\nbbb\nccc\n")
    try:
        divide(fname, 2)
        lines0 = _read_lines(fname + '0')
        non0 = [l for l in lines0 if l]
        assert all(l == 'aa' or l == 'bb' or l == 'cc' for l in non0)
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case17():
    fname = _write("xyz\n")
    try:
        divide(fname, 3)
        lines0 = _read_lines(fname + '0')
        non0 = [l for l in lines0 if l]
        assert non0[0] == 'xyz'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case18():
    fname = _write("data123\ninfo456\n")
    try:
        divide(fname, 4)
        lines0 = _read_lines(fname + '0')
        lines1 = _read_lines(fname + '1')
        non0 = [l for l in lines0 if l]
        non1 = [l for l in lines1 if l]
        assert non0[0] == 'data'
        assert non1[0] == '123'
        assert non0[1] == 'info'
        assert non1[1] == '456'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case19():
    fname = _write("split here\n")
    try:
        divide(fname, 5)
        lines0 = _read_lines(fname + '0')
        lines1 = _read_lines(fname + '1')
        non0 = [l for l in lines0 if l]
        non1 = [l for l in lines1 if l]
        assert non0[0] == 'split'
        assert non1[0] == ' here'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass

def test_case20():
    fname = _write("row1col\nrow2col\nrow3col\n")
    try:
        divide(fname, 4)
        lines0 = _read_lines(fname + '0')
        non0 = [l for l in lines0 if l]
        assert non0[0] == 'row1'
        assert non0[1] == 'row2'
        assert non0[2] == 'row3'
    finally:
        os.unlink(fname)
        for s in ['0', '1']:
            try:
                os.unlink(fname + s)
            except:
                pass
