async function fetchEvents() {
  const res = await fetch('/api/events');
  const data = await res.json();
  const tbody = document.querySelector('#events-table tbody');
  tbody.innerHTML = '';
  for (const id in data) {
    const ev = data[id];
    const tr = document.createElement('tr');
    tr.innerHTML = `<td>${ev.name}</td><td>${ev.date}</td><td>${ev.time}</td>` +
                   `<td>${ev.location}</td><td>${ev.price}</td>` +
                   `<td>${(ev.program || []).join(', ')}</td>` +
                   `<td><button data-id="${id}" class="delete-btn">Delete</button></td>`;
    tbody.appendChild(tr);
  }
}

document.getElementById('event-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    name: document.getElementById('name').value,
    date: document.getElementById('date').value,
    time: document.getElementById('time').value,
    location: document.getElementById('location').value,
    price: parseFloat(document.getElementById('price').value || 0),
    program: document.getElementById('program').value.split(',').map(p => p.trim()).filter(Boolean)
  };
  await fetch('/api/events', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  });
  e.target.reset();
  fetchEvents();
});

document.getElementById('events-table').addEventListener('click', async (e) => {
  if (e.target.classList.contains('delete-btn')) {
    const id = e.target.getAttribute('data-id');
    await fetch(`/api/events/${id}`, {method: 'DELETE'});
    fetchEvents();
  }
});

fetchEvents();
