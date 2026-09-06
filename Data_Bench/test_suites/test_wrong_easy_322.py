# Test suite for wrong_easy_322  (slug: minimum-index-sum-of-two-lists)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_322.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.findRestaurant(['Shogun', 'Tapioca Express', 'Burger King', 'KFC'], ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun']) == ['Shogun']

def test_case_2():
    sol = Solution()
    assert sol.findRestaurant(['Shogun', 'Tapioca Express', 'Burger King', 'KFC'], ['KFC', 'Shogun', 'Burger King']) == ['Shogun']

def test_case_3():
    sol = Solution()
    assert sol.findRestaurant(['happy', 'sad', 'good'], ['sad', 'happy', 'good']) == ['happy', 'sad']

def test_case_4():
    sol = Solution()
    assert sol.findRestaurant(['Shogun'], ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun']) == ['Shogun']

def test_case_5():
    sol = Solution()
    assert sol.findRestaurant(['Burger King', 'KFC', 'Shogun', 'Tapioca Express'], ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun']) == ['Shogun']

def test_case_6():
    sol = Solution()
    assert sol.findRestaurant(['KFC', 'Burger King', 'Tapioca Express', 'Shogun'], ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun']) == ['Shogun']

def test_case_7():
    sol = Solution()
    assert sol.findRestaurant(['Shogun', 'Tapioca Express', 'Burger King', 'KFC', 'x'], ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun']) == ['Shogun']

def test_case_8():
    sol = Solution()
    assert sol.findRestaurant(['Shogun', 'Tapioca Express', 'Burger King', 'KFC'], ['Hungry Hunter Steakhouse', 'Piatti', 'Shogun', 'The Grill at Torrey Pines']) == ['Shogun']

def test_case_9():
    sol = Solution()
    assert sol.findRestaurant(['Shogun', 'Tapioca Express', 'Burger King', 'KFC'], ['Shogun', 'Hungry Hunter Steakhouse', 'The Grill at Torrey Pines', 'Piatti']) == ['Shogun']

def test_case_10():
    sol = Solution()
    assert sol.findRestaurant(['Shogun', 'Tapioca Express', 'Burger King', 'KFC'], ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun', 'x']) == ['Shogun']

def test_case_11():
    sol = Solution()
    assert sol.findRestaurant(['Shogun'], ['KFC', 'Shogun', 'Burger King']) == ['Shogun']

def test_case_12():
    sol = Solution()
    assert sol.findRestaurant(['Burger King', 'KFC', 'Shogun', 'Tapioca Express'], ['KFC', 'Shogun', 'Burger King']) == ['KFC']

def test_case_13():
    sol = Solution()
    assert sol.findRestaurant(['KFC', 'Burger King', 'Tapioca Express', 'Shogun'], ['KFC', 'Shogun', 'Burger King']) == ['KFC']

def test_case_14():
    sol = Solution()
    assert sol.findRestaurant(['Shogun', 'Tapioca Express', 'Burger King', 'KFC', 'x'], ['KFC', 'Shogun', 'Burger King']) == ['Shogun']

def test_case_15():
    sol = Solution()
    assert sol.findRestaurant(['Shogun', 'Tapioca Express', 'Burger King', 'KFC'], ['KFC']) == ['KFC']

