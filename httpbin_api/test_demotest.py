
import pytest
import json
import requests


class Test_httpbin():

    def test_get_ip(self):
        BASE_URL="http://httpbin.org/"
        LOCAL_IP="120.34.205.175"
        IP_URL = "/ip"
        url = BASE_URL + IP_URL
        r = requests.get(url)
        print(r.headers)
        response_data = r.json()
        print(response_data)
        assert 200 == r.status_code
        assert LOCAL_IP == response_data["origin"]

    def test_post_method(self):
        BASE_URL="http://httpbin.org/"
        POST_TEST_URL="/post"
        url = BASE_URL + POST_TEST_URL
        post_data = {"name":"yourname","pwd":"123456"}
        r = requests.post(url,data = post_data)
        print(r.headers)
        print(r.text)
        response_data = r.json()
        assert 200 == r.status_code
        assert post_data["name"] == response_data["form"]["name"]
        assert post_data["pwd"] == response_data["form"]["pwd"]

    if __name__ == '__main__':
        # url_get = "http://httpbin.org//ip"
        # url_post = "http://httpbin.org//post"
        # test_get_ip(url_get)
        # test_post_method(url_post)

        pytest.main(["-s", "test_demotest.py", "--html=report.html"])
