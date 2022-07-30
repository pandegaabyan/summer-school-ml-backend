import requests
import time
import numpy as np

MODEL_API_URL = "http://localhost:4000/predict"
IMAGE_PATH = "image.png"

image = open(IMAGE_PATH, "rb").read()
last = time.time()
r = requests.post(MODEL_API_URL, files={"image": image}).json()
print(r)
print("time taken :", time.time()-last)