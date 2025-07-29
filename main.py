from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import io

app = Flask(__name__)

# Load model once at startup
model = tf.keras.models.load_model("./pneumonia_model/pneumonia_model.keras")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files["image"]

    try:
        # Preprocess image
        image = tf.keras.preprocessing.image.load_img(
            io.BytesIO(image_file.read()),
            target_size=(150, 150),
            color_mode="grayscale"
        )
        image_array = tf.keras.preprocessing.image.img_to_array(image).astype("float32") / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        # Predict
        prediction = model.predict(image_array)[0][0]

        label = "Pneumonia" if prediction > 0.5 else "Normal"

        return jsonify({
            "prediction": label,
            "confidence": f"{prediction:.4f}"
        })

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)