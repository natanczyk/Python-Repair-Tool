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
    f_in = _write("Hello World")
    f_out = _write("")
    try:
        corta(f_in, f_out, 5)
        content = _read(f_out)
        assert content == "Hello"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case2():
    f_in = _write("Hello")
    f_out = _write("")
    try:
        corta(f_in, f_out, 100)
        content = _read(f_out)
        assert 'Hello' in content
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case3():
    f_in = _write("Hello")
    f_out = _write("")
    try:
        corta(f_in, f_out, 5)
        content = _read(f_out)
        assert 'Hello' in content
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case4():
    f_in = _write("abcdefghij")
    f_out = _write("")
    try:
        corta(f_in, f_out, 3)
        content = _read(f_out)
        assert content == "abc"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case5():
    f_in = _write("abcdefghij")
    f_out = _write("")
    try:
        corta(f_in, f_out, 0)
        content = _read(f_out)
        assert content == ""
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case6():
    f_in = _write("1234567890")
    f_out = _write("")
    try:
        corta(f_in, f_out, 7)
        content = _read(f_out)
        assert content == "1234567"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case7():
    f_in = _write("short")
    f_out = _write("")
    try:
        corta(f_in, f_out, 1000)
        content = _read(f_out)
        assert 'short' in content
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case8():
    f_in = _write("python")
    f_out = _write("")
    try:
        corta(f_in, f_out, 6)
        content = _read(f_out)
        assert 'python' in content
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case9():
    f_in = _write("abcde")
    f_out = _write("")
    try:
        corta(f_in, f_out, 2)
        content = _read(f_out)
        assert content == "ab"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case10():
    f_in = _write("Hello World")
    f_out = _write("")
    try:
        corta(f_in, f_out, 11)
        content = _read(f_out)
        assert 'Hello World' in content
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case11():
    f_in = _write("Hello World")
    f_out = _write("")
    try:
        corta(f_in, f_out, 4)
        content = _read(f_out)
        assert content == "Hell"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case12():
    f_in = _write("data")
    f_out = _write("")
    try:
        corta(f_in, f_out, 4)
        content = _read(f_out)
        assert 'data' in content
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case13():
    f_in = _write("0123456789")
    f_out = _write("")
    try:
        corta(f_in, f_out, 1)
        content = _read(f_out)
        assert content == "0"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case14():
    f_in = _write("test content here")
    f_out = _write("")
    try:
        corta(f_in, f_out, 4)
        content = _read(f_out)
        assert content == "test"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case15():
    f_in = _write("longer text than n")
    f_out = _write("")
    try:
        corta(f_in, f_out, 6)
        content = _read(f_out)
        assert content == "longer"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case16():
    f_in = _write("abc")
    f_out = _write("")
    try:
        corta(f_in, f_out, 50)
        content = _read(f_out)
        assert 'abc' in content
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case17():
    f_in = _write("programming")
    f_out = _write("")
    try:
        corta(f_in, f_out, 7)
        content = _read(f_out)
        assert content == "program"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case18():
    f_in = _write("exactly ten!")
    f_out = _write("")
    try:
        corta(f_in, f_out, 10)
        content = _read(f_out)
        assert content == "exactly te"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case19():
    f_in = _write("hello")
    f_out = _write("old content")
    try:
        corta(f_in, f_out, 3)
        content = _read(f_out)
        assert content == "hel"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)

def test_case20():
    f_in = _write("ABCDE")
    f_out = _write("")
    try:
        corta(f_in, f_out, 3)
        content = _read(f_out)
        assert content == "ABC"
    finally:
        os.unlink(f_in)
        os.unlink(f_out)
