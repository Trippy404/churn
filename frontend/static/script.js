document.getElementById("form").onsubmit = async (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);

  const res = await fetch("http://127.0.0.1:8000/api/run", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
};
