from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(3)) == 5*3
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10*10
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(2)) == 5*2
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(3)) == 10*3
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1*1

