import numpy as np
import tensorflow as tf
import flask
import cv2
import io
app = flask.Flask(__name__)
model = tf.keras.applications.resnet50.ResNet50(weights="imagenet")
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

@app.route('/predict', methods=["POST"])
def predict():
    results = {"success":False, "predictions":[]}
    if flask.request.method == "POST":
        if flask.request.files["image"]:
            try:
                image = preprocess(flask.request.files["image"])
                preds = model.predict(image)
                results["predictions"] = postprocess(preds)
                results["success"] = True
                return results
            except Exception as e:
                print(e)
                return results

if __name__ == '__main__':
    app.run(port=4000, debug=True)