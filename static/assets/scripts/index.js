document.getElementById('uploadForm').onsubmit = async function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/api/predict', {
        method: "POST",
        body: formData
    });
    const result = await response.json();
    document.getElementById('result').innerText = result.prediction + " (Confidence: " + result.confidence + ")";
}