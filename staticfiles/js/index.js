const sectionOverview = document.querySelector(".overview");
const sectionApplication = document.querySelector(".application");

const listOverview = document.querySelector(".list-overview");
const listApplication = document.querySelector(".list-application");

const btnOverview = document.querySelector(".btn-overview");
const btnApplication = document.querySelector(".btn-application");

if (document.URL.includes("application")) {
  hideOverview();
  showApplication();
}

btnOverview.addEventListener("click", () => {
  hideApplication();
  showOverview();
});

btnApplication.addEventListener("click", () => {
  hideOverview();
  showApplication();
});

function showOverview() {
  sectionOverview.classList.remove("d-none");
  listOverview.classList.remove("text-secondary");

  listOverview.classList.add("border-dark");
  listOverview.classList.add("text-dark");
}

function hideOverview() {
  listOverview.classList.remove("border-dark");
  listOverview.classList.remove("text-dark");

  sectionOverview.classList.add("d-none");
  listOverview.classList.add("text-secondary");
}

function showApplication() {
  sectionApplication.classList.remove("d-none");
  listApplication.classList.remove("text-secondary");

  listApplication.classList.add("border-dark");
  listApplication.classList.add("text-dark");
}

function hideApplication() {
  listApplication.classList.remove("border-dark");
  listApplication.classList.remove("text-dark");

  sectionApplication.classList.add("d-none");
  listApplication.classList.add("text-secondary");
}
