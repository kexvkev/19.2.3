import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc=Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self,2,2)==4
    def test_division_correctly(self):
        assert self.calc.division(self,10,5)==2
    def test_subtractiom_correctly(self):
        assert self.calc.subtraction(self,16,8)==8
    def test_adding_correctly(self):
        assert self.calc.adding(self,5,5)==10