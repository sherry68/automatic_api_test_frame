import pytest

class TestApi:

    @pytest.mark.parametrize('args', [['a',12], ['b',13], ['c',14]])
    def test_api1(self,args):
        print("output is ", args)

    @pytest.mark.parametrize('name, age', [['a',12], ['b',13], ['c',14]])
    def test_api2(self, name, age):
        print(name, age)



if __name__ == '__main__':
    pytest.main(['--vs, test_api.py'])

