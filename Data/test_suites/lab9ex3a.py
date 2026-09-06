def test_case1():
    assert len(baralho()) == 52

def test_case2():
    deck = baralho()
    suits = {card['np'] for card in deck}
    assert suits == {'spades', 'hearts', 'diamonds', 'clubs'}

def test_case3():
    deck = baralho()
    values = {card['vlr'] for card in deck}
    assert values == {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}

def test_case4():
    deck = baralho()
    assert {'np': 'spades', 'vlr': 'A'} in deck

def test_case5():
    deck = baralho()
    assert {'np': 'hearts', 'vlr': 'K'} in deck

def test_case6():
    deck = baralho()
    assert {'np': 'diamonds', 'vlr': '10'} in deck

def test_case7():
    deck = baralho()
    assert {'np': 'clubs', 'vlr': 'J'} in deck

def test_case8():
    deck = baralho()
    pairs = [(c['np'], c['vlr']) for c in deck]
    assert len(set(pairs)) == 52

def test_case9():
    deck = baralho()
    spades = [c for c in deck if c['np'] == 'spades']
    assert len(spades) == 13

def test_case10():
    deck = baralho()
    hearts = [c for c in deck if c['np'] == 'hearts']
    assert len(hearts) == 13

def test_case11():
    deck = baralho()
    diamonds = [c for c in deck if c['np'] == 'diamonds']
    assert len(diamonds) == 13

def test_case12():
    deck = baralho()
    clubs = [c for c in deck if c['np'] == 'clubs']
    assert len(clubs) == 13

def test_case13():
    deck = baralho()
    aces = [c for c in deck if c['vlr'] == 'A']
    assert len(aces) == 4

def test_case14():
    deck = baralho()
    assert all('np' in card and 'vlr' in card for card in deck)

def test_case15():
    deck = baralho()
    assert isinstance(deck, list)

def test_case16():
    deck = baralho()
    kings = [c for c in deck if c['vlr'] == 'K']
    assert len(kings) == 4

def test_case17():
    deck = baralho()
    tens = [c for c in deck if c['vlr'] == '10']
    assert len(tens) == 4

def test_case18():
    deck = baralho()
    assert {'np': 'spades', 'vlr': 'K'} in deck

def test_case19():
    deck = baralho()
    assert {'np': 'clubs', 'vlr': 'A'} in deck

def test_case20():
    deck = baralho()
    all_combos = {(s, v) for s in ['spades', 'hearts', 'diamonds', 'clubs']
                  for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']}
    deck_combos = {(c['np'], c['vlr']) for c in deck}
    assert deck_combos == all_combos
