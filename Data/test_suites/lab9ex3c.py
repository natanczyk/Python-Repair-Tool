def test_case1():
    result = distribui(baralho(), 4)
    assert len(result) == 4

def test_case2():
    result = distribui(baralho(), 4)
    assert all(len(hand) == 13 for hand in result)

def test_case3():
    result = distribui(baralho(), 2)
    assert len(result) == 2

def test_case4():
    result = distribui(baralho(), 2)
    assert all(len(hand) == 26 for hand in result)

def test_case5():
    result = distribui(baralho(), 1)
    assert len(result) == 1

def test_case6():
    result = distribui(baralho(), 1)
    assert len(result[0]) == 52

def test_case7():
    result = distribui(baralho(), 13)
    assert all(len(hand) == 4 for hand in result)

def test_case8():
    result = distribui(baralho(), 5)
    cards_per_player = len(result[0])
    assert cards_per_player * 5 <= 52
    assert (cards_per_player + 1) * 5 > 52

def test_case9():
    result = distribui(baralho(), 4)
    all_cards = [card for hand in result for card in hand]
    pairs = [(c['np'], c['vlr']) for c in all_cards]
    assert len(set(pairs)) == len(pairs)

def test_case10():
    result = distribui(baralho(), 4)
    assert all(isinstance(hand, list) for hand in result)

def test_case11():
    result = distribui(baralho(), 4)
    total = sum(len(hand) for hand in result)
    assert total % 4 == 0

def test_case12():
    result = distribui(baralho(), 3)
    assert len(result) == 3
    cards_per = len(result[0])
    assert cards_per * 3 <= 52

def test_case13():
    result = distribui(baralho(), 3)
    assert all(len(hand) == len(result[0]) for hand in result)

def test_case14():
    result = distribui(baralho(), 4)
    sizes = {len(hand) for hand in result}
    assert len(sizes) == 1

def test_case15():
    result = distribui(baralho(), 2)
    all_cards = [card for hand in result for card in hand]
    assert all('np' in c and 'vlr' in c for c in all_cards)

def test_case16():
    result = distribui(baralho(), 13)
    assert len(result) == 13

def test_case17():
    result = distribui(baralho(), 52)
    assert len(result) == 52
    assert all(len(hand) == 1 for hand in result)

def test_case18():
    result = distribui(baralho(), 4)
    all_cards = [card for hand in result for card in hand]
    assert len(all_cards) == 52

def test_case19():
    result = distribui(baralho(), 5)
    total = sum(len(hand) for hand in result)
    assert total <= 52

def test_case20():
    for n in [2, 4, 13]:
        result = distribui(baralho(), n)
        assert len(result) == n
        sizes = {len(hand) for hand in result}
        assert len(sizes) == 1
