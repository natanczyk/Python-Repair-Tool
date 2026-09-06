import os
import tempfile

def _write(content):
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8')
    f.write(content)
    f.close()
    return f.name

def test_case1():
    fname = _write("Hello\nWorld\n")
    try:
        assert conta_linhas(fname) == 2
    finally:
        os.unlink(fname)

def test_case2():
    fname = _write("Line 1\nLine 2\nLine 3\n")
    try:
        assert conta_linhas(fname) == 3
    finally:
        os.unlink(fname)

def test_case3():
    fname = _write("")
    try:
        assert conta_linhas(fname) == 0
    finally:
        os.unlink(fname)

def test_case4():
    fname = _write("\n")
    try:
        assert conta_linhas(fname) == 0
    finally:
        os.unlink(fname)

def test_case5():
    fname = _write("\n\n\n")
    try:
        assert conta_linhas(fname) == 0
    finally:
        os.unlink(fname)

def test_case6():
    fname = _write("Hello\n\nWorld\n")
    try:
        assert conta_linhas(fname) == 2
    finally:
        os.unlink(fname)

def test_case7():
    fname = _write("\nHello\n\nWorld\n\n")
    try:
        assert conta_linhas(fname) == 2
    finally:
        os.unlink(fname)

def test_case8():
    fname = _write("Hello")
    try:
        assert conta_linhas(fname) == 1
    finally:
        os.unlink(fname)

def test_case9():
    fname = _write("a\nb\nc\nd\ne\n")
    try:
        assert conta_linhas(fname) == 5
    finally:
        os.unlink(fname)

def test_case10():
    fname = _write("Line 1\n\nLine 3\n\nLine 5\n")
    try:
        assert conta_linhas(fname) == 3
    finally:
        os.unlink(fname)

def test_case11():
    fname = _write(" \n")
    try:
        assert conta_linhas(fname) == 1
    finally:
        os.unlink(fname)

def test_case12():
    fname = _write("Hello\nWorld")
    try:
        assert conta_linhas(fname) == 2
    finally:
        os.unlink(fname)

def test_case13():
    fname = _write("a\n\n\nb\n\n\nc\n")
    try:
        assert conta_linhas(fname) == 3
    finally:
        os.unlink(fname)

def test_case14():
    fname = _write("x\n" * 10)
    try:
        assert conta_linhas(fname) == 10
    finally:
        os.unlink(fname)

def test_case15():
    fname = _write("Hello\nWorld\n")
    try:
        result = conta_linhas(fname)
        assert isinstance(result, int)
    finally:
        os.unlink(fname)

def test_case16():
    fname = _write("\n\nHello\n\n")
    try:
        assert conta_linhas(fname) == 1
    finally:
        os.unlink(fname)

def test_case17():
    fname = _write("line1\nline2\nline3\nline4\nline5\n")
    try:
        assert conta_linhas(fname) == 5
    finally:
        os.unlink(fname)

def test_case18():
    fname = _write("A\n\nB\n\nC\n\nD\n")
    try:
        assert conta_linhas(fname) == 4
    finally:
        os.unlink(fname)

def test_case19():
    fname = _write("only one line")
    try:
        assert conta_linhas(fname) == 1
    finally:
        os.unlink(fname)

def test_case20():
    fname = _write("\n\n\n\n\ncontent\n\n\nmore\n")
    try:
        assert conta_linhas(fname) == 2
    finally:
        os.unlink(fname)
