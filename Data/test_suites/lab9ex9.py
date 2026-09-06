def test_case1():
    livros = {
        'Dom Casmurro': {'autor': 'Machado de Assis', 'ano': 1899},
        'O Alquimista': {'autor': 'Paulo Coelho', 'ano': 1988},
        'Os Lusiadas': {'autor': 'Luis de Camoes', 'ano': 1572}
    }
    assert mais_antigo(livros) == 'Os Lusiadas'

def test_case2():
    livros = {'Unico Livro': {'autor': 'Autor', 'ano': 2000}}
    assert mais_antigo(livros) == 'Unico Livro'

def test_case3():
    livros = {
        'A': {'autor': 'X', 'ano': 1900},
        'B': {'autor': 'Y', 'ano': 1800},
        'C': {'autor': 'Z', 'ano': 1700}
    }
    assert mais_antigo(livros) == 'C'

def test_case4():
    livros = {
        'Modern': {'autor': 'A', 'ano': 2020},
        'Old': {'autor': 'B', 'ano': 1500}
    }
    assert mais_antigo(livros) == 'Old'

def test_case5():
    livros = {
        'Livro1': {'autor': 'A', 'ano': 2000},
        'Livro2': {'autor': 'B', 'ano': 2001},
        'Livro3': {'autor': 'C', 'ano': 1999}
    }
    assert mais_antigo(livros) == 'Livro3'

def test_case6():
    livros = {
        'X': {'autor': 'A', 'ano': 1000},
        'Y': {'autor': 'B', 'ano': 999},
        'Z': {'autor': 'C', 'ano': 1001}
    }
    assert mais_antigo(livros) == 'Y'

def test_case7():
    livros = {
        'Alpha': {'autor': 'A', 'ano': 1850},
        'Beta': {'autor': 'B', 'ano': 1920},
        'Gamma': {'autor': 'C', 'ano': 1780},
        'Delta': {'autor': 'D', 'ano': 1960}
    }
    assert mais_antigo(livros) == 'Gamma'

def test_case8():
    livros = {
        'Book1': {'autor': 'A', 'ano': 2023},
        'Book2': {'autor': 'B', 'ano': 2022},
        'Book3': {'autor': 'C', 'ano': 2021}
    }
    assert mais_antigo(livros) == 'Book3'

def test_case9():
    livros = {
        'Ancient': {'autor': 'A', 'ano': 100},
        'Medieval': {'autor': 'B', 'ano': 1200},
        'Modern': {'autor': 'C', 'ano': 1900}
    }
    result = mais_antigo(livros)
    assert result == 'Ancient'

def test_case10():
    livros = {
        'P': {'autor': 'A', 'ano': 1950},
        'Q': {'autor': 'B', 'ano': 1949}
    }
    assert mais_antigo(livros) == 'Q'

def test_case11():
    livros = {
        'Livro': {'autor': 'A', 'ano': 0}
    }
    assert mais_antigo(livros) == 'Livro'

def test_case12():
    livros = {
        'First': {'autor': 'A', 'ano': 1},
        'Second': {'autor': 'B', 'ano': 2},
        'Third': {'autor': 'C', 'ano': 3}
    }
    assert mais_antigo(livros) == 'First'

def test_case13():
    livros = {
        'A1': {'titulo': 'A1', 'autor': 'A', 'ano': 1800},
        'A2': {'titulo': 'A2', 'autor': 'B', 'ano': 1799},
        'A3': {'titulo': 'A3', 'autor': 'C', 'ano': 1801}
    }
    assert mais_antigo(livros) == 'A2'

def test_case14():
    livros = {
        'New': {'autor': 'A', 'ano': 2025},
        'Old': {'autor': 'B', 'ano': 1400},
        'Very Old': {'autor': 'C', 'ano': 800}
    }
    assert mais_antigo(livros) == 'Very Old'

def test_case15():
    livros = {'Solo': {'autor': 'Autor', 'ano': 1984}}
    result = mais_antigo(livros)
    assert isinstance(result, str)

def test_case16():
    livros = {
        'Title A': {'autor': 'A', 'ano': 1600},
        'Title B': {'autor': 'B', 'ano': 1601},
        'Title C': {'autor': 'C', 'ano': 1602},
        'Title D': {'autor': 'D', 'ano': 1599}
    }
    assert mais_antigo(livros) == 'Title D'

def test_case17():
    livros = {
        'Newest': {'autor': 'A', 'ano': 2024},
        'Oldest': {'autor': 'B', 'ano': 1200}
    }
    result = mais_antigo(livros)
    assert result == 'Oldest'

def test_case18():
    livros = {
        'Z': {'autor': 'A', 'ano': 1950},
        'A': {'autor': 'B', 'ano': 1960},
        'M': {'autor': 'C', 'ano': 1940}
    }
    assert mais_antigo(livros) == 'M'

def test_case19():
    livros = {
        'Book X': {'autor': 'A', 'ano': 1700},
        'Book Y': {'autor': 'B', 'ano': 1750},
        'Book Z': {'autor': 'C', 'ano': 1650}
    }
    result = mais_antigo(livros)
    assert result == 'Book Z'

def test_case20():
    livros = {
        'Recent': {'autor': 'A', 'ano': 2000},
        'Older': {'autor': 'B', 'ano': 1900},
        'Oldest': {'autor': 'C', 'ano': 1800},
        'Newest': {'autor': 'D', 'ano': 2010}
    }
    assert mais_antigo(livros) == 'Oldest'
