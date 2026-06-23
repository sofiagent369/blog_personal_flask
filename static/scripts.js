document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;

    // Función para cargar posts desde el servidor
    async function loadPosts() {
        try {
            const response = await fetch('/api/posts');
            if (!response.ok) throw new Error(response.statusText);
            const posts = await response.json();
            
            const postList = document.querySelector('.post-list');
            postList.innerHTML = '';

            posts.forEach(post => {
                const article = document.createElement('article');
                article.className = 'post-item';
                
                const title = document.createElement('h3');
                title.textContent = post.title;

                const content = document.createElement('p');
                content.textContent = `${post.content.substring(0, 100)}...`;

                const readMoreLink = document.createElement('a');
                readMoreLink.className = 'read-more';
                readMoreLink.href = `#`;
                readMoreLink.textContent = 'Leer más';

                article.appendChild(title);
                article.appendChild(content);
                article.appendChild(readMoreLink);

                postList.appendChild(article);
            });
        } catch (error) {
            console.error('Error loading posts:', error);
        }
    }

    // Función para manejar el envío del formulario de creación/edición de posts
    async function handlePostFormSubmit(event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);

        try {
            let response;
            if (form.id === 'create-post-form') {
                response = await fetch('/api/posts', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        title: formData.get('title'),
                        content: formData.get('content')
                    })
                });
            } else if (form.id === 'edit-post-form') {
                const postId = form.getAttribute('data-post-id');
                response = await fetch(`/api/posts/${postId}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        title: formData.get('title'),
                        content: formData.get('content')
                    })
                });
            }

            if (!response.ok) throw new Error(response.statusText);
            const post = await response.json();
            alert(`Post ${form.id === 'create-post-form' ? 'creado' : 'actualizado'} con éxito`);
            form.reset();
            loadPosts();
        } catch (error) {
            console.error('Error submitting form:', error);
        }
    }

    // Cargar posts al cargar la página
    loadPosts();

    // Agregar eventos a los formularios de creación y edición de posts
    document.getElementById('create-post-form').addEventListener('submit', handlePostFormSubmit);
    document.querySelectorAll('.edit-post-form').forEach(form => {
        form.addEventListener('submit', handlePostFormSubmit);
    });
});