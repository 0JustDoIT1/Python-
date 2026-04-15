const navbarCollapse = document.getElementById("navbarNav");
const toggler = document.querySelector(".navbar-toggler");

const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
  toggle: false,
});

document.addEventListener("click", (e) => {
  const isMenuClick = e.target.closest(".nav-item");
  const isInside =
    navbarCollapse.contains(e.target) || toggler.contains(e.target);

  if (isMenuClick) {
    bsCollapse.hide();
    return;
  }

  if (!isInside && navbarCollapse.classList.contains("show")) {
    bsCollapse.hide();
  }
});

const webBtn = document.getElementById("webBtn");
const appBtn = document.getElementById("appBtn");

const webCarousel = document.getElementById("webCarouselWrapper");
const appCarousel = document.getElementById("appCarouselWrapper");

const webInstance = bootstrap.Carousel.getOrCreateInstance(
  document.getElementById("webCarousel"),
);

const appInstance = bootstrap.Carousel.getOrCreateInstance(
  document.getElementById("appCarousel"),
);

function showWeb() {
  webCarousel.classList.remove("d-none");
  appCarousel.classList.add("d-none");

  webBtn.classList.add("active");
  appBtn.classList.remove("active");

  const slider = document.querySelector(".tab-slider");
  if (slider) slider.style.transform = "translateX(0%)";

  webInstance.to(0);
}

function showApp() {
  appCarousel.classList.remove("d-none");
  webCarousel.classList.add("d-none");

  appBtn.classList.add("active");
  webBtn.classList.remove("active");

  const slider = document.querySelector(".tab-slider");
  if (slider) slider.style.transform = "translateX(100%)";

  appInstance.to(0);
}

webBtn.addEventListener("click", showWeb);
appBtn.addEventListener("click", showApp);

const skills = [
  { name: "TypeScript", type: "language" },
  { name: "Python", type: "language" },
  { name: "JavaScript", type: "language" },

  { name: "HTML5", type: "frontend" },
  { name: "CSS3", type: "frontend" },
  { name: "React", type: "frontend" },
  { name: "Next.js", type: "frontend" },
  { name: "React Native", type: "frontend" },
  { name: "TailwindCSS", type: "frontend" },

  { name: "Node.js", type: "backend" },
  { name: "NestJS", type: "backend" },

  { name: "MongoDB", type: "database" },
  { name: "SQLite", type: "database" },
  { name: "Firebase", type: "database" },
  { name: "Amazon S3", type: "database" },

  { name: "GitHub", type: "tools" },
];

const skillContainer = document.getElementById("skillTags");

function renderSkills() {
  if (!skillContainer) return;

  skillContainer.innerHTML = skills
    .map(
      (skill) => `
      <span class="skill-tag ${skill.type}">
        ${skill.name}
      </span>
    `,
    )
    .join("");
}

renderSkills();

document.getElementById("emailCard").addEventListener("click", () => {
  window.location.href = "mailto:hbc3869@gmail.com";
});

document.getElementById("phoneCard").addEventListener("click", () => {
  window.location.href = "tel:01090309615";
});
