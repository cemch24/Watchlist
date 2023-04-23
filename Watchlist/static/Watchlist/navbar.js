// Get the navbar element
const navbar = document.querySelector('.navbar');

// Get the navbar toggler element
const navbarToggler = document.querySelector('.navbar-toggler');

// Get the navbar collapse element
const navbarCollapse = document.querySelector('.navbar-collapse');

// Add event listener to navbar toggler element
navbarToggler.addEventListener('click', function() {
    // Toggle the 'show' class on the navbar collapse element
    navbarCollapse.classList.toggle('show');
});
