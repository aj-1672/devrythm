// scroll-effect.js
document.addEventListener("DOMContentLoaded", function () {
  const hero = document.querySelector(".hero");
  const heroHeight = hero.offsetHeight;
  const heroLogo = document.querySelector(".hero-logo");
  const navbar = document.querySelector(".navbar");
  const searchContainer = document.querySelector(".search-container");

  window.addEventListener("scroll", function () {
    const scrollPosition = window.scrollY;

    // Show navbar when search hits top
    if (scrollPosition > heroHeight) {
      navbar.classList.add("visible");

      // Transform search bar
      if (scrollPosition > heroHeight + 50) {
        searchContainer.style.padding = "10px 40px";
        searchContainer.querySelector(".search-bar").style.maxWidth = "200px";
      } else {
        searchContainer.style.padding = "20px 40px";
        searchContainer.querySelector(".search-bar").style.maxWidth = "600px";
      }
    } else {
      navbar.classList.remove("visible");
      searchContainer.style.padding = "20px 40px";
      searchContainer.querySelector(".search-bar").style.maxWidth = "600px";
    }
  });
});
