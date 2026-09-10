const serviceForm = document.querySelector("#serviceForm");
const formStatus = document.querySelector("#formStatus");

serviceForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(serviceForm);
  const name = String(formData.get("name") || "").trim();
  const service = String(formData.get("service") || "").trim();

  formStatus.textContent = `Thanks, ${name}. Your ${service.toLowerCase()} request is ready to send.`;
  serviceForm.reset();
});
