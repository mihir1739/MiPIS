import requests
import json
import base64
import os
from PIL import Image
from django.conf import settings
def compare(a,b):
    '''
    API call request sent from here.Used to find similiarity between the faces.
    Parameters:
    a: path to first image.
    b: path to secind image.
    '''
    url = "https://api-us.faceplusplus.com/facepp/v3/compare"
    api_key = "Dq2Wy1yC_mKVIc--6Paiysiaxo1laa2Z"
    api_secret = "KAhncIFWAOjqUu2vFqOZG2WGvD_LK7Il"
    img1_path = os.path.join(settings.MEDIA_ROOT,str(a))
    img2_path =  os.path.join(settings.MEDIA_ROOT,str(b))
    image1 = Image.open(img1_path)
    image2 = Image.open(img2_path)
    # e_i1 = base64.b64encode(image1)
    # e_i2 = base64.b64encode(image2)

    
    r = requests.post(url=url,data={
        "api_key":api_key,
        "api_secret":api_secret,
        "image_base64_1":base64.b64encode(open(img1_path, "rb").read()),
        "image_base64_2":base64.b64encode(open(img2_path, "rb").read())
    })

    file = open('geek.txt', 'w')
    f = dict(r.json())
    file.write(str(f))
    return f['confidence']
    

# def compare(a,b):
#     a = 'http://' + settings.ALLOWED_HOSTS[3]+ settings.MEDIA_URL + str(a)
#     b = 'http://' + settings.ALLOWED_HOSTS[3]+ settings.MEDIA_URL + str(b)
#     print(a)
#     print(b)
#     return 90.0
# x = compare(12,5)
# print(x)
# image1 = Image.open('/home/mihir/Code/Engage/Server/media/images/staff/APJ.jpeg')
# with open('/home/mihir/Code/Engage/Server/media/images/staff/APJ.jpeg', "rb") as img1_file:
#     e_i1 = base64.b64encode(img1_file.read())
# print(e_i1)
# e_i1 = base64.b64encode(image1)
# print(e_i1)
# image2 = Image.open(img2_path)