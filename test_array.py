from mini_array import MiniArray

def test_addition():
    a = MiniArray([1, 2, 3])
    b = MiniArray([4, 5, 6])
    result = a + b
    assert result.data == [5, 7, 9], f'expected [5, 7, 9] but got {result.data}'

def test_addition_scalar():
    a = MiniArray([1, 2, 3])
    result = a + 5
    assert result.data == [6, 7, 8]

def test_multiplication():
    a = MiniArray([1, 2, 3])
    b = MiniArray([4, 5, 6])
    result = a * b
    assert result.data == [4, 10, 18]

def test_multiplication_scalar():
    a = MiniArray([1, 2, 3])
    result = 2 * a 
    assert result.data == [2, 4, 6]

def test_subtraction():
    a = MiniArray([5, 6, 7])
    b = MiniArray([1, 2, 3])
    result = a - b
    assert result.data == [4, 4, 4]

def test_subtraction_scalar():
    a = MiniArray([5, 6, 7])
    result = a - 2
    assert result.data == [3, 4, 5]

def test_division():
    a = MiniArray([10, 20, 30])
    b = MiniArray([2, 5, 10])
    result = a / b
    assert result.data == [5.0, 4.0, 3.0]

def test_division_scalar():
    a = MiniArray([10, 20, 30])
    result = a / 10
    assert result.data == [1.0, 2.0, 3.0]

def test_division_by_zero_in_array():
    a = MiniArray([1, 2, 3])
    b = MiniArray([1, 0, 1])
    result = a / b
    assert result.data == [1.0, float('inf'), 3.0]

def test_division_by_zero_scalar():
    a = MiniArray([1, 2, 3])
    result = a / 0
    assert result.data == [float('inf'), float('inf'), float('inf')]

if __name__ == "__main__":
    test_addition()
    test_addition_scalar()
    test_multiplication()
    test_multiplication_scalar()
    test_subtraction()
    test_subtraction_scalar()
    test_division()
    test_division_scalar()
    test_division_by_zero_in_array()
    test_division_by_zero_scalar()
    print("✅ All tests passed!")