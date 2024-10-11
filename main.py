from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import io

app = Flask(__name__)

model = tf.keras.models.load_model("./pneumonia_model/pneumonia_model.keras")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/predict", methods=["POST"])
def predict():
    get_data = request.files["image"]
    img = tf.keras.preprocessing.image.load_img(io.BytesIO(get_data.read()), target_size=(150,150), color_mode="grayscale")
    img = tf.keras.preprocessing.image.img_to_array(img).astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    if prediction > 0.5:
        response_json = {
            "prediction": "Pneumonia",
            "confidence": str(prediction[0][0])
        } 
    
    else:
        response_json = {
            "prediction": "Normal",
            "confidence": str(prediction[0][0])
        }

    return jsonify(response_json)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)