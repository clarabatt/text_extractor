document.getElementById('fileInput').addEventListener('change', function(e) {
    var fileName = e.target.files[0].name;
    document.getElementById('fileName').innerText = fileName;
});