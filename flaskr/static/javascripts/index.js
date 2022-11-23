const navbarlinks = document.getElementsByClassName("navbar-links")[0];

function hamburgerMenu() {
    const toggleButton = document.getElementsByClassName("toggle-button")[0];    

    toggleButton.addEventListener("click", ()=> {
        navbarlinks.classList.toggle("active");
    })
    
}

function closeHamburgerMenu() {
    const navbarMenu = document.querySelector(".navbar-links").classList;
    const main = document.querySelector("main")
    main.addEventListener("click", ()=> {
        if (navbarMenu.contains("active")) {
            navbarlinks.classList.remove("active");
        }
    });
}

// Run Function
hamburgerMenu();
closeHamburgerMenu();