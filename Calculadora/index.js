const displayValorAnterior = document.getElementById('valor-anterior');
const displayValorActual = document.getElementById('valor-actual');
const botonesNumeros = document.querySelectorAll('.numero');
const botonesOperadores = document.querySelectorAll('.operador');
const historia = document.getElementById('history');
const igualar = document.getElementById('igualar');
const display = new Display(displayValorAnterior, displayValorActual);

botonesNumeros.forEach(boton=>{
    boton.addEventListener('click', () => {display.agregarNumero(boton.innerHTML)});
});

botonesOperadores.forEach(boton=>{
    boton.addEventListener('click', ()=> display.computar(boton.value)
    )
})

igualar.addEventListener('click', function(){
    var histo = document.createElement('p');
    histo.classList.add('paragraph-styling');
    histo.innerText = displayValorAnterior.innerHTML;
    historia.appendChild(histo);
    histo.addEventListener('click',()=>{
        displayValorActual.innerText = histo.innerHTML;
    })
    histo.addEventListener('dblclick',()=>{
        histo.style.textDecoration = "line-through";
    })
        localStorage.setItem("operacion", JSON.stringify(histo.innerHTML));
    }    
)