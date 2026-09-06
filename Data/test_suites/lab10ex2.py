import os
import tempfile

def _write(content):
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8')
    f.write(content)
    f.close()
    return f.name

def test_case1():
    fname = _write("hello\n")
    try:
        result = conta_vogais(fname)
        assert result['e'] == 1
        assert result['o'] == 1
    finally:
        os.unlink(fname)

def test_case2():
    fname = _write("")
    try:
        result = conta_vogais(fname)
        assert result.get('a', 0) == 0
        assert result.get('e', 0) == 0
        assert result.get('i', 0) == 0
        assert result.get('o', 0) == 0
        assert result.get('u', 0) == 0
    finally:
        os.unlink(fname)

def test_case3():
    fname = _write("bcdfg\n")
    try:
        result = conta_vogais(fname)
        for v in 'aeiou':
            assert result.get(v, 0) == 0
    finally:
        os.unlink(fname)

def test_case4():
    fname = _write("aeiou\n")
    try:
        result = conta_vogais(fname)
        assert result['a'] == 1
        assert result['e'] == 1
        assert result['i'] == 1
        assert result['o'] == 1
        assert result['u'] == 1
    finally:
        os.unlink(fname)

def test_case5():
    fname = _write("banana\n")
    try:
        result = conta_vogais(fname)
        assert result['a'] == 3
        assert result.get('e', 0) == 0
    finally:
        os.unlink(fname)

def test_case6():
    fname = _write("HELLO\n")
    try:
        result = conta_vogais(fname)
        for v in 'aeiou':
            assert result.get(v, 0) == 0
    finally:
        os.unlink(fname)

def test_case7():
    fname = _write("Hello World\n")
    try:
        result = conta_vogais(fname)
        assert result['e'] == 1
        assert result['o'] == 2
        assert result.get('a', 0) == 0
    finally:
        os.unlink(fname)

def test_case8():
    fname = _write("aeiouaeiou\n")
    try:
        result = conta_vogais(fname)
        assert result['a'] == 2
        assert result['e'] == 2
        assert result['i'] == 2
        assert result['o'] == 2
        assert result['u'] == 2
    finally:
        os.unlink(fname)

def test_case9():
    fname = _write("line one\nline two\n")
    try:
        result = conta_vogais(fname)
        assert result['i'] == 2
        assert result['e'] == 2
        assert result['o'] == 2
    finally:
        os.unlink(fname)

def test_case10():
    fname = _write("python programming\n")
    try:
        result = conta_vogais(fname)
        assert result['o'] == 2
        assert result['a'] == 1
        assert result['i'] == 1
    finally:
        os.unlink(fname)

def test_case11():
    fname = _write("hello\n")
    try:
        result = conta_vogais(fname)
        assert isinstance(result, dict)
    finally:
        os.unlink(fname)

def test_case12():
    fname = _write("aaa\n")
    try:
        result = conta_vogais(fname)
        assert result['a'] == 3
    finally:
        os.unlink(fname)

def test_case13():
    fname = _write("uuuu\n")
    try:
        result = conta_vogais(fname)
        assert result['u'] == 4
    finally:
        os.unlink(fname)

def test_case14():
    fname = _write("first line\nsecond line\nthird line\n")
    try:
        result = conta_vogais(fname)
        assert result['i'] == 4
        assert result['e'] == 4
    finally:
        os.unlink(fname)

def test_case15():
    fname = _write("a aranha arranha a ra\n")
    try:
        result = conta_vogais(fname)
        assert result['a'] == 10
    finally:
        os.unlink(fname)

def test_case16():
    fname = _write("unique\n")
    try:
        result = conta_vogais(fname)
        assert result['u'] == 2
        assert result['i'] == 1
        assert result['e'] == 1
    finally:
        os.unlink(fname)

def test_case17():
    fname = _write("vowels: a e i o u\n")
    try:
        result = conta_vogais(fname)
        assert result['a'] == 1
        assert result['e'] == 2
        assert result['i'] == 1
        assert result['o'] == 1
        assert result['u'] == 1
    finally:
        os.unlink(fname)

def test_case18():
    fname = _write("xyz\n")
    try:
        result = conta_vogais(fname)
        for v in 'aeiou':
            assert result.get(v, 0) == 0
    finally:
        os.unlink(fname)

def test_case19():
    fname = _write("education\n")
    try:
        result = conta_vogais(fname)
        assert result['e'] == 1
        assert result['u'] == 1
        assert result['a'] == 1
        assert result['i'] == 1
        assert result['o'] == 1
    finally:
        os.unlink(fname)

def test_case20():
    fname = _write("one\ntwo\nthree\nfour\nfive\n")
    try:
        result = conta_vogais(fname)
        assert result['o'] == 2
        assert result['e'] == 4
        assert result['i'] == 1
        assert result['u'] == 1
    finally:
        os.unlink(fname)
