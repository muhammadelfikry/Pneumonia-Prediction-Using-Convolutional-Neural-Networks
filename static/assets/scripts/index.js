document.getElementById('uploadForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData(this);

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const result = await response.json();

        const resultElement = document.getElementById('result');
        resultElement.innerHTML = `
            <p>Status: ${result.prediction}</p>
            <p>Confidence: ${result.confidence}</p>
        `;
        resultElement.classList.add('active');
    } catch (error) {
        console.error('Error during prediction:', error);

        document.getElementById('result').innerHTML = `
            <p style="color: red;">Error: ${error.message}</p>
        `;
    }
});
