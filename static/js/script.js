// ---------------> SCROLL - BAR <---------------
{
  const body = document.body;
  let lastScroll = 0;

  window.addEventListener("scroll", () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll <= 0) {
      body.classList.remove("scroll-up");
    }

    if (currentScroll > lastScroll && !body.classList.contains("scroll-down")) {
      body.classList.remove("scroll-up");
      body.classList.add("scroll-down");
    }

    if (currentScroll < lastScroll && body.classList.contains("scroll-down")) {
      body.classList.remove("scroll-down");
      body.classList.add("scroll-up");
    }

    lastScroll = currentScroll;
  });
}

// ---------------> TOGGLE - NAV <---------------
{
  const btnToggle = document.querySelector(".btn-toggle_nav");
  const navMenu = document.querySelector(".nav-menu");

  btnToggle.addEventListener("click", () => {
    btnToggle.classList.toggle("active")
    navMenu.classList.toggle("active")
  })

  document.querySelectorAll(".nav-link").forEach(n => {
    n.addEventListener("click", () => {
      btnToggle.classList.remove("active")
      navMenu.classList.remove("active")
    })
  })
}