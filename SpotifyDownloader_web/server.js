let downloadButton = document.getElementById("button")
downloadButton.addEventListener("click", navigateToURL)

function navigateToURL() {
    let urlInput = document.getElementById('url');
    let url = urlInput.value;
    console.log(url)
}