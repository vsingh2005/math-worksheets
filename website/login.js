/* =========================================================
   KIDS STEM STUDIO - LOGIN MODULE
   Dedicated script for login.html
   ========================================================= */

// Auto-redirect to portal if already authenticated
window.addEventListener('DOMContentLoaded', () => {
  const session = localStorage.getItem('kss_session') || sessionStorage.getItem('kss_session');
  if (session) {
    window.location.href = 'portal.html';
  }
});

function togglePasswordVisibility(inputId, btnEl) {
  const input = document.getElementById(inputId);
  if (!input) return;
  const icon = btnEl ? btnEl.querySelector('.dashicons') : null;
  if (input.type === 'password') {
    input.type = 'text';
    if (icon) {
      icon.classList.remove('dashicons-visibility');
      icon.classList.add('dashicons-hidden');
    }
  } else {
    input.type = 'password';
    if (icon) {
      icon.classList.remove('dashicons-hidden');
      icon.classList.add('dashicons-visibility');
    }
  }
}

function showAuthAlert(msg, type = 'error') {
  const alert = document.getElementById('auth-alert');
  if (!alert) return;
  alert.innerText = msg;
  alert.className = type === 'error'
    ? 'mb-4 p-3 rounded-lg text-xs font-bold text-center bg-rose-100 text-rose-800 border border-rose-200'
    : 'mb-4 p-3 rounded-lg text-xs font-bold text-center bg-emerald-100 text-emerald-800 border border-emerald-200';
  alert.classList.remove('hidden');
}

function switchAuthTab(tab) {
  const loginForm = document.getElementById('loginform');
  const lostForm = document.getElementById('lostpasswordform');
  const navLogin = document.getElementById('nav-login-links');
  const navBack = document.getElementById('nav-back-to-login');
  const alert = document.getElementById('auth-alert');

  if (alert) alert.classList.add('hidden');

  if (tab === 'lostpassword') {
    if (loginForm) loginForm.classList.add('hidden');
    if (lostForm) lostForm.classList.remove('hidden');
    if (navLogin) navLogin.classList.add('hidden');
    if (navBack) navBack.classList.remove('hidden');
  } else {
    if (loginForm) loginForm.classList.remove('hidden');
    if (lostForm) lostForm.classList.add('hidden');
    if (navLogin) navLogin.classList.remove('hidden');
    if (navBack) navBack.classList.add('hidden');
  }
}

async function handleLoginFormSubmit(e) {
  e.preventDefault();
  const loginInput = document.getElementById('user_login').value;
  const passInput = document.getElementById('user_pass').value;
  const rememberMe = document.getElementById('rememberme').checked;
  const submitBtn = document.getElementById('wp-submit');

  try {
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.value = 'Authenticating...';
    }

    await AuthManager.loginUser(loginInput, passInput, rememberMe);
    showAuthAlert('Login successful! Redirecting to portal...', 'success');

    setTimeout(() => {
      window.location.href = 'portal.html';
    }, 500);

  } catch (err) {
    showAuthAlert(err.message || 'Invalid credentials.', 'error');
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.value = 'Log In to Math Portal';
    }
  }
}

function handleLostPasswordSubmit(e) {
  e.preventDefault();
  const input = document.getElementById('user_reset').value.trim();
  if (!input) return;
  showAuthAlert('Password reset instructions sent to ' + input, 'success');
  setTimeout(() => switchAuthTab('login'), 2500);
}
