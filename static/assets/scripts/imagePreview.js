function previewImage() {
    const file = document.getElementById('imageInput').files[0];
    const preview  = document.getElementById('imagePreview');
    const reader = new FileReader();

    reader.addEventListener('load', function() {
        preview.src = reader.result;
        preview.style.display = 'block';
    });

    if (file) {
        reader.readAsDataURL(file)
    }

}