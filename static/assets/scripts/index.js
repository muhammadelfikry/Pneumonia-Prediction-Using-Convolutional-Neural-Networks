document.getElementById('uploadForm').onsubmit = async function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/api/predict', {
        method: "POST",
        body: formData
    });
    const result = await response.json();
    document.getElementById('result').innerHTML = `
    <p>Status: ${result.prediction}</p>
    <p>Confidence: ${result.confidence}</p>
    `;
}