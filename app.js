const questions = [
  // --- GRADE 6 (EASY) ---
  {
    id: 1,
    grade: 6,
    domain: "Ratios & Rates",
    text: "A classroom has 8 boys and 12 girls. What is the ratio of boys to girls in simplest form?",
    type: "multiple-choice",
    options: [
      { text: "8:12", correct: false },
      { text: "2:3", correct: true },
      { text: "3:2", correct: false },
      { text: "4:6", correct: false }
    ]
  },
  {
    id: 2,
    grade: 6,
    domain: "Algebraic Expressions",
    text: "Evaluate the expression: x² - y² when x = 4 and y = 3.",
    type: "multiple-choice",
    options: [
      { text: "1", correct: false },
      { text: "7", correct: true },
      { text: "25", correct: false },
      { text: "14", correct: false }
    ]
  },
  {
    id: 3,
    grade: 6,
    domain: "Coordinate Geometry",
    text: "Determine the distance between Point A(2, 5) and Point B(9, 5) on a grid map.",
    type: "multiple-choice",
    options: [
      { text: "5 units", correct: false },
      { text: "7 units", correct: true },
      { text: "11 units", correct: false },
      { text: "9 units", correct: false }
    ]
  },
  {
    id: 4,
    grade: 6,
    domain: "Measurement Conversions",
    text: "Convert 48 ounces into pounds. (1 pound = 16 ounces)",
    type: "numeric-response",
    correctAnswer: "3",
    placeholder: "Enter weight in pounds..."
  },
  {
    id: 13,
    grade: 6,
    domain: "Fractions",
    text: "Simplify the fraction 24/36 to its lowest terms.",
    type: "multiple-choice",
    options: [
      { text: "12/18", correct: false },
      { text: "2/3", correct: true },
      { text: "3/4", correct: false },
      { text: "4/6", correct: false }
    ]
  },
  {
    id: 14,
    grade: 6,
    domain: "Percentages",
    text: "What is 15% of 80?",
    type: "multiple-choice",
    options: [
      { text: "12", correct: true },
      { text: "10", correct: false },
      { text: "15", correct: false },
      { text: "8", correct: false }
    ]
  },
  {
    id: 19,
    grade: 6,
    domain: "Negative Numbers",
    text: "Which of the following numbers has the greatest absolute value?",
    type: "multiple-choice",
    options: [
      { text: "-12", correct: true },
      { text: "8", correct: false },
      { text: "-3", correct: false },
      { text: "0", correct: false }
    ]
  },
  {
    id: 20,
    grade: 6,
    domain: "Basic Equations",
    text: "Solve for x: x + 15.4 = 20",
    type: "numeric-response",
    correctAnswer: "4.6",
    placeholder: "Enter value of x..."
  },
  {
    id: 21,
    grade: 6,
    domain: "Data & Statistics",
    text: "Find the mean of the numbers: 5, 8, 12, 15.",
    type: "numeric-response",
    correctAnswer: "10",
    placeholder: "Enter the average..."
  },
  {
    id: 22,
    grade: 6,
    domain: "Area of Triangles",
    text: "Find the area of a triangle with a base of 6 cm and a height of 5 cm.",
    type: "numeric-response",
    correctAnswer: "15",
    placeholder: "Enter area in square cm..."
  },
  {
    id: 29,
    grade: 6,
    domain: "Prime Numbers",
    text: "Identify the prime number from the following options:",
    type: "multiple-choice",
    options: [
      { text: "15", correct: false },
      { text: "21", correct: false },
      { text: "29", correct: true },
      { text: "33", correct: false }
    ]
  },
  {
    id: 30,
    grade: 6,
    domain: "Factors & Multiples",
    text: "Find the greatest common factor (GCF) of 24 and 36.",
    type: "numeric-response",
    correctAnswer: "12",
    placeholder: "Enter GCF..."
  },
  {
    id: 31,
    grade: 6,
    domain: "Fraction Arithmetic",
    text: "Calculate: 3/4 + 1/8",
    type: "multiple-choice",
    options: [
      { text: "4/12", correct: false },
      { text: "7/8", correct: true },
      { text: "5/8", correct: false },
      { text: "1/2", correct: false }
    ]
  },
  {
    id: 32,
    grade: 6,
    domain: "Decimal to Fraction",
    text: "Write 0.75 as a fraction in simplest form.",
    type: "multiple-choice",
    options: [
      { text: "75/100", correct: false },
      { text: "3/4", correct: true },
      { text: "1/2", correct: false },
      { text: "2/3", correct: false }
    ]
  },
  {
    id: 33,
    grade: 6,
    domain: "Perimeter",
    text: "Find the perimeter of a rectangle with length 8 cm and width 5 cm.",
    type: "numeric-response",
    correctAnswer: "26",
    placeholder: "Enter perimeter in cm..."
  },

  // --- GRADE 7 (MEDIUM) ---
  {
    id: 5,
    grade: 7,
    domain: "Equations",
    text: "Solve for x: 3(x - 5.2) = 14.4",
    type: "multiple-choice",
    options: [
      { text: "x = 4.8", correct: false },
      { text: "x = 10", correct: true },
      { text: "x = 9.6", correct: false },
      { text: "x = 7.2", correct: false }
    ]
  },
  {
    id: 6,
    grade: 7,
    domain: "Scale Drawings",
    text: "A map uses a scale of 1.5 cm = 10 km. If two towns are 6 cm apart on the map, what is the actual distance between them?",
    type: "multiple-choice",
    options: [
      { text: "15 km", correct: false },
      { text: "40 km", correct: true },
      { text: "30 km", correct: false },
      { text: "60 km", correct: false }
    ]
  },
  {
    id: 7,
    grade: 7,
    domain: "Probability",
    text: "A bag contains 5 red marbles, 3 blue marbles, and 2 green marbles. If you select one marble at random, what is the probability that it is NOT red?",
    type: "multiple-choice",
    options: [
      { text: "1/2", correct: true },
      { text: "3/10", correct: false },
      { text: "1/5", correct: false },
      { text: "7/10", correct: false }
    ]
  },
  {
    id: 8,
    grade: 7,
    domain: "Geometry: Area of Circles",
    text: "Find the area of a circle with a radius of 6 cm. (Leave your answer in terms of π, e.g. write 36pi)",
    type: "numeric-response",
    correctAnswer: "36pi",
    placeholder: "Enter area (e.g. 36pi)..."
  },
  {
    id: 15,
    grade: 7,
    domain: "Inequalities",
    text: "Solve the inequality: 2x - 5 > 7",
    type: "multiple-choice",
    options: [
      { text: "x > 6", correct: true },
      { text: "x > 1", correct: false },
      { text: "x < 6", correct: false },
      { text: "x > 12", correct: false }
    ]
  },
  {
    id: 16,
    grade: 7,
    domain: "Rational Numbers",
    text: "Find the value of -15.5 + 8.25",
    type: "multiple-choice",
    options: [
      { text: "-7.25", correct: true },
      { text: "-23.75", correct: false },
      { text: "7.25", correct: false },
      { text: "-7.5", correct: false }
    ]
  },
  {
    id: 23,
    grade: 7,
    domain: "Unit Rates",
    text: "A car travels 180 miles on 6 gallons of gas. What is the unit rate in miles per gallon?",
    type: "numeric-response",
    correctAnswer: "30",
    placeholder: "Enter miles per gallon..."
  },
  {
    id: 24,
    grade: 7,
    domain: "Angles",
    text: "Angles A and B are complementary. If angle A is 35°, find the measure of angle B in degrees.",
    type: "numeric-response",
    correctAnswer: "55",
    placeholder: "Enter angle measure..."
  },
  {
    id: 25,
    grade: 7,
    domain: "Percent Increase",
    text: "An item costs $50. If the price increases by 10%, what is the new price in dollars?",
    type: "numeric-response",
    correctAnswer: "55",
    placeholder: "Enter new price..."
  },
  {
    id: 34,
    grade: 7,
    domain: "One-Step Equations",
    text: "Solve for x: -4x = 28",
    type: "numeric-response",
    correctAnswer: "-7",
    placeholder: "Enter value of x..."
  },
  {
    id: 35,
    grade: 7,
    domain: "Circle Circumference",
    text: "Find the circumference of a circle with a diameter of 10 cm in terms of π. (e.g. write 10pi)",
    type: "numeric-response",
    correctAnswer: "10pi",
    placeholder: "Enter circumference (e.g. 10pi)..."
  },
  {
    id: 36,
    grade: 7,
    domain: "Probability Calculations",
    text: "A box contains 4 red, 6 blue, and 5 yellow balls. What is the probability of selecting a blue ball?",
    type: "multiple-choice",
    options: [
      { text: "2/5", correct: true },
      { text: "6/10", correct: false },
      { text: "1/3", correct: false },
      { text: "4/15", correct: false }
    ]
  },
  {
    id: 37,
    grade: 7,
    domain: "Two-Step Equations",
    text: "Solve for x: x/3 - 4 = 2",
    type: "numeric-response",
    correctAnswer: "18",
    placeholder: "Enter value of x..."
  },
  {
    id: 38,
    grade: 7,
    domain: "Simple Interest",
    text: "Calculate the simple interest earned on $200 at a 5% interest rate for 3 years.",
    type: "numeric-response",
    correctAnswer: "30",
    placeholder: "Enter interest in dollars..."
  },
  {
    id: 39,
    grade: 7,
    domain: "Discount Word Problems",
    text: "A jacket originally costs $80 and is on sale for 25% off. What is the sale price in dollars?",
    type: "numeric-response",
    correctAnswer: "60",
    placeholder: "Enter sale price..."
  },
  {
    id: 40,
    grade: 7,
    domain: "Expression Simplification",
    text: "Simplify the expression: 3x - 5 + 2x + 9",
    type: "multiple-choice",
    options: [
      { text: "5x + 4", correct: true },
      { text: "5x - 4", correct: false },
      { text: "x + 4", correct: false },
      { text: "5x + 14", correct: false }
    ]
  },

  // --- GRADE 8 (HARD) ---
  {
    id: 9,
    grade: 8,
    domain: "Pythagorean Theorem",
    text: "A right triangle has leg lengths of 6 cm and 8 cm. Find the length of the hypotenuse.",
    type: "multiple-choice",
    options: [
      { text: "10 cm", correct: true },
      { text: "14 cm", correct: false },
      { text: "12 cm", correct: false },
      { text: "9.8 cm", correct: false }
    ]
  },
  {
    id: 10,
    grade: 8,
    domain: "Linear Functions",
    text: "Find the slope (m) of the line passing through (-3, 4) and (5, 8).",
    type: "multiple-choice",
    options: [
      { text: "m = 1/2", correct: true },
      { text: "m = 2", correct: false },
      { text: "m = -1/2", correct: false },
      { text: "m = 4/8", correct: false }
    ]
  },
  {
    id: 11,
    grade: 8,
    domain: "Linear Models",
    text: "Write the equation of a line with a slope of -3 and a y-intercept of 4.",
    type: "multiple-choice",
    options: [
      { text: "y = -3x + 4", correct: true },
      { text: "y = 4x - 3", correct: false },
      { text: "y = -3x - 4", correct: false },
      { text: "y = 3x + 4", correct: false }
    ]
  },
  {
    id: 12,
    grade: 8,
    domain: "Scientific Notation",
    text: "Convert 0.00045 into scientific notation.",
    type: "multiple-choice",
    options: [
      { text: "4.5 × 10⁻⁴", correct: true },
      { text: "4.5 × 10⁻⁵", correct: false },
      { text: "45 × 10⁻⁵", correct: false },
      { text: "4.5 × 10⁻³", correct: false }
    ]
  },
  {
    id: 17,
    grade: 8,
    domain: "Exponent Rules",
    text: "Simplify: (2³)²",
    type: "multiple-choice",
    options: [
      { text: "64", correct: true },
      { text: "32", correct: false },
      { text: "16", correct: false },
      { text: "128", correct: false }
    ]
  },
  {
    id: 18,
    grade: 8,
    domain: "Volume of Cylinders",
    text: "Find the volume of a cylinder with radius 3 cm and height 10 cm. (Leave in terms of π, e.g. write 90pi)",
    type: "numeric-response",
    correctAnswer: "90pi",
    placeholder: "Enter volume (e.g. 90pi)..."
  },
  {
    id: 26,
    grade: 8,
    domain: "Converse of Pythagorean Theorem",
    text: "Which set of numbers represents a Pythagorean triple (can form a right triangle)?",
    type: "multiple-choice",
    options: [
      { text: "3, 4, 5", correct: true },
      { text: "2, 3, 4", correct: false },
      { text: "5, 10, 12", correct: false },
      { text: "8, 9, 10", correct: false }
    ]
  },
  {
    id: 27,
    grade: 8,
    domain: "Integer Exponents",
    text: "Evaluate: 5⁻² (Write your answer as a fraction, e.g. 1/25)",
    type: "numeric-response",
    correctAnswer: "1/25",
    placeholder: "Enter fraction..."
  },
  {
    id: 28,
    grade: 8,
    domain: "Volume of Spheres",
    text: "Find the volume of a sphere with radius 3 cm in terms of π. (Volume formula: V = 4/3 π r³)",
    type: "multiple-choice",
    options: [
      { text: "36π cm³", correct: true },
      { text: "12π cm³", correct: false },
      { text: "48π cm³", correct: false },
      { text: "18π cm³", correct: false }
    ]
  },
  {
    id: 41,
    grade: 8,
    domain: "Systems of Equations",
    text: "Solve the system of equations: y = 2x + 1 and y = -x + 4. Find the coordinate pair (x, y).",
    type: "multiple-choice",
    options: [
      { text: "(1, 3)", correct: true },
      { text: "(2, 5)", correct: false },
      { text: "(0, 1)", correct: false },
      { text: "(-1, -1)", correct: false }
    ]
  },
  {
    id: 42,
    grade: 8,
    domain: "Solving Linear Equations",
    text: "Find the value of x: 3x + 4 = x + 12",
    type: "numeric-response",
    correctAnswer: "4",
    placeholder: "Enter value of x..."
  },
  {
    id: 43,
    grade: 8,
    domain: "Large Scientific Notation",
    text: "Write the number 6,200,000 in scientific notation.",
    type: "multiple-choice",
    options: [
      { text: "6.2 × 10⁶", correct: true },
      { text: "6.2 × 10⁵", correct: false },
      { text: "62 × 10⁵", correct: false },
      { text: "6.2 × 10⁷", correct: false }
    ]
  },
  {
    id: 44,
    grade: 8,
    domain: "Roots & Radicals",
    text: "Determine the value of √64 + ∛27",
    type: "numeric-response",
    correctAnswer: "11",
    placeholder: "Enter value..."
  },
  {
    id: 45,
    grade: 8,
    domain: "Volume of Cones",
    text: "Find the volume of a cone with radius 3 cm and height 4 cm in terms of π. (V = 1/3 π r² h)",
    type: "numeric-response",
    correctAnswer: "12pi",
    placeholder: "Enter volume (e.g. 12pi)..."
  },
  {
    id: 46,
    grade: 8,
    domain: "Multi-Step Linear Equations",
    text: "Find the value of x in the equation: 2(x - 3) = 4x + 8",
    type: "numeric-response",
    correctAnswer: "-7",
    placeholder: "Enter value of x..."
  }
];

// App State
let state = {
  currentStep: 1, // 1: Student Information/Landing, 2: Instructions, 3: Placement Test, 4: Results
  currentQuestionIndex: 0,
  activeDifficulty: 7, // starts at Grade 7 (medium)
  userAnswers: {},
  questionsServed: [], // List of question objects served dynamically
  score: 0,
  timeElapsed: 0,
  timerInterval: null
};

// Start Assessment
function startAssessmentFlow() {
  state.currentStep = 2;
  updateStepView();
}

function startExam() {
  state.currentStep = 3;
  state.currentQuestionIndex = 0;
  state.questionsServed = [];
  state.userAnswers = {};
  state.timeElapsed = 0;
  
  // Serve the first Grade 7 question
  serveNextQuestion(7);
  updateStepView();
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
  // Find a question of this difficulty grade that hasn't been served yet
  const servedIds = state.questionsServed.map(q => q.id);
  const pool = questions.filter(q => q.grade === difficulty && !servedIds.includes(q.id));
  
  if (pool.length > 0) {
    const nextQ = pool[Math.floor(Math.random() * pool.length)];
    state.questionsServed.push(nextQ);
  } else {
    // If pool is empty, fallback to any unserved question regardless of difficulty
    const fallbackPool = questions.filter(q => !servedIds.includes(q.id));
    if (fallbackPool.length > 0) {
      const nextQ = fallbackPool[Math.floor(Math.random() * fallbackPool.length)];
      state.questionsServed.push(nextQ);
    } else {
      // End test if absolutely out of questions
      finishExam();
    }
  }
}

function renderQuestion() {
  const container = document.getElementById("question-container");
  if (!container) return;

  const currentQ = state.questionsServed[state.currentQuestionIndex];
  if (!currentQ) return;

  document.getElementById("question-number-display").innerText = `Question ${state.currentQuestionIndex + 1} of 15`;
  
  // Update progress bar
  const progressPercent = ((state.currentQuestionIndex + 1) / 15) * 100;
  document.getElementById("progress-bar-fill").style.width = `${progressPercent}%`;

  let htmlContent = `
    <div class="mb-6">
      <span class="px-3 py-1 text-xs font-bold text-sky-600 bg-sky-50 rounded-full">${currentQ.domain} (Grade ${currentQ.grade})</span>
      <h2 class="text-xl font-bold text-slate-800 mt-4 leading-relaxed">${currentQ.text}</h2>
    </div>
  `;

  if (currentQ.type === "multiple-choice") {
    htmlContent += `<div class="space-y-4">`;
    currentQ.options.forEach((opt, idx) => {
      const isSelected = state.userAnswers[state.currentQuestionIndex] === idx;
      const optionClass = isSelected 
        ? "border-sky-500 bg-sky-50 ring-2 ring-sky-500/20" 
        : "border-slate-100 hover:bg-slate-50";
      
      htmlContent += `
        <button onclick="selectOption(${idx})" class="w-full text-left p-4 rounded-xl border-2 ${optionClass} transition-all duration-200 focus:outline-none flex items-center justify-between">
          <span class="text-slate-700 font-semibold">${opt.text}</span>
          <span class="w-5 h-5 rounded-full border-2 flex items-center justify-center ${isSelected ? 'border-sky-500 bg-sky-500 text-white' : 'border-slate-300'}">
            ${isSelected ? '✓' : ''}
          </span>
        </button>
      `;
    });
    htmlContent += `</div>`;
  } else if (currentQ.type === "numeric-response") {
    const currentVal = state.userAnswers[state.currentQuestionIndex] || "";
    htmlContent += `
      <div class="mt-4">
        <input type="text" id="numeric-input" oninput="saveNumericAnswer(this.value)" value="${currentVal}" placeholder="${currentQ.placeholder}" class="w-full p-4 rounded-xl border-2 border-slate-200 focus:border-sky-500 focus:outline-none text-lg text-slate-800 font-bold transition-all duration-200">
      </div>
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
    const isAnswered = state.userAnswers[i] !== undefined;
    
    let btnClass = "bg-slate-100 text-slate-400";
    if (isCurrent) {
      btnClass = "bg-sky-500 text-white ring-4 ring-sky-500/20";
    } else if (isAnswered) {
      btnClass = "bg-emerald-500 text-white";
    }

    html += `
      <button onclick="jumpToQuestion(${i})" class="w-10 h-10 rounded-full font-bold flex items-center justify-center transition-all duration-200 ${btnClass}">
        ${i + 1}
      </button>
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
    alert("Please answer the question before moving next!");
    return;
  }

  // Adaptive logic: Check correctness of current question to set difficulty for the next served question
  let isCorrect = false;
  if (currentQ.type === "multiple-choice") {
    isCorrect = currentQ.options[userAns].correct;
  } else if (currentQ.type === "numeric-response") {
    isCorrect = String(userAns).trim().toLowerCase() === currentQ.correctAnswer.toLowerCase();
  }

  // Adjust difficulty grade dynamically
  if (isCorrect) {
    if (state.activeDifficulty < 8) state.activeDifficulty++;
  } else {
    if (state.activeDifficulty > 6) state.activeDifficulty--;
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
  state.currentStep = 4;
  
  // Calculate recommended level based on standard ratios and scoring
  let correctCount = 0;
  state.questionsServed.forEach((q, idx) => {
    const userAns = state.userAnswers[idx];
    if (userAns !== undefined) {
      if (q.type === "multiple-choice") {
        if (q.options[userAns] && q.options[userAns].correct) correctCount++;
      } else if (q.type === "numeric-response") {
        if (String(userAns).trim().toLowerCase() === q.correctAnswer.toLowerCase()) correctCount++;
      }
    }
  });

  state.score = correctCount;
  updateStepView();
  triggerConfetti();
}

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

function updateStepView() {
  // Hide all screens
  document.getElementById("landing-screen").classList.add("hidden");
  document.getElementById("instructions-screen").classList.add("hidden");
  document.getElementById("exam-screen").classList.add("hidden");
  document.getElementById("results-screen").classList.add("hidden");

  // Update timeline indicator
  for (let i = 1; i <= 4; i++) {
    const stepEl = document.getElementById(`timeline-step-${i}`);
    if (stepEl) {
      if (i < state.currentStep) {
        stepEl.className = "timeline-step bg-emerald-500 text-white";
        stepEl.innerText = "✓";
      } else if (i === state.currentStep) {
        stepEl.className = "timeline-step bg-sky-500 text-white ring-4 ring-sky-500/20";
        stepEl.innerText = i;
      } else {
        stepEl.className = "timeline-step bg-slate-200 text-slate-400";
        stepEl.innerText = i;
      }
    }
  }

  // Toggle header action button
  const headerBtn = document.getElementById("header-action-btn");
  if (headerBtn) {
    if (state.currentStep === 3) {
      headerBtn.innerText = "Home";
      headerBtn.onclick = function() {
        openModal('exit-confirm-modal');
      };
    } else {
      headerBtn.innerText = "Begin Placement Test";
      headerBtn.onclick = startAssessmentFlow;
    }
  }

  // Update Parent Confidence Section vs Test Rules
  const confidenceSection = document.getElementById("parent-confidence-section");
  if (confidenceSection) {
    if (state.currentStep === 3) {
      confidenceSection.innerHTML = `
        <div class="max-w-5xl w-full mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 text-center">
          <div class="space-y-3 flex flex-col items-center">
            <span class="text-4xl">📝</span>
            <h4 class="font-bold text-navy-dark">Rule 1: Work Independently</h4>
            <p class="text-sm text-slate-500 leading-relaxed">Do not ask parents, siblings, or friends for help on any problem.</p>
          </div>
          <div class="space-y-3 flex flex-col items-center">
            <span class="text-4xl">✏️</span>
            <h4 class="font-bold text-navy-dark">Rule 2: Paper & Pencil</h4>
            <p class="text-sm text-slate-500 leading-relaxed">Solve questions on scratch paper before selecting your answer.</p>
          </div>
          <div class="space-y-3 flex flex-col items-center">
            <span class="text-4xl">🚫</span>
            <h4 class="font-bold text-navy-dark">Rule 3: No Calculators</h4>
            <p class="text-sm text-slate-500 leading-relaxed">Work through arithmetic mentally or on scratch paper.</p>
          </div>
          <div class="space-y-3 flex flex-col items-center">
            <span class="text-4xl">⭐</span>
            <h4 class="font-bold text-navy-dark">Rule 4: Try Your Best</h4>
            <p class="text-sm text-slate-500 leading-relaxed">Take your time and think through every question carefully.</p>
          </div>
        </div>
      `;
    } else {
      confidenceSection.innerHTML = `
        <div class="max-w-5xl w-full mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 text-center">
          <div class="space-y-3 flex flex-col items-center">
            <span class="text-4xl">🎓</span>
            <h4 class="font-bold text-navy-dark">Standards-Aligned</h4>
            <p class="text-sm text-slate-500 leading-relaxed">Covers fundamental core math domains from standard curricula.</p>
          </div>
          <div class="space-y-3 flex flex-col items-center">
            <span class="text-4xl">🔒</span>
            <h4 class="font-bold text-navy-dark">Secure Assessment</h4>
            <p class="text-sm text-slate-500 leading-relaxed">No tracking, private assessment, safe learning environment.</p>
          </div>
          <div class="space-y-3 flex flex-col items-center">
            <span class="text-4xl">💡</span>
            <h4 class="font-bold text-navy-dark">Personalized Results</h4>
            <p class="text-sm text-slate-500 leading-relaxed">Instant level mapping with clear feedback for parents.</p>
          </div>
          <div class="space-y-3 flex flex-col items-center">
            <span class="text-4xl">🏫</span>
            <h4 class="font-bold text-navy-dark">Educator Developed</h4>
            <p class="text-sm text-slate-500 leading-relaxed">Formulated by teachers to yield accurate grade benchmarks.</p>
          </div>
        </div>
      `;
    }
  }

  // Show active screen
  if (state.currentStep === 1) {
    document.getElementById("landing-screen").classList.remove("hidden");
  } else if (state.currentStep === 2) {
    document.getElementById("instructions-screen").classList.remove("hidden");
  } else if (state.currentStep === 3) {
    document.getElementById("exam-screen").classList.remove("hidden");
    renderQuestion();
  } else if (state.currentStep === 4) {
    document.getElementById("results-screen").classList.remove("hidden");
    
    // Group and calculate correct ratios by grade for advanced recommendation
    const grade8Served = state.questionsServed.filter(q => q.grade === 8);
    const grade7Served = state.questionsServed.filter(q => q.grade === 7);
    
    const getCorrectRatio = (servedList) => {
      if (servedList.length === 0) return 0;
      let correct = 0;
      servedList.forEach(q => {
        const idx = state.questionsServed.indexOf(q);
        const userAns = state.userAnswers[idx];
        if (userAns !== undefined) {
          if (q.type === "multiple-choice") {
            if (q.options[userAns] && q.options[userAns].correct) correct++;
          } else if (q.type === "numeric-response") {
            if (String(userAns).trim().toLowerCase() === q.correctAnswer.toLowerCase()) correct++;
          }
        }
      });
      return correct / servedList.length;
    };

    const g8Ratio = getCorrectRatio(grade8Served);
    const g7Ratio = getCorrectRatio(grade7Served);

    let recommendedLevel = "6th Grade Foundation";
    if (grade8Served.length >= 3 && g8Ratio >= 0.7) {
      recommendedLevel = "8th Grade Rigorous Math";
    } else if (grade7Served.length >= 3 && g7Ratio >= 0.7) {
      recommendedLevel = "7th Grade Standard Math";
    } else {
      // Fallback based on total score
      if (state.score >= 11) {
        recommendedLevel = "8th Grade Rigorous Math";
      } else if (state.score >= 7) {
        recommendedLevel = "7th Grade Standard Math";
      }
    }
    
    document.getElementById("placement-recommendation").innerText = recommendedLevel;
    document.getElementById("score-details").innerText = `You answered ${state.score} out of 15 questions correctly.`;
  }
}

// Global initialization
window.onload = function() {
  updateStepView();
};
