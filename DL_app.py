import numpy as np
import tensorflow as tf
import flask
import cv2
import io
app = flask.Flask(__name__)
model = tf.keras.applications.mobilenet_v2.MobileNetV2(weights="imagenet")
print("Model loaded")

def preprocess(image):
    result = io.BytesIO(image.read())
    result = cv2.imdecode(np.frombuffer(result.read(), np.uint8), 1)
    result = cv2.resize(result, (224,224))
    result = np.expand_dims(result, axis=0)
    return result

def postprocess(preds):
    final_result = []
    result = tf.keras.applications.imagenet_utils.decode_predictions(preds)
    for (imagenetID, label, prob) in result[0]:
        r = {"label": label, "probability": float(prob)}
        final_result.append(r)
    return final_result

## handle request here

if __name__ == '__main__':
    app.run(port=4000, debug=True)