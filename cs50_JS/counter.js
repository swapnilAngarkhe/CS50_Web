document.addEventListener('DOMContentLoaded', function(){
    if (!localStorage.getItem('counter')) {
        localStorage.setItem('counter', '0');
    }
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');

    document.querySelector('button').onclick = function() {
        let counter = parseInt(localStorage.getItem('counter'));
        counter++;
        document.querySelector('h1').innerHTML = counter;
        localStorage.setItem('counter', counter.toString());
    };
});
