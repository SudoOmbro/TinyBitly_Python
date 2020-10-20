import requests


class NullStringException(Exception):
    pass


class Result:

    def __init__(self, ll=None, sl=None):
        self.long = ll
        self.short = sl
        self.ok = False
        self.error = None


class Bitly:

    API_URL = "https://api-ssl.bitly.com/v4/{endpoint}"

    def __init__(self, api_token):
        self.apiToken = api_token
        self.header = {'Content-Type': 'application/json',
                       'Authorization': f'Bearer {self.apiToken}'}

    def shorten(self, long_url: str):
        """
        shortens a url

        :param long_url: the url to shorten.
        :return: a Result object containing the original url, the shortened url, the status and the error message.
        :rtype: Result
        """
        if long_url is None:
            raise NullStringException("long_url is None")
        result = Result(ll=long_url)
        payload = {"long_url": long_url}
        self._call_api("shorten", payload, result, "link", "short")
        return result

    def expand(self, short_url: str):
        """
        expands a previously shortened url

        :param short_url: the previously shortened url
        :return: a Result object containing the original url, the shortened url, the status and the error message.
        :rtype: Result
        """
        if short_url is None:
            raise NullStringException("short_url is None")
        result = Result(sl=short_url)
        bitlink_id = short_url[8:]  # remove https://
        payload = {"bitlink_id": bitlink_id}
        self._call_api("expand", payload, result, "long_url", "long")
        return result

    def _call_api(self, endpoint, payload, result, response_field, result_field):
        # send request and get response
        response = requests.post(
            self.API_URL.format(endpoint=endpoint),
            headers=self.header,
            json=payload
        )
        # fill result according to the response
        if response.status_code == 200 or response.status_code == 201:
            result.__dict__[result_field] = (response.json())[response_field]
            result.ok = True
        else:
            result.error = (response.json())['message']


if __name__ == "__main__":
    # test
    bitly = Bitly("YOUR_API_TOKEN_HERE")
    original_link = "https://github.com/SudoOmbro"
    short_link = bitly.shorten(original_link).short
    long_link = bitly.expand(short_link).long
    print(f"here's the original link: {original_link}")
    print(f"here's the shortened link: {short_link}")
    print(f"here's the expanded link: {long_link} (it should be equal to the first one)")
