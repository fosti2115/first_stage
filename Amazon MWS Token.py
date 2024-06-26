import requests

mws_token = "amzn.mws.a1b2cde3-abc1-e45f-gh67-89999ab0cdef

def make_mws_request(token):
    endpoint = "https://mws.amazonservices.com/Orders/2013-09-01"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    params = {
        "Action": "ListOrders",
        "SellerId": "A2NEXAMPLETF53",
        "MWSAuthToken": token
    }

    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200:
        print("Request was successful!")
        print("Response data:", response.text)
    else:
        print("Request failed!")
        print("Status code:", response.status_code)
        print("Error message:", response.text)

make_mws_request(mws_token)
