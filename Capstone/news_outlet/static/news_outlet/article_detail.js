document.addEventListener('DOMContentLoaded', function() {
    const saveButton = document.getElementById('save-article');
    saveButton.addEventListener('click', () => save_unsave(saveButton.getAttribute('data-article-id')));
});

function save_unsave(articleId) {
    const saveButton = document.getElementById('save-article');

    fetch(`/save_article/${articleId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: 'action= bookmark',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.result); // Check for the correct key 'result'
        console.log(data.error);  // save any errors
        if (data.result === "saved") {
            saveButton.innerText = 'Unsave Article';
            saveButton.classList.remove('btn-primary');
            saveButton.classList.add('btn-warning');
        } else if (data.result === "deleted") {
            saveButton.innerText = 'Save Article';
            saveButton.classList.remove('btn-warning');
            saveButton.classList.add('btn-primary');
        } else {
            console.log("if eleif failed")
            saveButton.innerText = 'Unable';
        }
    });
}
