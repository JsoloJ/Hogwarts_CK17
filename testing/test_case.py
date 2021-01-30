# -*- coding: utf-8 -*-
import pytest
import sys
from testing.common import deal_datas
sys.path.append('..')
from pythoncode.Calculator import Calculator



class TestCalc:
    data:list=deal_datas.get_datas()

    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,result",data["add"]["datas"],ids=data["add"]["ids"])
    def test_add(self,a,b,result):
        assert result == self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,result",data["div"]["datas"],ids=data["div"]["ids"])
    def test_div(self,a,b,result):
        if b == 0:
            try:
                self.calc.div(self,a,b)
            except Exception as f:
                print('除数不能为零')
        else:
            assert result == self.calc.div(a,b)

if __name__ == '__main__':
    pytest.main(["-v","-s"])