// 1. NODO CANCIÓN (Actualizado para tener portada)
class NodoCancion {
    titulo: string;
    artista: string;
    urlAudio: string;
    portada: string; // URL de la imagen (de iTunes o genérica)
    siguiente: NodoCancion | null;
    anterior: NodoCancion | null;

    constructor(titulo: string, artista: string, urlAudio: string, portada: string) {
        this.titulo = titulo;
        this.artista = artista;
        this.urlAudio = urlAudio;
        this.portada = portada;
        this.siguiente = null;
        this.anterior = null;
    }
}

// 2. LISTA DOBLEMENTE ENLAZADA
class PlaylistDoble {
    cabeza: NodoCancion | null = null;
    cola: NodoCancion | null = null;
    cancionActual: NodoCancion | null = null;
    longitud: number = 0;

    agregarAlFinal(titulo: string, artista: string, urlAudio: string, portada: string) {
        const nuevoNodo = new NodoCancion(titulo, artista, urlAudio, portada);
        if (!this.cabeza) {
            this.cabeza = nuevoNodo;
            this.cola = nuevoNodo;
        } else {
            if (this.cola) {
                this.cola.siguiente = nuevoNodo;
                nuevoNodo.anterior = this.cola;
                this.cola = nuevoNodo;
            }
        }
        this.longitud++;
        if(this.longitud === 1) this.cancionActual = this.cabeza;
    }

    agregarAlInicio(titulo: string, artista: string, urlAudio: string, portada: string) {
        const nuevoNodo = new NodoCancion(titulo, artista, urlAudio, portada);
        if (!this.cabeza) {
            this.cabeza = nuevoNodo;
            this.cola = nuevoNodo;
        } else {
            nuevoNodo.siguiente = this.cabeza;
            this.cabeza.anterior = nuevoNodo;
            this.cabeza = nuevoNodo;
        }
        this.longitud++;
        if(this.longitud === 1) this.cancionActual = this.cabeza;
    }

    agregarEnPosicion(titulo: string, artista: string, urlAudio: string, portada: string, posicion: number) {
        if (posicion <= 0) { this.agregarAlInicio(titulo, artista, urlAudio, portada); return; }
        if (posicion >= this.longitud) { this.agregarAlFinal(titulo, artista, urlAudio, portada); return; }

        const nuevoNodo = new NodoCancion(titulo, artista, urlAudio, portada);
        let actual: NodoCancion | null = this.cabeza;
        let contador = 0;

        while (actual !== null && contador < posicion) {
            actual = actual.siguiente;
            contador++;
        }

        if (actual && actual.anterior) {
            nuevoNodo.siguiente = actual;
            nuevoNodo.anterior = actual.anterior;
            actual.anterior.siguiente = nuevoNodo;
            actual.anterior = nuevoNodo;
            this.longitud++;
        }
    }

    eliminar(titulo: string): boolean {
        if (!this.cabeza) return false;
        let actual: NodoCancion | null = this.cabeza;
        
        while (actual !== null) {
            if (actual.titulo === titulo) {
                if (this.cancionActual === actual) {
                    this.cancionActual = actual.siguiente ? actual.siguiente : actual.anterior;
                }

                if (actual === this.cabeza) {
                    this.cabeza = actual.siguiente;
                    if (this.cabeza) this.cabeza.anterior = null;
                } else if (actual === this.cola) {
                    this.cola = actual.anterior;
                    if (this.cola) this.cola.siguiente = null;
                } else {
                    if (actual.anterior && actual.siguiente) {
                        actual.anterior.siguiente = actual.siguiente;
                        actual.siguiente.anterior = actual.anterior;
                    }
                }
                this.longitud--;
                return true;
            }
            actual = actual.siguiente;
        }
        return false;
    }

    siguienteCancion() {
        if (this.cancionActual && this.cancionActual.siguiente) {
            this.cancionActual = this.cancionActual.siguiente;
            return true;
        }
        return false;
    }

    anteriorCancion() {
        if (this.cancionActual && this.cancionActual.anterior) {
            this.cancionActual = this.cancionActual.anterior;
            return true;
        }
        return false;
    }
}

// ==========================================
// CONTROLADOR DE LA APLICACIÓN (DOM Y AUDIO)
// ==========================================
const miPlaylist = new PlaylistDoble();
const reproductorAudio = new Audio();
let reproduciendo = false;
const portadaPorDefecto = "https://via.placeholder.com/60/282828/FFFFFF?text=🎵";

// Elementos DOM Globales
const ulPlaylist = document.getElementById('ul-playlist') as HTMLUListElement;
const contadorCanciones = document.getElementById('contador-canciones') as HTMLSpanElement;
const selectPosicion = document.getElementById('select-posicion') as HTMLSelectElement;
const inputIndice = document.getElementById('input-indice') as HTMLInputElement;

// Elementos del Reproductor
const btnPlayPause = document.getElementById('btn-play-pause') as HTMLButtonElement;
const imgPortadaActual = document.getElementById('img-portada-actual') as HTMLImageElement;
const txtTituloActual = document.getElementById('txt-titulo-actual') as HTMLHeadingElement;
const txtArtistaActual = document.getElementById('txt-artista-actual') as HTMLParagraphElement;
const barraProgreso = document.getElementById('barra-progreso') as HTMLInputElement;

// --- GESTIÓN DE POSICIÓN ---
selectPosicion.addEventListener('change', () => {
    inputIndice.style.display = selectPosicion.value === 'cualquiera' ? 'block' : 'none';
});

function obtenerPosicionDeseada(): { metodo: string, indice: number } {
    const metodo = selectPosicion.value;
    let indice = -1;
    if (metodo === 'cualquiera') {
        const val = parseInt(inputIndice.value);
        if (!isNaN(val) && val > 0) indice = val - 1; // Convertir posición humana (1,2..) a índice (0,1..)
    }
    return { metodo, indice };
}

function procesarIngresoCancion(titulo: string, artista: string, url: string, portada: string) {
    const config = obtenerPosicionDeseada();
    
    if (config.metodo === 'final') {
        miPlaylist.agregarAlFinal(titulo, artista, url, portada);
    } else if (config.metodo === 'inicio') {
        miPlaylist.agregarAlInicio(titulo, artista, url, portada);
    } else if (config.metodo === 'cualquiera') {
        if (config.indice === -1) { alert("Ingresa un número de posición válido"); return; }
        miPlaylist.agregarEnPosicion(titulo, artista, url, portada, config.indice);
    }

    if (miPlaylist.longitud === 1) cargarCancionEnReproductor(false); // Carga la data pero no le da play
    actualizarUI();
}

// --- ACTUALIZAR INTERFAZ ---
function actualizarUI() {
    ulPlaylist.innerHTML = '';
    contadorCanciones.innerText = `${miPlaylist.longitud} canciones`;
    
    let actual = miPlaylist.cabeza;
    let index = 1;
    
    while (actual) {
        const li = document.createElement('li');
        li.className = 'playlist-item';
        if (actual === miPlaylist.cancionActual) li.classList.add('sonando');

        li.innerHTML = `
            <div class="cell-num">${index}</div>
            <div class="cell-titulo">
                <img src="${actual.portada}" alt="cover">
                <p>${actual.titulo}</p>
            </div>
            <div class="cell-artista">${actual.artista}</div>
        `;
        
        // Botón Eliminar
        const btnBorrar = document.createElement('button');
        btnBorrar.className = 'btn-eliminar';
        btnBorrar.innerText = '🗑';
        
        const tituloBorrar = actual.titulo;
        btnBorrar.onclick = () => {
            const eraActual = (miPlaylist.cancionActual?.titulo === tituloBorrar);
            miPlaylist.eliminar(tituloBorrar);
            if (eraActual) cargarCancionEnReproductor(true);
            actualizarUI();
        };

        const divAccion = document.createElement('div');
        divAccion.appendChild(btnBorrar);
        li.appendChild(divAccion);
        
        // Doble click para reproducir esta canción (Opcional, muy pro)
        const nodoCapturado = actual;
        li.ondblclick = () => {
            miPlaylist.cancionActual = nodoCapturado;
            cargarCancionEnReproductor(true);
            actualizarUI();
        };

        ulPlaylist.appendChild(li);
        actual = actual.siguiente;
        index++;
    }
}

// --- API DE ITUNES (OPCIÓN 1) ---
const inputBusqueda = document.getElementById('input-busqueda') as HTMLInputElement;
const btnBuscar = document.getElementById('btn-buscar') as HTMLButtonElement;
const contenedorResultados = document.getElementById('resultados-busqueda') as HTMLDivElement;

btnBuscar.addEventListener('click', async () => {
    const query = inputBusqueda.value.trim();
    if (!query) return;

    contenedorResultados.innerHTML = "<p style='font-size:0.8em; color:gray;'>Buscando...</p>";

    try {
        const respuesta = await fetch(`https://itunes.apple.com/search?term=${encodeURIComponent(query)}&media=music&limit=4`);
        const datos = await respuesta.json();

        contenedorResultados.innerHTML = "";
        
        if(datos.results.length === 0) {
            contenedorResultados.innerHTML = "<p style='font-size:0.8em; color:gray;'>No se encontraron resultados.</p>";
            return;
        }

        datos.results.forEach((cancion: any) => {
            const div = document.createElement('div');
            div.className = 'item-resultado';
            
            // Reemplazamos 100x100 por una portada más grande si está disponible
            const imgUrl = cancion.artworkUrl100; 
            
            div.innerHTML = `
                <img src="${imgUrl}" alt="Cover">
                <div class="item-info">
                    <p>${cancion.trackName}</p>
                    <span class="res-artista">${cancion.artistName}</span>
                </div>
                <button class="btn-add-mini">+</button>
            `;

            const btnAdd = div.querySelector('.btn-add-mini') as HTMLButtonElement;
            btnAdd.onclick = () => {
                procesarIngresoCancion(cancion.trackName, cancion.artistName, cancion.previewUrl, imgUrl);
                contenedorResultados.innerHTML = "<p style='font-size:0.8em; color:green;'>¡Agregada!</p>";
                inputBusqueda.value = "";
            };

            contenedorResultados.appendChild(div);
        });

    } catch (error) {
        contenedorResultados.innerHTML = "<p style='font-size:0.8em; color:red;'>Error al buscar.</p>";
    }
});

// --- SUBIR ARCHIVO LOCAL ---
document.getElementById('btn-agregar-local')?.addEventListener('click', () => {
    const inputTitulo = document.getElementById('input-titulo-local') as HTMLInputElement;
    const inputArtista = document.getElementById('input-artista-local') as HTMLInputElement;
    const inputArchivo = document.getElementById('input-archivo') as HTMLInputElement;

    if (!inputTitulo.value || !inputArtista.value || !inputArchivo.files || inputArchivo.files.length === 0) {
        alert("Completa todos los campos locales y selecciona un archivo .mp3"); return;
    }

    const archivo = inputArchivo.files[0];
    const urlLocal = URL.createObjectURL(archivo);

    procesarIngresoCancion(inputTitulo.value, inputArtista.value, urlLocal, portadaPorDefecto);
    
    // Limpiar campos
    inputTitulo.value = ''; inputArtista.value = ''; inputArchivo.value = '';
});

// --- REPRODUCTOR AUDIO ---
// Define los iconos en formato SVG
const iconPlay = `<svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>`;
const iconPause = `<svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>`;

// Actualiza la función cargarCancionEnReproductor
function cargarCancionEnReproductor(autoPlay: boolean = false) {
    if (miPlaylist.cancionActual) {
        if(reproductorAudio.src !== miPlaylist.cancionActual.urlAudio) {
            reproductorAudio.src = miPlaylist.cancionActual.urlAudio;
        }
        txtTituloActual.innerText = miPlaylist.cancionActual.titulo;
        txtArtistaActual.innerText = miPlaylist.cancionActual.artista;
        imgPortadaActual.src = miPlaylist.cancionActual.portada;
        
        if (autoPlay) {
            reproductorAudio.play();
            reproduciendo = true;
            btnPlayPause.innerHTML = iconPause;
            btnPlayPause.classList.add('reproduciendo'); // Pone el botón verde
        }
    } else {
        txtTituloActual.innerText = "Sin reproducir";
        txtArtistaActual.innerText = "Selecciona una canción";
        imgPortadaActual.src = portadaPorDefecto;
        reproductorAudio.pause();
        reproductorAudio.src = "";
        btnPlayPause.innerHTML = iconPlay;
        btnPlayPause.classList.remove('reproduciendo');
    }
}

// Botones de control
btnPlayPause.addEventListener('click', () => {
    if (!miPlaylist.cancionActual) return;
    
    if (reproduciendo) {
        reproductorAudio.pause(); 
        reproduciendo = false; 
        btnPlayPause.innerHTML = iconPlay;
        btnPlayPause.classList.remove('reproduciendo'); // Quita el verde
    } else {
        reproductorAudio.play(); 
        reproduciendo = true; 
        btnPlayPause.innerHTML = iconPause;
        btnPlayPause.classList.add('reproduciendo'); // Pone el verde
    }
});

document.getElementById('btn-parar')?.addEventListener('click', () => {
    reproductorAudio.pause(); 
    reproductorAudio.currentTime = 0;
    reproduciendo = false; 
    btnPlayPause.innerHTML = iconPlay;
    btnPlayPause.classList.remove('reproduciendo');
});

document.getElementById('btn-adelantar')?.addEventListener('click', () => {
    if (miPlaylist.siguienteCancion()) { cargarCancionEnReproductor(true); actualizarUI(); }
});

document.getElementById('btn-retroceder')?.addEventListener('click', () => {
    if (miPlaylist.anteriorCancion()) { cargarCancionEnReproductor(true); actualizarUI(); }
});

reproductorAudio.addEventListener('ended', () => {
    if (miPlaylist.siguienteCancion()) { 
        cargarCancionEnReproductor(true); 
        actualizarUI(); 
    } else { 
        reproduciendo = false; 
        btnPlayPause.innerHTML = iconPlay;
        btnPlayPause.classList.remove('reproduciendo');
    }
});

// Barra Progreso y Tiempo
const tiempoActualTxt = document.getElementById('tiempo-actual') as HTMLSpanElement;
const tiempoTotalTxt = document.getElementById('tiempo-total') as HTMLSpanElement;

function formateaTiempo(segs: number) {
    if (isNaN(segs)) return "0:00";
    const m = Math.floor(segs / 60); const s = Math.floor(segs % 60);
    return `${m}:${s < 10 ? '0' : ''}${s}`;
}

reproductorAudio.addEventListener('timeupdate', () => {
    if (reproductorAudio.duration) {
        barraProgreso.value = ((reproductorAudio.currentTime / reproductorAudio.duration) * 100).toString();
        tiempoActualTxt.innerText = formateaTiempo(reproductorAudio.currentTime);
        tiempoTotalTxt.innerText = formateaTiempo(reproductorAudio.duration);
    }
});

barraProgreso.addEventListener('input', () => {
    if (reproductorAudio.duration) {
        reproductorAudio.currentTime = (parseFloat(barraProgreso.value) / 100) * reproductorAudio.duration;
    }
});

document.getElementById('barra-volumen')?.addEventListener('input', (e) => {
    reproductorAudio.volume = parseInt((e.target as HTMLInputElement).value) / 100;
});