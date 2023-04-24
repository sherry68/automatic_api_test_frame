import pytest

from common.yaml_util import YamlUtil


@pytest.fixture(scope='function')
def conn_database():
    print('\nconnect')
    yield
    print('\ndisconnect')

@pytest.fixture(scope="class", autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()
