import pytest

from Python.calc import Calc


class Testclac:

    def setup(self):
        self.calc = Calc()

    def test_add1(self):
        result = self.calc.add(1, 2)
        print(result)
        assert result == 3

    def test_add2(self):
        result = self.calc.add(0, 0)
        assert result == 0

    def test_add3(self):
        result = self.calc.add(-1, 7)
        assert result == 6

    def test_add4(self):
        result = self.calc.add(-1, -2)
        assert result == -3


if __name__ == '__main__':
    pytest.main(['-vs','Test_clac.py::Testclac'])
    # pytest.main(['-vs','Test_clac.py::Test_clac::test_add1'])
