const API_URL = "http://localhost:8000/movies/";

// Funció per carregar totes les pel·lícules (READ)
async function fetchMovies() {
    try {
        const response = await fetch(API_URL);
        const movies = await response.json();
        const listBody = document.getElementById('movie-list');
        listBody.innerHTML = '';

        movies.forEach(movie => {
            const id = movie.id || movie._id;
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>
                    <strong>${movie.titol}</strong><br>
                    <span class="movie-desc">${movie.genere} | ${movie.usuari}</span>
                </td>
                <td>
                    <select onchange="updateMovieStatus('${id}', this.value)">
                        <option value="pendent de veure" ${movie.estat === 'pendent de veure' ? 'selected' : ''}>Pendent</option>
                        <option value="vista" ${movie.estat === 'vista' ? 'selected' : ''}>Vista</option>
                    </select>
                </td>
                <td>${movie.puntuacio} / 5</td>
                <td>
                    <button class="btn-delete" onclick="deleteMovie('${id}')">Eliminar</button>
                </td>
            `;
            listBody.appendChild(row);
        });
    } catch (error) {
        console.error("Error carregant pel·lícules:", error);
    }
}

// Funció per crear una pel·lícula (CREATE)
document.getElementById('movie-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const movieData = {
        titol: document.getElementById('titol').value,
        descripcio: document.getElementById('descripcio').value,
        estat: document.getElementById('estat').value,
        puntuacio: parseInt(document.getElementById('puntuacio').value),
        genere: document.getElementById('genere').value,
        usuari: document.getElementById('usuari').value
    };

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(movieData)
        });

        if (response.ok) {
            document.getElementById('movie-form').reset();
            fetchMovies();
        }
    } catch (error) {
        console.error("Error creant la pel·lícula:", error);
    }
});

// Funció per actualitzar només l'estat (UPDATE)
async function updateMovieStatus(id, newStatus) {
    try {
        await fetch(`${API_URL}${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ estat: newStatus })
        });
        // No cal recarregar tota la llista per un simple canvi d'estat
    } catch (error) {
        console.error("Error actualitzant estat:", error);
        fetchMovies(); // Recarreguem en cas d'error
    }
}

// Funció per eliminar una pel·lícula (DELETE)
async function deleteMovie(id) {
    if (!confirm("Segur que vols eliminar aquesta pel·lícula?")) return;

    try {
        const response = await fetch(`${API_URL}${id}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            fetchMovies();
        }
    } catch (error) {
        console.error("Error eliminant:", error);
    }
}

// Iniciar la càrrega quan el DOM estigui a punt
document.addEventListener('DOMContentLoaded', fetchMovies);

// Funció per buscar un element específic per ID
async function fetchById() {
    const idInput = document.getElementById("search-id-input").value.trim();

    if (!idInput) {
        alert("Si us plau, introdueix un ID per buscar.");
        return;
    }

    try {
        // Cridem al backend afegint l'ID al final de la URL constant
        const response = await fetch(API_URL + idInput);

        if (response.ok) {
            const data = await response.json();

            // Mostrem el resultat.
            // ULL: Canvia 'titol' i 'descripcio' pels noms reals de les teves variables si fas tasques
            alert(`Element trobat!\n\nTítol: ${data.titol}\nDescripció: ${data.descripcio}\nEstat: ${data.estat}`);

        } else if (response.status === 404) {
            alert("No s'ha trobat cap element amb aquest ID a la base de dades.");
        } else {
            alert("Error: Verifica que l'ID tingui el format correcte de MongoDB (24 caràcters).");
        }
    } catch (error) {
        console.error("Error al buscar per ID:", error);
        alert("Error de connexió amb el servidor.");
    }
}

async function filtrarPerGenere() {
    const genere = document.getElementById("filter-genere").value.trim();
    let url = API_URL;
    
    // Si ha escrit alguna cosa, afegim el paràmetre a la URL
    if (genere) {
        url = `${API_URL}?genere=${genere}`;
    }
    
    try {
        const response = await fetch(url);
        const movies = await response.json();
        
        // Codi repetit de fetchMovies per repintar la taula:
        const listBody = document.getElementById('movie-list');
        listBody.innerHTML = '';

        movies.forEach(movie => {
            const id = movie.id || movie._id;
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>
                    <strong>${movie.titol}</strong><br>
                    <span class="movie-desc">${movie.genere} | ${movie.usuari}</span>
                </td>
                <td>
                    <select onchange="updateMovieStatus('${id}', this.value)">
                        <option value="pendent de veure" ${movie.estat === 'pendent de veure' ? 'selected' : ''}>Pendent</option>
                        <option value="vista" ${movie.estat === 'vista' ? 'selected' : ''}>Vista</option>
                    </select>
                </td>
                <td>${movie.puntuacio} / 5</td>
                <td>
                    <button class="btn-delete" onclick="deleteMovie('${id}')">Eliminar</button>
                </td>
            `;
            listBody.appendChild(row);
        });
    } catch (error) {
        console.error("Error filtrant:", error);
    }
}
