window.addEventListener('load', ()=> { /* Escuchamos cuando se carga el documento */

      /*cree dos constantes y me guarde los elemebtos que necesitamos */

      const display = document.querySelector('.calculator-display');
      const keypadbuttons = document.getElementsByClassName('keypad-button');

      /*cree otra constante para convertir el HTMLcollection a Array */
      const keypadbuttonsArray = Array.from(keypadbuttons);

      /*Itere por nuestro nuevo array de botones */

      keypadbuttonsArray.forEach( (button) => {

        /*A cada boton le agregue un listener*/
        button.addEventListener('click', ()=> {
            calculadora(button, display);
        })
      })
});

function calculadora(button, display) {
    switch (button.innerHTML) {
    case 'C':
        borrar(display);
        break;

        case '=':
            calcular(display);
            break;

        default:
            actualizar(display, button);
            break;
    }
}

function calcular (display) {
    display.innerHTML = eval(display.innerHTML) /*tomar el string, resorverlo y guardarlo en el innerHTML del display*/
}

function actualizar(display, button){
    if (display.innerHTML == 0) {
        display.innerHTML = '';
    }
    display.innerHTML += button.innerHTML;
}

function borrar(display) {
    display.innerHTML = 0;
}