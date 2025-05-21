<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <title>Scraper Moldinsolv</title>
  <style>
    body { font-family: Arial; padding: 2em; max-width: 600px; margin: auto; }
    input, button { padding: 0.5em; font-size: 1em; }
    ul { margin-top: 1em; }
    li { margin-bottom: 0.5em; }
  </style>
</head>
<body>
  <h1>Caută pe moldinsolv.md</h1>
  <input type="text" id="search" placeholder="Introdu cuvântul cheie" />
  <button onclick="cauta()">Caută</button>
  <ul id="rezultate"></ul>

  <script>
    async function cauta() {
      const q = document.getElementById("search").value;
      const ul = document.getElementById("rezultate");
      ul.innerHTML = "";

      if (!q) {
        ul.innerHTML = "<li>Introdu un cuvânt cheie.</li>";
        return;
      }

      const res = await fetch(`https://<nume-aplicatie>.onrender.com/cauta?q=${encodeURIComponent(q)}`);
      const data = await res.json();

      if (data.rezultate) {
        data.rezultate.forEach(item => {
          const li = document.createElement("li");
          li.innerHTML = `<a href="${item.url}" target="_blank">${item.titlu}</a>`;
          ul.appendChild(li);
        });
      } else {
        ul.innerHTML = `<li>${data.mesaj || "Eroare la căutare."}</li>`;
      }
    }
  </script>
</body>
</html>
