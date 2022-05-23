import requests
import json
from django.conf import settings
def compare(a,b):
    url = "https://api-us.faceplusplus.com/facepp/v3/compare"
    api_key = "Dq2Wy1yC_mKVIc--6Paiysiaxo1laa2Z"
    api_secret = "KAhncIFWAOjqUu2vFqOZG2WGvD_LK7Il"
    image1_url = "https://cdn.britannica.com/48/222648-050-F4D0A2D8/President-of-India-A-P-J-Abdul-Kalam-2007.jpg"
    image2_url = "https://img.etimg.com/thumb/width-1200,height-900,imgsize-56008,resizemode-1,msid-48264767/news/politics-and-nation/former-president-apj-abdul-kalams-unfinished-lecture-to-appear-in-new-book.jpg"

    data = {"api_key":api_key,
            "api_secret":api_secret,
            "image_url1":image1_url,
            "image_url2":image2_url}

    r = requests.post(url=url,data=data)
    f = dict(r.json())
    return f["confidence"]

# def compare(a,b):
#     a = settings.MEDIA_URL + str(a)
#     b = settings.MEDIA_URL + str(b)
#     print(a)
#     print(b)
#     return 90.0