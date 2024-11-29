
// For Navigation Bar //
window.addEventListener('scroll', function(){
    const nav = document.querySelector('.container');
    const links = nav.querySelectorAll('a');
    const coupleSearchTop = document.querySelector('.couple-search-top');
    if (window.scrollY > 20){
        nav.style.backgroundColor = '#EFF0F1';
        nav.classList.add('scrolled');
    }
    else{
        nav.style.backgroundColor = 'transparent';
        nav.classList.remove('scrolled');
    }
});


// Recommend position items//
document.addEventListener('DOMContentLoaded', function(){
    const container = document.getElementById('recommend-card');
    const items = container.children;
    if (items.length < 5){
        container.classList.add('start');
    }
    else{
        container.classList.add('space-between');
    }
});
