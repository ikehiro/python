import pytest

class TestStringConvert:
    # 前準備
    @pytest.fixture
    def target(self):
        from src.poetry_demo.fizz_buzz import string_convert        
        return string_convert

    check_value_data = [
          (1, '1')     
        , (2, '2')     
        , (3, 'Fizz')  
        , (6, 'Fizz')  
        , (5, 'Buzz')  
        , (10, 'Buzz') 
        , (15, 'FizzBuzz')
        , (30, 'FizzBuzz')
    ]

    # 検証
    @pytest.mark.parametrize('num, expected_return_value', check_value_data)
    def test_return_value(self, target, num, expected_return_value):      
        assert target(num) == expected_return_value
    
