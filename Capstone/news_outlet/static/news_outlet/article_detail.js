document.addEventListener('DOMContentLoaded', function() {
    const saveButton = document.querySelector('#save-article');

    if (saveButton) {
        const isSaved = localStorage.getItem('isSaved');

        if (isSaved !== null) {
            saveButton.innerText = 'Unsave Article';
        } else {
            saveButton.innerText = 'Save Article';
        }

        saveButton.addEventListener('click', function() {
            const articleId = saveButton.getAttribute('data-article-id');
            
            fetch(`/save_article/${articleId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.saved !== undefined) {
                    isSaved = data.saved;
                    localStorage.setItem('isSaved', isSaved);

                    if (isSaved) {
                        saveButton.innerText = 'Unsave Article';
                    } else {
                        saveButton.innerText = 'Save Article';
                    }
                }
            })
            .catch(error => {
                console.error('An error occurred:', error);
            });
        });
    }
});