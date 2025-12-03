async function fetchGuests() {
  const res = await fetch('/api/guests');
  const data = await res.json();
  const tbody = document.querySelector('#guests-table tbody');
  tbody.innerHTML = '';
  data.forEach(g => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${g.name}</td>
      <td>${g.email}</td>
      <td>${g.category || ''}</td>
      <td>${g.event_id || ''}</td>
      <td><button data-id="${g.id}" class="btn btn-delete">Delete</button></td>`;
    tbody.appendChild(tr);
  });
}

document.getElementById('guest-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    name: document.getElementById('g-name').value,
    email: document.getElementById('g-email').value,
    category: document.getElementById('g-category').value,
    event_id: parseInt(document.getElementById('g-event').value || '0') || null
  };
  await fetch('/api/guests', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  });
  e.target.reset();
  fetchGuests();
});

document.querySelector('#guests-table').addEventListener('click', async (e) => {
  if (e.target.classList.contains('btn-delete')) {
    const id = e.target.getAttribute('data-id');
    await fetch(`/api/guests/${id}`, {method: 'DELETE'});
    fetchGuests();
  }
});

fetchGuests();
