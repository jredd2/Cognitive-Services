# The main point of this code is to show how to call the Computer Vision API from Python

import os

# use json library to read data passsed back and the web serv
import sys
import json
import pprint

# Hide your keys protect it with your life
from dotenv import load_dotenv
load_dotenv(dotenv_path='C:/Users/jessiereddjr./venv/keys.env')

#import the requests library
import requests

import matplotlib.pyplot as plt
from PIL import Image 
from io import BytesIO

if 'COMPUTER_VISION_KEY' in os.environ:
    COMPUTER_VISION_KEY = os.getenv('COMPUTER_VISION_KEY')
    subscription_key = os.environ[COMPUTER_VISION_KEY]
#else: 
    #print("\nSet the COMPUTER_VISION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    #sys.exit()

if 'https://pythonimageanalayzer.cognitiveservices.azure.com/' in os.environ:
    endpoint = os.environ['https://pythonimageanalayzer.cognitiveservices.azure.com/']
endpoint = 'https://pythonimageanalayzer.cognitiveservices.azure.com/'
analyze_url = endpoint + "vision/v3.1/analyze"

# Set image_path to the local path of an image that you want to analyze.
# Sample images are here, if needed:
# https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images
image_path = "/Users/jessiereddjr./Documents/Docker-Logo-2013.png"

# Read the image into a byte array

subscription_key = '#####'
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color,Brands,tags'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(analysis)
print(analysis['color']['dominantColorBackground'])
image_caption = analysis["description"]["captions"][0]["text"].capitalize()
print()
print('all tags')
for item in analysis['description']['tags']:
    print(item)

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)
plt.show()
