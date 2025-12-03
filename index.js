async function loadEvents() {
  const res = await fetch('/api/events');
  const events = await res.json();
  const container = document.getElementById('event-tiles');
  container.innerHTML = '';
  events.forEach(ev => {
    const tile = document.createElement('div');
    tile.className = 'tile';
    tile.innerHTML = `<h3>${ev.name}</h3><p>${ev.date} ${ev.time}</p><p>${ev.location}</p>`;
    container.appendChild(tile);
  });
}

function filterEvents() {
  const term = document.getElementById('search').value.toLowerCase();
  document.querySelectorAll('.tile').forEach(tile => {
    tile.style.display = tile.textContent.toLowerCase().includes(term) ? '' : 'none';
  });
}

document.getElementById('search').addEventListener('input', filterEvents);
loadEvents();
