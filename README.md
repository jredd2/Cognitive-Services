<br>[Alt Text](png-transparent-microsoft-azure-cloud-computing-microsoft-corporation-platform-as-a-service-business-cloud-computing-blue-angle-service.png)</br>
# Cognitive-Services
Analyze a local image using the Computer Vision REST API and Python

## What is Computer Vision? 
Computer Vision is an AI Microsoft Azure Service that can analyze content in images and videos. It is very powerful tool that can be used for tasks such as text extraction, spatial analysis, and image understanding to name a few. The most notable realm this could be useful in is law enforcement where cameras may be needed to identify suspects or possibly help in finding missing persons. It could also be used when processing patients within a hospital. The possibilities are endless so I encourage all to play around with this tool as I have.

### Objective: Use Azure Computer Vision AI to Analyze following in a local image in python:

Create a .py file name analyze-local-image.py to house our python application.

2. Create a new computer service api in Azure portal.


3. Import the various modules/libraries to include import os, import sys, import json, import pprint, import matplotlib, import requests, import dotenv.


4. Create a .env to protect your subscription_key and COMPUTER_VISION_KEY.


Protect your keys
5. Create an if statements to make use of the COMPUTER_VISION_KEY and use os.getenv to call on your .env file where API keys are stored.


6. Create an if statement for your endpoints so we can call on the analyze service.


Set image_path to the local path of an image that you want to analyze.

Read the image into a bite array you’ll need to reference the documentation for request parameters.

Print the output in json format for readability.

## Results
The output will be a nice well laid out json format that’s easy to read revealing some interesting information about the image we just analyzed.


### Prerequisites

A free Azure Subscription
A code editor/ IDE such as Visual Studio Code
Computer Vision API created in Azure
Github Account
