def test_case1():
    result = ataques_rainhas({}, (4, 4), 'white')
    assert result == {'white': [], 'black': []}

def test_case2():
    board = {(4, 7): ['pawn', 'black']}
    result = ataques_rainhas(board, (4, 4), 'white')
    assert len(result['black']) == 1
    assert result['black'][0][0] == 'pawn'
    assert result['black'][0][2] == (4, 7)

def test_case3():
    board = {(4, 7): ['pawn', 'white']}
    result = ataques_rainhas(board, (4, 4), 'white')
    assert result == {'white': [], 'black': []}

def test_case4():
    board = {(4, 6): ['pawn', 'white'], (4, 8): ['rook', 'black']}
    result = ataques_rainhas(board, (4, 4), 'white')
    assert result == {'white': [], 'black': []}

def test_case5():
    board = {(6, 6): ['bishop', 'black']}
    result = ataques_rainhas(board, (4, 4), 'white')
    assert len(result['black']) == 1
    assert result['black'][0][2] == (6, 6)

def test_case6():
    board = {(4, 5): ['pawn', 'black'], (4, 8): ['rook', 'black']}
    result = ataques_rainhas(board, (4, 4), 'white')
    assert len(result['black']) == 1
    assert result['black'][0][2] == (4, 5)

def test_case7():
    board = {(4, 7): ['pawn', 'white']}
    result = ataques_rainhas(board, (4, 4), 'black')
    assert len(result['white']) == 1
    assert result['white'][0][2] == (4, 7)

def test_case8():
    board = {(7, 4): ['rook', 'black']}
    result = ataques_rainhas(board, (4, 4), 'white')
    assert len(result['black']) == 1
    assert result['black'][0][2] == (7, 4)

def test_case9():
    board = {
        (4, 7): ['pawn', 'black'],
        (4, 1): ['knight', 'black'],
        (7, 4): ['rook', 'black'],
        (1, 4): ['rook', 'black'],
        (7, 7): ['bishop', 'black'],
        (7, 1): ['bishop', 'black'],
        (1, 7): ['pawn', 'black'],
        (1, 1): ['queen', 'black']
    }
    result = ataques_rainhas(board, (4, 4), 'white')
    assert len(result['black']) == 8

def test_case10():
    result = ataques_rainhas({}, (4, 4), 'white')
    assert isinstance(result, dict)
    assert 'white' in result
    assert 'black' in result

def test_case11():
    board = {(4, 7): ['pawn', 'black']}
    result = ataques_rainhas(board, (4, 4), 'white')
    piece = result['black'][0]
    assert isinstance(piece, list)
    assert len(piece) == 3
    assert piece[0] == 'pawn'
    assert piece[1] == 'black'
    assert isinstance(piece[2], tuple)

def test_case12():
    board = {(5, 5): ['pawn', 'white'], (7, 7): ['bishop', 'black']}
    result = ataques_rainhas(board, (4, 4), 'white')
    assert result == {'white': [], 'black': []}

def test_case13():
    board = {
        (4, 6): ['pawn', 'black'],
        (6, 4): ['rook', 'black'],
        (6, 6): ['bishop', 'black']
    }
    result = ataques_rainhas(board, (4, 4), 'white')
    assert len(result['black']) == 3

def test_case14():
    board = {
        (4, 6): ['pawn', 'white'],
        (4, 2): ['rook', 'black'],
        (6, 4): ['bishop', 'black'],
        (2, 4): ['pawn', 'white']
    }
    result = ataques_rainhas(board, (4, 4), 'white')
    positions = [p[2] for p in result['black']]
    assert (4, 2) in positions
    assert (6, 4) in positions
    assert len(result['black']) == 2

def test_case15():
    board = {(8, 4): ['king', 'black']}
    result = ataques_rainhas(board, (1, 4), 'white')
    assert len(result['black']) == 1
    assert result['black'][0][2] == (8, 4)

def test_case16():
    board = {
        (4, 5): ['pawn', 'white'],
        (4, 3): ['pawn', 'white'],
        (5, 4): ['pawn', 'white'],
        (3, 4): ['pawn', 'white'],
        (5, 5): ['pawn', 'white'],
        (5, 3): ['pawn', 'white'],
        (3, 5): ['pawn', 'white'],
        (3, 3): ['pawn', 'white']
    }
    result = ataques_rainhas(board, (4, 4), 'white')
    assert result['black'] == []

def test_case17():
    board = {(1, 8): ['rook', 'black']}
    result = ataques_rainhas(board, (1, 1), 'white')
    assert result['black'][0][2] == (1, 8)

def test_case18():
    board = {
        (5, 5): ['pawn', 'white'],
        (5, 3): ['pawn', 'white'],
        (3, 5): ['rook', 'white'],
        (3, 3): ['rook', 'white']
    }
    result = ataques_rainhas(board, (4, 4), 'black')
    assert len(result['white']) == 4

def test_case19():
    board = {(4, 6): ['pawn', 'black'], (4, 7): ['rook', 'black']}
    result = ataques_rainhas(board, (4, 4), 'white')
    positions = [p[2] for p in result['black']]
    assert (4, 6) in positions
    assert (4, 7) not in positions

def test_case20():
    board = {(4, 7): ['pawn', 'black'], (7, 4): ['rook', 'black']}
    result = ataques_rainhas(board, (4, 4), 'white')
    assert len(result['black']) == 2
    assert result['white'] == []
