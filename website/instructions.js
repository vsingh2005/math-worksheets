/* =========================================================
   KIDS STEM STUDIO - INSTRUCTIONS MODULE
   Dedicated script for instructions.html
   ========================================================= */

window.addEventListener('DOMContentLoaded', () => {
  AuthManager.requireAuth();
  AuthManager.updateHeaderUI();

  // If no track is stored in session, default to 7-8
  if (!sessionStorage.getItem('selectedTrack')) {
    sessionStorage.setItem('selectedTrack', '7-8');
  }
});

function openModal(id) {
  const el = document.getElementById(id);
  if (el) {
    el.classList.remove('hidden');
    el.classList.add('flex');
  }
}

function closeModal(id) {
  const el = document.getElementById(id);
  if (el) {
    el.classList.add('hidden');
    el.classList.remove('flex');
  }
}
