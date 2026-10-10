/* =========================================================
   KIDS STEM STUDIO - EXAM ENGINE MODULE
   Dedicated script for exam.html
   ========================================================= */

// App State
let state = {
  currentStep: 3,
  currentQuestionIndex: 0,
  activeDifficulty: 7, // Default medium grade
  userAnswers: {},
  questionsServed: [],
  score: 0,
  timeElapsed: 0,
  timerInterval: null,
  isExiting: false,
  selectedTrack: '7-8',
  pendingNavigationUrl: null,
  pendingNavigationTarget: null
};

// HTML tag helpers to bypass WordPress/WAF filters
const _t = name => '<' + name;
const _c = name => '</' + name + '>';

// Initialize exam on page load
window.addEventListener('DOMContentLoaded', () => {
  AuthManager.requireAuth();
  AuthManager.updateHeaderUI();

  const track = sessionStorage.getItem('selectedTrack') || '7-8';
  selectTrack(track);
  startExam();
});

function selectTrack(track) {
  state.selectedTrack = track;
}

async function loadQuestionBankFromWordPress() {
  try {
    const res = await fetch('/wp-json/kss-math/v1/questions');
    if (res.ok) {
      const data = await res.json();
      if (Array.isArray(data) && data.length > 0) {
        questions = data;
        console.log('Successfully loaded custom question bank from WordPress admin panel:', questions.length);
      }
    }
  } catch (e) {
    console.log('Using default local question bank.');
  }
}

async function startExam() {
  await loadQuestionBankFromWordPress();
  state.currentStep = 3;
  state.currentQuestionIndex = 0;
  state.userAnswers = {};
  state.timeElapsed = 0;

  // Initialize starting difficulty based on chosen track
  let minGrade = 7;
  if (state.selectedTrack === '3-4') {
    minGrade = 3;
  } else if (state.selectedTrack === '5-6') {
    minGrade = 5;
  }
  state.activeDifficulty = minGrade;

  state.questionsServed = [];
  serveNextQuestion(state.activeDifficulty);

  renderQuestion();
  startTimer();
}

function startTimer() {
  if (state.timerInterval) clearInterval(state.timerInterval);
  state.timerInterval = setInterval(() => {
    state.timeElapsed++;
    const minutes = Math.floor(state.timeElapsed / 60);
    const seconds = state.timeElapsed % 60;
    const timeString = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    const timerEl = document.getElementById("timer-display");
    if (timerEl) {
      timerEl.innerText = `Time: ${timeString}`;
    }
  }, 1000);
}

function stopTimer() {
  if (state.timerInterval) clearInterval(state.timerInterval);
}

function serveNextQuestion(difficulty) {
  if (state.questionsServed.length >= 15) return;
  const servedIds = state.questionsServed.map(q => q.id);
  const pool = questions.filter(q => q.grade === difficulty && !servedIds.includes(q.id));

  if (pool.length > 0) {
    const nextQ = pool[Math.floor(Math.random() * pool.length)];
    state.questionsServed.push(nextQ);
  } else {
    const fallbackPool = questions.filter(q => !servedIds.includes(q.id));
    if (fallbackPool.length > 0) {
      const nextQ = fallbackPool[Math.floor(Math.random() * fallbackPool.length)];
      state.questionsServed.push(nextQ);
    } else {
      finishExam();
    }
  }
}

function renderQuestion() {
  const container = document.getElementById("question-container");
  if (!container) return;

  const currentQ = state.questionsServed[state.currentQuestionIndex];
  if (!currentQ) return;

  const qNumDisplay = document.getElementById("question-number-display");
  if (qNumDisplay) {
    qNumDisplay.innerText = `Question ${state.currentQuestionIndex + 1} of 15`;
  }

  const progressPercent = ((state.currentQuestionIndex + 1) / 15) * 100;
  const progressBarFill = document.getElementById("progress-bar-fill");
  if (progressBarFill) {
    progressBarFill.style.width = `${progressPercent}%`;
  }

  let htmlContent = `
    ${_t('div')} class="mb-6">
      <span class="px-3 py-1 text-xs font-bold text-sky-600 bg-sky-50 rounded-full">${currentQ.domain} (Grade ${currentQ.grade})</span>
      <h2 class="text-xl font-bold text-slate-800 mt-4 leading-relaxed">${currentQ.text}</h2>
    ${_c('div')}
  `;

  if (currentQ.type === "multiple-choice") {
    htmlContent += `${_t('div')} class="space-y-4">`;
    currentQ.options.forEach((opt, idx) => {
      const isSelected = state.userAnswers[state.currentQuestionIndex] === idx;
      const optionClass = isSelected
        ? "border-sky-500 bg-sky-50 ring-2 ring-sky-500/20"
        : "border-slate-100 hover:bg-slate-50";

      htmlContent += `
        ${_t('button')} onclick="selectOption(${idx})" class="w-full text-left p-4 rounded-xl border-2 ${optionClass} transition-all duration-200 focus:outline-none flex items-center justify-between">
          <span class="text-slate-700 font-semibold">${opt.text}</span>
          <span class="w-5 h-5 rounded-full border-2 flex items-center justify-center ${isSelected ? 'border-sky-500 bg-sky-500 text-white' : 'border-slate-300'}">
            ${isSelected ? '✓' : ''}
          </span>
        ${_c('button')}
      `;
    });
    htmlContent += `${_c('div')}`;
  } else if (currentQ.type === "numeric-response") {
    const currentVal = state.userAnswers[state.currentQuestionIndex] || "";
    htmlContent += `
      ${_t('div')} class="mt-4">
        <input type="text" id="numeric-input" oninput="saveNumericAnswer(this.value)" value="${currentVal}" placeholder="${currentQ.placeholder || 'Enter your numerical answer...'}" class="w-full p-4 rounded-xl border-2 border-slate-200 focus:border-sky-500 focus:outline-none text-lg text-slate-800 font-bold transition-all duration-200">
      ${_c('div')}
    `;
  }

  container.innerHTML = htmlContent;
  renderSidebar();
}

function selectOption(idx) {
  state.userAnswers[state.currentQuestionIndex] = idx;
  renderQuestion();
}

function saveNumericAnswer(val) {
  state.userAnswers[state.currentQuestionIndex] = val;
}

function renderSidebar() {
  const container = document.getElementById("sidebar-questions");
  if (!container) return;

  let html = "";
  for (let i = 0; i < 15; i++) {
    const isCurrent = i === state.currentQuestionIndex;
    const isAnswered = state.userAnswers[i] !== undefined && String(state.userAnswers[i]).trim() !== "";
    const isServed = i < state.questionsServed.length;

    let btnClass = "bg-slate-100 text-slate-400";
    let isDisabled = false;

    if (isCurrent) {
      btnClass = "bg-sky-500 text-white ring-4 ring-sky-500/20";
    } else if (isAnswered) {
      btnClass = "bg-emerald-500 text-white";
    } else if (isServed) {
      btnClass = "bg-slate-100 text-slate-700";
    } else {
      btnClass = "bg-slate-50 text-slate-300 cursor-not-allowed opacity-50";
      isDisabled = true;
    }

    html += `
      ${_t('button')} onclick="jumpToQuestion(${i})" ${isDisabled ? 'disabled' : ''} class="w-10 h-10 rounded-full font-bold flex items-center justify-center transition-all duration-200 ${btnClass}">
        ${i + 1}
      ${_c('button')}
    `;
  }
  container.innerHTML = html;
}

function jumpToQuestion(idx) {
  if (idx < state.questionsServed.length) {
    state.currentQuestionIndex = idx;
    renderQuestion();
  }
}

function nextQuestion() {
  const currentQ = state.questionsServed[state.currentQuestionIndex];
  const userAns = state.userAnswers[state.currentQuestionIndex];

  if (userAns === undefined || String(userAns).trim() === "") {
    openModal('answer-required-modal');
    return;
  }

  let isCorrect = false;
  if (currentQ.type === "multiple-choice") {
    isCorrect = currentQ.options[userAns] && currentQ.options[userAns].correct;
  } else if (currentQ.type === "numeric-response") {
    isCorrect = String(userAns).trim().toLowerCase() === currentQ.correctAnswer.toLowerCase();
  }

  let minGrade = 7;
  let maxGrade = 8;
  if (state.selectedTrack === '3-4') {
    minGrade = 3;
    maxGrade = 4;
  } else if (state.selectedTrack === '5-6') {
    minGrade = 5;
    maxGrade = 6;
  }

  if (isCorrect) {
    if (state.activeDifficulty < maxGrade) state.activeDifficulty++;
  } else {
    if (state.activeDifficulty > minGrade) state.activeDifficulty--;
  }

  if (state.currentQuestionIndex === 14) {
    finishExam();
  } else {
    state.currentQuestionIndex++;
    if (state.currentQuestionIndex >= state.questionsServed.length) {
      serveNextQuestion(state.activeDifficulty);
    }
    renderQuestion();
  }
}

function previousQuestion() {
  if (state.currentQuestionIndex > 0) {
    state.currentQuestionIndex--;
    renderQuestion();
  }
}

function finishExam() {
  stopTimer();

  // Ensure state.questionsServed contains 15 questions even if ended early
  let minGrade = 7;
  let maxGrade = 8;
  if (state.selectedTrack === '3-4') {
    minGrade = 3;
    maxGrade = 4;
  } else if (state.selectedTrack === '5-6') {
    minGrade = 5;
    maxGrade = 6;
  }
  while (state.questionsServed.length < 15) {
    const servedIds = state.questionsServed.map(q => q.id);
    const available = questions.filter(q => (q.grade === minGrade || q.grade === maxGrade) && !servedIds.includes(q.id));
    if (available.length > 0) {
      const nextQ = available[Math.floor(Math.random() * available.length)];
      state.questionsServed.push(nextQ);
    } else {
      break;
    }
  }

  let correctCount = 0;
  const answerBreakdown = [];

  state.questionsServed.forEach((q, idx) => {
    const userAns = state.userAnswers[idx];
    let userAnsText = "No Answer";
    let correctAnsText = "";
    let isCorrect = false;

    if (q.type === "multiple-choice") {
      if (userAns !== undefined && q.options[userAns]) {
        userAnsText = q.options[userAns].text;
        isCorrect = q.options[userAns].correct;
      }
      const correctObj = q.options.find(o => o.correct);
      correctAnsText = correctObj ? correctObj.text : "";
    } else if (q.type === "numeric-response") {
      userAnsText = userAns !== undefined ? String(userAns).trim() : "No Answer";
      correctAnsText = q.correctAnswer;
      isCorrect = userAnsText.toLowerCase() === q.correctAnswer.toLowerCase();
    }

    if (isCorrect) correctCount++;

    answerBreakdown.push({
      questionIndex: idx + 1,
      questionId: q.id,
      grade: q.grade,
      domain: q.domain,
      text: q.text,
      userAnswerText: userAnsText,
      correctAnswerText: correctAnsText,
      isCorrect: isCorrect,
      explanation: q.explanation
    });
  });

  state.score = correctCount;
  state.answerBreakdown = answerBreakdown;

  const getCorrectRatio = (servedList) => {
    if (servedList.length === 0) return 0;
    let correct = 0;
    servedList.forEach(q => {
      const idx = state.questionsServed.indexOf(q);
      const item = answerBreakdown[idx];
      if (item && item.isCorrect) correct++;
    });
    return correct / servedList.length;
  };

  let recommendedLevel = "6th Grade Foundation Math";
  if (state.selectedTrack === '3-4') {
    const grade4Served = state.questionsServed.filter(q => q.grade === 4);
    const g4Ratio = getCorrectRatio(grade4Served);
    if (grade4Served.length >= 3 && g4Ratio >= 0.7) {
      recommendedLevel = "4th Grade Standard Math";
    } else {
      if (state.score >= 10) {
        recommendedLevel = "4th Grade Standard Math";
      } else {
        recommendedLevel = "3rd Grade Foundation Math";
      }
    }
  } else if (state.selectedTrack === '5-6') {
    const grade6Served = state.questionsServed.filter(q => q.grade === 6);
    const g6Ratio = getCorrectRatio(grade6Served);
    if (grade6Served.length >= 3 && g6Ratio >= 0.7) {
      recommendedLevel = "6th Grade Foundation Math";
    } else {
      if (state.score >= 10) {
        recommendedLevel = "6th Grade Foundation Math";
      } else {
        recommendedLevel = "5th Grade Standard Math";
      }
    }
  } else {
    // default 7-8 track
    const grade8Served = state.questionsServed.filter(q => q.grade === 8);
    const grade7Served = state.questionsServed.filter(q => q.grade === 7);
    const g8Ratio = getCorrectRatio(grade8Served);
    const g7Ratio = getCorrectRatio(grade7Served);

    if (grade8Served.length >= 3 && g8Ratio >= 0.7) {
      recommendedLevel = "8th Grade Rigorous Math";
    } else if (grade7Served.length >= 3 && g7Ratio >= 0.7) {
      recommendedLevel = "7th Grade Standard Math";
    } else {
      if (state.score >= 11) {
        recommendedLevel = "8th Grade Rigorous Math";
      } else if (state.score >= 7) {
        recommendedLevel = "7th Grade Standard Math";
      } else {
        recommendedLevel = "6th Grade Foundation Math";
      }
    }
  }

  state.recommendedLevel = recommendedLevel;

  AuthManager.saveExamAttempt({
    score: state.score,
    timeElapsed: state.timeElapsed,
    recommendedLevel: recommendedLevel,
    answers: answerBreakdown
  });

  sessionStorage.setItem('lastExamResult', JSON.stringify({
    score: state.score,
    timeElapsed: state.timeElapsed,
    recommendedLevel: recommendedLevel,
    answerBreakdown: answerBreakdown
  }));

  window.location.href = 'results.html';
}

// Global modal handlers that dynamically inject missing HTML modal layouts on WordPress
const safeOpenModal = function(id) {
  let modal = document.getElementById(id);
  if (!modal && id === 'answer-required-modal') {
    const modalHtml = `
      ${_t('div')} id="answer-required-modal"
        class="fixed inset-0 bg-navy-dark/40 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
        ${_t('div')} class="bg-white max-w-md w-full rounded-2xl p-6 md:p-8 space-y-6 shadow-2xl text-center">
          ${_t('span')} class="text-4xl">📝${_c('span')}
          ${_t('h3')} class="text-2xl font-extrabold text-navy-dark">Answer Required${_c('h3')}
          ${_t('p')} class="text-slate-500 font-semibold leading-relaxed">Please select or enter an answer for the math question before moving on.${_c('p')}
          ${_t('div')} class="flex items-center justify-center pt-2">
            ${_t('button')} onclick="closeModal('answer-required-modal')"
              class="px-8 py-3 bg-sky-500 text-white font-bold rounded-xl hover:bg-sky-600 transition-colors shadow-md shadow-sky-500/20 hover:!bg-sky-600 hover:!text-white">
              OK
            ${_c('button')}
          ${_c('div')}
        ${_c('div')}
      ${_c('div')}
    `;
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = modalHtml;
    const modalNode = tempDiv.firstElementChild;
    document.body.appendChild(modalNode);
    modal = modalNode;
  }
  if (modal) {
    modal.classList.remove('hidden');
    modal.classList.add('flex');
  }
};

const safeCloseModal = function(id) {
  const modal = document.getElementById(id);
  if (modal) {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
  }
};

window.openModal = safeOpenModal;
window.closeModal = safeCloseModal;
try {
  openModal = safeOpenModal;
  closeModal = safeCloseModal;
} catch (e) {
  // Ignore in strict contexts
}

function handleLogoClick() {
  openModal('exit-confirm-modal');
}

function handleExit() {
  state.isExiting = true;
  closeModal('exit-confirm-modal');
  if (state.pendingNavigationUrl) {
    if (state.pendingNavigationTarget === '_blank') {
      window.open(state.pendingNavigationUrl, '_blank');
      state.pendingNavigationUrl = null;
      state.pendingNavigationTarget = null;
    } else {
      window.location.href = state.pendingNavigationUrl;
    }
  } else {
    window.location.href = 'portal.html';
  }
}

// Warn if student attempts to leave mid-exam
window.addEventListener('beforeunload', (e) => {
  if (state.currentStep === 3 && !state.isExiting) {
    e.preventDefault();
    e.returnValue = '';
  }
});

// Intercept navigation links during test
document.addEventListener('click', (e) => {
  const anchor = e.target.closest('a');
  if (anchor && state.currentStep === 3) {
    e.preventDefault();
    state.pendingNavigationUrl = anchor.href;
    state.pendingNavigationTarget = anchor.target;
    openModal('exit-confirm-modal');
  }
});
