async function loadSummary() {
  const res = await fetch('/api/analytics');
  const data = await res.json();
  const div = document.getElementById('summary');
  div.innerHTML = `<p><strong>Events:</strong> ${data.events}</p>` +
                  `<p><strong>Guests:</strong> ${data.guests}</p>`;
}

loadSummary();
