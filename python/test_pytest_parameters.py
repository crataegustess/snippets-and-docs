import pytest
import roman

@pytest.mark.parametrize("input1, output",[('V',5),('X',10),('I',1)])
def test_roman_convert_to_dec(input1:str, output:int):
    assert roman.convert_to_dec(input1) == output,"test failed"

@pytest.mark.parametrize("input1, output",[(5,'V'),(10,'X'),(1,'I'),(100,'C'),(50,'L'),(1983,'MCMLXXXIII'),(2150,'MMCL'),(1876,'MDCCCLXXVI')])
def test_roman_convert_to_roman(input1:int, output:str):
    assert roman.convert_to_roman(input1) == output,'test failed'