/* =========================================================
   KIDS STEM STUDIO - RESULTS & BREAKDOWN MODULE
   Dedicated script for results.html
   ========================================================= */

// Results State
let state = {
  score: 0,
  timeElapsed: 0,
  recommendedLevel: '7th Grade Standard Math',
  answerBreakdown: [],
  activeReviewFilter: 'all'
};

// HTML tag helpers to bypass WordPress/WAF filters
const _t = name => '<' + name;
const _c = name => '</' + name + '>';

window.addEventListener('DOMContentLoaded', () => {
  AuthManager.requireAuth();
  AuthManager.updateHeaderUI();

  const lastResult = JSON.parse(sessionStorage.getItem('lastExamResult'));
  if (lastResult) {
    state.answerBreakdown = lastResult.answerBreakdown || [];
    state.score = lastResult.score || 0;
    state.recommendedLevel = lastResult.recommendedLevel || '7th Grade Standard Math';
    state.timeElapsed = lastResult.timeElapsed || 0;

    const recEl = document.getElementById("placement-recommendation");
    if (recEl) recEl.innerText = state.recommendedLevel;

    const scoreEl = document.getElementById("score-details");
    if (scoreEl) scoreEl.innerText = `You answered ${state.score} out of 15 questions correctly.`;

    const minutes = Math.floor(state.timeElapsed / 60);
    const seconds = state.timeElapsed % 60;
    const timeEl = document.getElementById("time-details");
    if (timeEl) {
      timeEl.innerText = `Time elapsed: ${minutes} minute${minutes !== 1 ? 's' : ''} and ${seconds} second${seconds !== 1 ? 's' : ''}.`;
    }

    const userStatus = document.getElementById("user-save-status");
    if (userStatus && AuthManager.currentUser) {
      userStatus.innerText = `Math assessment linked to active student account: ${AuthManager.currentUser.username}`;
    }

    renderFluidBreakdown();
    triggerConfetti();
  } else {
    // If no recent exam result found, return safely to portal
    window.location.href = 'portal.html';
  }
});

function triggerConfetti() {
  const container = document.getElementById("confetti-container");
  if (!container) return;
  container.innerHTML = "";
  container.style.opacity = "1";
  container.style.transition = "opacity 1s ease";

  const colors = ["#4DA8FF", "#5ECF7A", "#FFD75E", "#FF8B6A"];
  for (let i = 0; i < 80; i++) {
    const confetti = document.createElement("div");
    confetti.classList.add("confetti");
    confetti.style.left = `${Math.random() * 100}vw`;
    confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    confetti.style.animationDelay = `${Math.random() * 2}s`;
    confetti.style.animationDuration = `${2 + Math.random() * 3}s`;
    container.appendChild(confetti);
  }

  setTimeout(() => {
    container.style.opacity = "0";
    setTimeout(() => {
      container.innerHTML = "";
    }, 1000);
  }, 5000);
}

function filterReview(type) {
  state.activeReviewFilter = type;
  renderFluidBreakdown();
}

function renderFluidBreakdown() {
  const container = document.getElementById('fluid-question-breakdown');
  if (!container || !state.answerBreakdown) return;

  const totalCount = state.answerBreakdown.length;
  const incorrectCount = state.answerBreakdown.filter(i => !i.isCorrect).length;
  const correctCount = state.answerBreakdown.filter(i => i.isCorrect).length;

  const btnAll = document.getElementById('filter-btn-all');
  const btnInc = document.getElementById('filter-btn-incorrect');
  const btnCor = document.getElementById('filter-btn-correct');

  if (btnAll) {
    btnAll.innerText = `All (${totalCount})`;
    btnAll.className = state.activeReviewFilter === 'all' 
      ? "px-4 py-2 text-xs font-extrabold rounded-lg bg-white text-navy-dark shadow-sm hover:!bg-white hover:!text-navy-dark" 
      : "px-4 py-2 text-xs font-extrabold rounded-lg text-slate-500 hover:!bg-white/50 hover:!text-slate-700";
  }
  if (btnInc) {
    btnInc.innerText = `Incorrect (${incorrectCount})`;
    btnInc.className = state.activeReviewFilter === 'incorrect' 
      ? "px-4 py-2 text-xs font-extrabold rounded-lg bg-white text-rose-600 shadow-sm hover:!bg-white hover:!text-rose-600" 
      : "px-4 py-2 text-xs font-extrabold rounded-lg text-rose-600 hover:!bg-white/50 hover:!text-rose-700";
  }
  if (btnCor) {
    btnCor.innerText = `Correct (${correctCount})`;
    btnCor.className = state.activeReviewFilter === 'correct' 
      ? "px-4 py-2 text-xs font-extrabold rounded-lg bg-white text-emerald-600 shadow-sm hover:!bg-white hover:!text-emerald-600" 
      : "px-4 py-2 text-xs font-extrabold rounded-lg text-emerald-600 hover:!bg-white/50 hover:!text-emerald-700";
  }

  let items = state.answerBreakdown;
  if (state.activeReviewFilter === 'incorrect') {
    items = items.filter(i => !i.isCorrect);
  } else if (state.activeReviewFilter === 'correct') {
    items = items.filter(i => i.isCorrect);
  }

  if (items.length === 0) {
    container.innerHTML = `
      ${_t('div')} class="text-center py-6 bg-slate-50 rounded-xl border border-slate-200">
        <p class="text-sm font-bold text-slate-500">No math questions match this filter selection.</p>
      ${_c('div')}
    `;
    return;
  }

  let html = "";
  items.forEach((item) => {
    const isCorrect = item.isCorrect;
    const borderClass = isCorrect ? "correct-card" : "incorrect-card";
    const statusBadge = isCorrect
      ? `<span class="px-2.5 py-1 text-xs font-extrabold rounded-full bg-emerald-100 text-emerald-800">Correct ✓</span>`
      : `<span class="px-2.5 py-1 text-xs font-extrabold rounded-full bg-rose-100 text-rose-800">Incorrect ✗</span>`;

    html += `
      ${_t('div')} class="bg-white p-6 rounded-2xl review-card ${borderClass} space-y-4 shadow-sm">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <div class="flex items-center space-x-2">
            <span class="font-extrabold text-navy-dark text-sm">Question ${item.questionIndex}</span>
            <span class="px-2.5 py-0.5 text-xs font-bold text-sky-600 bg-sky-50 rounded-full">${item.domain} (Grade ${item.grade})</span>
          </div>
          ${statusBadge}
        </div>

        <h4 class="text-base font-bold text-slate-800 leading-snug">${item.text}</h4>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-2 text-xs font-bold">
          <div class="p-3 rounded-xl ${isCorrect ? 'bg-emerald-50 border border-emerald-200 text-emerald-900' : 'bg-rose-50 border border-rose-200 text-rose-900'}">
            <span class="text-slate-400 block uppercase text-[10px] tracking-wider mb-0.5">Your Answer</span>
            <span class="text-sm">${item.userAnswerText}</span>
          </div>
          <div class="p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-900">
            <span class="text-emerald-600 block uppercase text-[10px] tracking-wider mb-0.5">Correct Answer</span>
            <span class="text-sm font-extrabold">${item.correctAnswerText}</span>
          </div>
        </div>

        <div class="explanation-box">
          <span class="text-xs font-extrabold text-slate-500 uppercase tracking-wider block mb-1 flex items-center gap-1">
            <span>💡</span> Step-by-Step Math Solution
          </span>
          <p class="text-xs md:text-sm text-slate-700 font-medium leading-relaxed">${item.explanation}</p>
        </div>
      ${_c('div')}
    `;
  });

  container.innerHTML = html;
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
