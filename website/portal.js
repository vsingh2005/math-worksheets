/* =========================================================
   KIDS STEM STUDIO - PORTAL DASHBOARD MODULE
   Dedicated script for portal.html
   ========================================================= */

window.addEventListener('DOMContentLoaded', () => {
  AuthManager.requireAuth();
  AuthManager.updateHeaderUI();
});

function showTrackSelection() {
  const main = document.getElementById('landing-main-content');
  const panel = document.getElementById('track-selection-panel');
  if (main) main.classList.add('hidden');
  if (panel) panel.classList.remove('hidden');
}

function showLandingMain() {
  const main = document.getElementById('landing-main-content');
  const panel = document.getElementById('track-selection-panel');
  if (main) main.classList.remove('hidden');
  if (panel) panel.classList.add('hidden');
}

function selectTrack(track) {
  sessionStorage.setItem('selectedTrack', track);
  window.location.href = 'instructions.html';
}

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
