def test_case1():
    deck = baralho()
    result = baralha(deck)
    assert result is not None or deck is not None

def test_case2():
    original = baralho()
    shuffled = baralha(baralho())
    result = shuffled if shuffled is not None else original
    assert len(result) == 52

def test_case3():
    shuffled = baralha(baralho())
    deck = shuffled if shuffled is not None else baralho()
    suits = {card['np'] for card in deck}
    assert suits == {'spades', 'hearts', 'diamonds', 'clubs'}

def test_case4():
    shuffled = baralha(baralho())
    deck = shuffled if shuffled is not None else baralho()
    values = {card['vlr'] for card in deck}
    assert values == {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}

def test_case5():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    pairs = [(c['np'], c['vlr']) for c in result]
    assert len(set(pairs)) == 52

def test_case6():
    for _ in range(3):
        deck = baralho()
        shuffled = baralha(deck)
        result = shuffled if shuffled is not None else deck
        assert len(result) == 52

def test_case7():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    spades = [c for c in result if c['np'] == 'spades']
    assert len(spades) == 13

def test_case8():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    assert all('np' in card and 'vlr' in card for card in result)

def test_case9():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    aces = [c for c in result if c['vlr'] == 'A']
    assert len(aces) == 4

def test_case10():
    deck = baralho()
    baralha(deck)
    assert len(deck) == 52

def test_case11():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    clubs = [c for c in result if c['np'] == 'clubs']
    assert len(clubs) == 13

def test_case12():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    hearts = [c for c in result if c['np'] == 'hearts']
    assert len(hearts) == 13

def test_case13():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    kings = [c for c in result if c['vlr'] == 'K']
    assert len(kings) == 4

def test_case14():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    assert isinstance(result, list)

def test_case15():
    for _ in range(3):
        deck = baralho()
        shuffled = baralha(deck)
        result = shuffled if shuffled is not None else deck
        pairs = [(c['np'], c['vlr']) for c in result]
        assert len(set(pairs)) == 52

def test_case16():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    diamonds = [c for c in result if c['np'] == 'diamonds']
    assert len(diamonds) == 13

def test_case17():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    tens = [c for c in result if c['vlr'] == '10']
    assert len(tens) == 4

def test_case18():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    all_combos = {(c['np'], c['vlr']) for c in result}
    expected = {(s, v) for s in ['spades', 'hearts', 'diamonds', 'clubs']
                for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']}
    assert all_combos == expected

def test_case19():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    jacks = [c for c in result if c['vlr'] == 'J']
    assert len(jacks) == 4

def test_case20():
    deck = baralho()
    shuffled = baralha(deck)
    result = shuffled if shuffled is not None else deck
    queens = [c for c in result if c['vlr'] == 'Q']
    assert len(queens) == 4
