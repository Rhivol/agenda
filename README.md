Acest proiect este un microserviciu Python (Flask) care face scraping pe site-ul [moldinsolv.md](https://moldinsolv.md) pentru a găsi rapid articole sau anunțuri relevante legate de proceduri judiciare, lichidări și faliment.

## 🔍 Ce face

- Primește un cuvânt cheie de la utilizator (ex: `faliment`)
- Caută articole relevante pe moldinsolv.md
- Returnează primele 5 rezultate în format JSON

## 🚀 Exemplu de utilizare

```http
GET https://moldinsolv-scraper.onrender.com/cauta?q=lichidare
