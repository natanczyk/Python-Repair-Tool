def test_case001():
    assert longest_common_subsequence('headache', 'pentadactyl') == 'eadac'

def test_case002():
    assert longest_common_subsequence('daenarys', 'targaryen') == 'aary'

def test_case003():
    assert longest_common_subsequence('XMJYAUZ', 'MZJAWXU') == 'MJAU'

def test_case004():
    assert longest_common_subsequence('thisisatest', 'testing123testing') == 'tsitest'

def test_case005():
    assert longest_common_subsequence('1234', '1224533324') == '1234'

def test_case006():
    assert longest_common_subsequence('abcbdab', 'bdcaba') == 'bcba'

def test_case007():
    assert longest_common_subsequence('TATAGC', 'TAGCAG') == 'TAAG'

def test_case008():
    assert longest_common_subsequence('ABCBDAB', 'BDCABA') == 'BCBA'

def test_case009():
    assert longest_common_subsequence('ABCD', 'XBCYDQ') == 'BCD'

def test_case010():
    assert longest_common_subsequence('acbdegcedbg', 'begcfeubk') == 'begceb'

