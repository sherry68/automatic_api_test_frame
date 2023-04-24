import requests
import pytest
import json
from common.yaml_util import YamlUtil
from common.requests_util import RequestsUtil


# url = "https://api.douban.com/v2/movie/subject/36193784"
# url = "https://pokeapi.co/api/v2/{endpoint}/"
# print(rep.cookies)
# print(rep.status_code)
# print(rep.reason)
# fetch('https://jsonplaceholder.typicode.com/posts', {
#   method: 'POST',
#   body: JSON.stringify({
#     title: 'foo',
#     body: 'bar',
#     userId: 1,
#   }),
#   headers: {
#     'Content-type': 'application/json; charset=UTF-8',
#   },
# })
#   .then((response) => response.json())
#   .then((json) => console.log(json));



class TestSendRequests:

    # def setup_method(self):
    #     print('execute this case before each functional test case')
    # def teardown_method(self):
    #     print('execute this case after each functional test case')

    access_token = ''
    cks = ''
    session = requests.session()

    @pytest.mark.smoke
    def test_get_ability(self):
        url = "https://pokeapi.co/api/v2/ability/"
        # rep = self.get_session().get(url, params=None)
        #rep = TestSendRequests.session.get(url, params=None)
        rep = requests.get(url, params=None)
        print(rep.status_code)
        print(rep.json())

        assert rep.status_code == 200
        assert rep.json()['count'] != 400
        assert "count" in rep.json()

    @pytest.mark.function
    def test_get_berry(self, conn_database):
        url = "https://pokeapi.co/api/v2/berry-firmness/1"
        rep = requests.request('get', url, params=None)
        print(rep.status_code)

    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('get_pet.yml'))
    def test_place_post(self, caseinfo):
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        headers = caseinfo['request']['headers']
        method = caseinfo['request']['method']

        rep = RequestsUtil().send_request(method, data, url, headers=headers)
        # rep = requests.request(method, url, data=json.dumps(data), headers=headers)

        # 'put'
        # print(rep.content)
        # rep = json.load(rep)
        print('\n', rep.status_code)
        print(rep.json())
        if method == 'get':
            assert rep.status_code == 200
        else:
            assert rep.status_code == 201
        # raise Exception("fail")

        # url = "https://jsonplaceholder.typicode.com/posts"
        # data = {'title': 'first', 'body': 'second', 'userId': 1}
        # headers = {'Content-type': 'application/json; charset=UTF-8'}
        # rep = requests.request('post', url, data=json.dumps(data), headers=headers)
        # # 'put'
        # # print(rep.content)
        # print(rep.status_code)
        # print(rep.json())
        # # raise Exception("fail")

    # def test_translate(self):
    #     url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    #
    #     # payload = "q=Hello%2C%20world!&target=es&source=en"
    #     data = {'q': 'Hello world', 'target':' zh'}
    #     headers = {
    #         "content-type": "application/x-www-form-urlencoded",
    #         "Accept-Encoding": "application/gzip",
    #         "X-RapidAPI-Key": "e810d517cdmsh385e926c5c01e02p13fa71jsn15fdfd95d0e9",
    #         "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    #     }
    #
    #     response = requests.request("POST", url, data = json.dumps(data), headers=headers)
    #
    #     print(response.text)


