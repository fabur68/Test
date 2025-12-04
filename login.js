async function doLogin(e) {
  e.preventDefault();
  const payload = {
    email: document.getElementById('email').value,
    password: document.getElementById('password').value,
    otp: document.getElementById('otp').value
  };
  const res = await fetch('/api/login', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  });
  const msgDiv = document.getElementById('login-msg');
  if (res.ok) {
    msgDiv.textContent = 'Login successful';
    window.location.href = 'index.html';
  } else {
    const data = await res.json();
    msgDiv.textContent = data.error || 'Login failed';
  }
}

document.getElementById('login-form').addEventListener('submit', doLogin);

async function doRegister(e) {
  e.preventDefault();
  const payload = {
    email: document.getElementById('reg-email').value,
    password: document.getElementById('reg-password').value,
    role: document.getElementById('reg-role').value
  };
  const res = await fetch('/api/register', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload)
  });
  const msgDiv = document.getElementById('register-msg');
  if (res.ok) {
    msgDiv.textContent = 'Registration successful';
  } else {
    const data = await res.json();
    msgDiv.textContent = data.error || 'Registration failed';
  }
}

document.getElementById('register-form').addEventListener('submit', doRegister);
