from main import add

def test_add_correct():
    # 測試 1+1 是否等於 2
    assert add(1, 1) == 2

def test_add_negative():
    # 測試 -1+1 是否等於 0
    assert add(-1, 1) == 0
