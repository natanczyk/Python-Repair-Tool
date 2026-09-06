import os
import tempfile

def _write(content):
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8')
    f.write(content)
    f.close()
    return f.name

def _read(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        return f.read()

def test_case1():
    f1 = _write("File 1 line 1\nFile 1 line 2\n")
    f2 = _write("File 2 line 1\nFile 2 line 2\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        content = _read(fout)
        assert 'File 1 line 1' in content
        assert 'File 2 line 1' in content
        lines = content.splitlines()
        assert lines.index('File 1 line 1') < lines.index('File 2 line 1')
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case2():
    f1 = _write("aaa\n")
    fout = _write("")
    try:
        concatena([f1], fout)
        content = _read(fout)
        assert 'aaa' in content
    finally:
        os.unlink(f1)
        os.unlink(fout)

def test_case3():
    f1 = _write("A\nB\n")
    f2 = _write("C\nD\n")
    f3 = _write("E\nF\n")
    fout = _write("")
    try:
        concatena([f1, f2, f3], fout)
        lines = _read(fout).splitlines()
        assert lines[0] == 'A'
        assert lines[2] == 'C'
        assert lines[4] == 'E'
    finally:
        for f in [f1, f2, f3, fout]:
            os.unlink(f)

def test_case4():
    f1 = _write("hello\n")
    f2 = _write("world\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        content = _read(fout)
        assert 'hello' in content
        assert 'world' in content
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case5():
    f1 = _write("line1\nline2\n")
    f2 = _write("line3\nline4\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        lines = _read(fout).splitlines()
        non_empty = [l for l in lines if l]
        assert len(non_empty) == 4
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case6():
    f1 = _write("1\n2\n3\n")
    f2 = _write("4\n5\n6\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        lines = _read(fout).splitlines()
        non_empty = [l for l in lines if l]
        assert non_empty == ['1', '2', '3', '4', '5', '6']
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case7():
    f1 = _write("part one\n")
    f2 = _write("part two\n")
    f3 = _write("part three\n")
    fout = _write("")
    try:
        concatena([f1, f2, f3], fout)
        content = _read(fout)
        assert 'part one' in content
        assert 'part two' in content
        assert 'part three' in content
    finally:
        for f in [f1, f2, f3, fout]:
            os.unlink(f)

def test_case8():
    f1 = _write("alpha\nbeta\n")
    f2 = _write("gamma\ndelta\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        lines = _read(fout).splitlines()
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'alpha'
        assert non_empty[3] == 'delta'
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case9():
    f1 = _write("x")
    f2 = _write("y")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        content = _read(fout)
        assert 'x' in content
        assert 'y' in content
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case10():
    f1 = _write("first file content\n")
    f2 = _write("second file content\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        content = _read(fout)
        pos1 = content.index('first')
        pos2 = content.index('second')
        assert pos1 < pos2
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case11():
    f1 = _write("A\nB\nC\n")
    f2 = _write("D\nE\nF\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        content = _read(fout)
        for ch in 'ABCDEF':
            assert ch in content
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case12():
    f1 = _write("row1\nrow2\n")
    f2 = _write("row3\nrow4\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        lines = _read(fout).splitlines()
        non_empty = [l for l in lines if l]
        assert non_empty[1] == 'row2'
        assert non_empty[2] == 'row3'
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case13():
    f1 = _write("single line\n")
    f2 = _write("another line\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        lines = _read(fout).splitlines()
        non_empty = [l for l in lines if l]
        assert len(non_empty) == 2
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case14():
    f1 = _write("p\nq\nr\n")
    f2 = _write("s\nt\nu\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        lines = _read(fout).splitlines()
        non_empty = [l for l in lines if l]
        assert non_empty == ['p', 'q', 'r', 's', 't', 'u']
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case15():
    f1 = _write("one\n")
    f2 = _write("two\n")
    f3 = _write("three\n")
    f4 = _write("four\n")
    fout = _write("")
    try:
        concatena([f1, f2, f3, f4], fout)
        lines = _read(fout).splitlines()
        non_empty = [l for l in lines if l]
        assert non_empty == ['one', 'two', 'three', 'four']
    finally:
        for f in [f1, f2, f3, f4, fout]:
            os.unlink(f)

def test_case16():
    f1 = _write("line a\nline b\n")
    f2 = _write("line c\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        lines = _read(fout).splitlines()
        non_empty = [l for l in lines if l]
        assert len(non_empty) == 3
        assert non_empty[2] == 'line c'
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case17():
    f1 = _write("cat\ndog\n")
    f2 = _write("bird\nfish\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        lines = _read(fout).splitlines()
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'cat'
        assert non_empty[3] == 'fish'
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case18():
    f1 = _write("start\n")
    f2 = _write("middle\n")
    f3 = _write("end\n")
    fout = _write("")
    try:
        concatena([f1, f2, f3], fout)
        lines = _read(fout).splitlines()
        non_empty = [l for l in lines if l]
        assert non_empty[0] == 'start'
        assert non_empty[1] == 'middle'
        assert non_empty[2] == 'end'
    finally:
        for f in [f1, f2, f3, fout]:
            os.unlink(f)

def test_case19():
    f1 = _write("content of file 1\n")
    f2 = _write("content of file 2\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        content = _read(fout)
        assert content.index('file 1') < content.index('file 2')
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)

def test_case20():
    f1 = _write("aa\nbb\ncc\n")
    f2 = _write("dd\nee\nff\n")
    fout = _write("")
    try:
        concatena([f1, f2], fout)
        lines = _read(fout).splitlines()
        non_empty = [l for l in lines if l]
        assert len(non_empty) == 6
        assert 'bb' in non_empty
        assert 'ee' in non_empty
    finally:
        for f in [f1, f2, fout]:
            os.unlink(f)
