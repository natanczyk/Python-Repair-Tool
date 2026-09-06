import os
import tempfile

def _write(content):
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8')
    f.write(content)
    f.close()
    return f.name

def _read_lines(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f.readlines()]

def test_case1():
    f1 = _write("Line 1\nLine 2\nLine 3\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        assert lines[0] == 'Line 3'
        assert lines[1] == 'Line 2'
        assert lines[2] == 'Line 1'
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case2():
    f1 = _write("a\nb\nc\nd\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        assert lines[0] == 'd'
        assert lines[-1] == 'a'
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case3():
    f1 = _write("only line\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        assert any('only line' in l for l in lines)
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case4():
    f1 = _write("first\nsecond\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        assert lines[0] == 'second'
        assert lines[1] == 'first'
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case5():
    f1 = _write("A\nB\nC\nD\nE\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'E'
        assert non_empty[-1] == 'A'
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case6():
    f1 = _write("Line 1\nLine 2\nLine 3\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert len(non_empty) == 3
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case7():
    f1 = _write("1\n2\n3\n4\n5\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty == ['5', '4', '3', '2', '1']
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case8():
    f1 = _write("hello world\ngoodbye world\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'goodbye world'
        assert non_empty[1] == 'hello world'
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case9():
    f1 = _write("alpha\nbeta\ngamma\ndelta\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'delta'
        assert non_empty[1] == 'gamma'
        assert non_empty[2] == 'beta'
        assert non_empty[3] == 'alpha'
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case10():
    f1 = _write("X\nY\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        content = open(f2, 'r', encoding='utf-8').read()
        os.unlink(f2)
        f2 = None
        assert 'Y' in content
        assert 'X' in content
    finally:
        os.unlink(f1)
        if f2:
            try:
                os.unlink(f2)
            except:
                pass

def test_case11():
    f1 = _write("Line 1\nLine 2\nLine 3\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        original = _read_lines(f1)
        reversed_lines = _read_lines(f2)
        non_empty_orig = [l for l in original if l]
        non_empty_rev = [l for l in reversed_lines if l]
        assert non_empty_rev == list(reversed(non_empty_orig))
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case12():
    f1 = _write("one\ntwo\nthree\nfour\nfive\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'five'
        assert non_empty[4] == 'one'
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case13():
    f1 = _write("row1\nrow2\nrow3\n")
    f2 = _write("original content\n")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert 'row1' not in non_empty[0]
        assert 'row3' in non_empty[0]
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case14():
    f1 = _write("p\nq\nr\ns\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty == ['s', 'r', 'q', 'p']
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case15():
    f1 = _write("first line\nsecond line\nthird line\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'third line'
        assert non_empty[2] == 'first line'
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case16():
    content = "".join(f"line {i}\n" for i in range(1, 7))
    f1 = _write(content)
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'line 6'
        assert non_empty[5] == 'line 1'
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case17():
    f1 = _write("abc\ndef\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'def'
        assert non_empty[1] == 'abc'
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case18():
    f1 = _write("z\ny\nx\nw\nv\nu\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'u'
        assert non_empty[5] == 'z'
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case19():
    f1 = _write("cat\ndog\nbird\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty == ['bird', 'dog', 'cat']
    finally:
        os.unlink(f1)
        os.unlink(f2)

def test_case20():
    f1 = _write("start\nmiddle\nend\n")
    f2 = _write("")
    try:
        inverte(f1, f2)
        lines = _read_lines(f2)
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'end'
        assert non_empty[1] == 'middle'
        assert non_empty[2] == 'start'
    finally:
        os.unlink(f1)
        os.unlink(f2)
