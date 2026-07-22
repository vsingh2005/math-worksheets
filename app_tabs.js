<script type="text/javascript">
/* <![CDATA[ */
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
		],
		explanation: "To simplify the ratio 8:12, divide both numbers by their greatest common factor (GCF), which is 4: 8 ÷ 4 = 2 and 12 ÷ 4 = 3. Therefore, the simplest form is 2:3."
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
		],
		explanation: "Substitute x = 4 and y = 3 into the expression: (4)² - (3)² = 16 - 9 = 7."
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
		],
		explanation: "Since both y-coordinates are equal to 5, calculate the horizontal distance by taking the absolute difference of the x-coordinates: |9 - 2| = 7 units."
	},
	{
		id: 4,
		grade: 6,
		domain: "Measurement Conversions",
		text: "Convert 48 ounces into pounds. (1 pound = 16 ounces)",
		type: "numeric-response",
		correctAnswer: "3",
		placeholder: "Enter weight in pounds...",
		explanation: "Divide the total ounces by 16 ounces per pound: 48 ÷ 16 = 3 pounds."
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
		],
		explanation: "Divide both numerator (24) and denominator (36) by their greatest common factor (12): 24 ÷ 12 = 2 and 36 ÷ 12 = 3, giving 2/3."
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
		],
		explanation: "Convert 15% to decimal form (0.15) and multiply by 80: 0.15 × 80 = 12."
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
		],
		explanation: "Absolute value measures distance from 0: |-12| = 12, |8| = 8, |-3| = 3, |0| = 0. 12 is the largest distance."
	},
	{
		id: 20,
		grade: 6,
		domain: "Basic Equations",
		text: "Solve for x: x + 15.4 = 20",
		type: "numeric-response",
		correctAnswer: "4.6",
		placeholder: "Enter value of x...",
		explanation: "Subtract 15.4 from both sides of the equation: x = 20 - 15.4 = 4.6."
	},
	{
		id: 21,
		grade: 6,
		domain: "Data & Statistics",
		text: "Find the mean of the numbers: 5, 8, 12, 15.",
		type: "numeric-response",
		correctAnswer: "10",
		placeholder: "Enter the average...",
		explanation: "Sum the numbers (5 + 8 + 12 + 15 = 40) and divide by the count (4): 40 ÷ 4 = 10."
	},
	{
		id: 22,
		grade: 6,
		domain: "Area of Triangles",
		text: "Find the area of a triangle with a base of 6 cm and a height of 5 cm.",
		type: "numeric-response",
		correctAnswer: "15",
		placeholder: "Enter area in square cm...",
		explanation: "Use the triangle area formula A = 1/2 × base × height: A = 1/2 × 6 × 5 = 15 cm²."
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
		],
		explanation: "A prime number has only 2 factors: 1 and itself. 15 (3×5), 21 (3×7), and 33 (3×11) are composite. 29 cannot be factored further."
	},
	{
		id: 30,
		grade: 6,
		domain: "Factors & Multiples",
		text: "Find the greatest common factor (GCF) of 24 and 36.",
		type: "numeric-response",
		correctAnswer: "12",
		placeholder: "Enter GCF...",
		explanation: "Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24. Factors of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36. The greatest common factor is 12."
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
		],
		explanation: "Find a common denominator (8): 3/4 = 6/8. Now add: 6/8 + 1/8 = 7/8."
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
		],
		explanation: "0.75 = 75/100. Divide both numerator and denominator by 25 to simplify: 75÷25 / 100÷25 = 3/4."
	},
	{
		id: 33,
		grade: 6,
		domain: "Perimeter",
		text: "Find the perimeter of a rectangle with length 8 cm and width 5 cm.",
		type: "numeric-response",
		correctAnswer: "26",
		placeholder: "Enter perimeter in cm...",
		explanation: "Perimeter formula: P = 2(length + width) = 2(8 + 5) = 2(13) = 26 cm."
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
		],
		explanation: "Divide both sides by 3: x - 5.2 = 4.8. Add 5.2 to both sides: x = 4.8 + 5.2 = 10."
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
		],
		explanation: "Determine the multiplier: 6 cm ÷ 1.5 cm = 4. Multiply the actual scale distance by 4: 4 × 10 km = 40 km."
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
		],
		explanation: "Total marbles = 5 + 3 + 2 = 10. Marbles that are NOT red = 3 blue + 2 green = 5. Probability = 5/10 = 1/2."
	},
	{
		id: 8,
		grade: 7,
		domain: "Geometry: Area of Circles",
		text: "Find the area of a circle with a radius of 6 cm. (Leave your answer in terms of π, e.g. write 36pi)",
		type: "numeric-response",
		correctAnswer: "36pi",
		placeholder: "Enter area (e.g. 36pi)...",
		explanation: "Use the circle area formula A = π r². With r = 6 cm, A = π × (6)² = 36π cm²."
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
		],
		explanation: "Add 5 to both sides: 2x > 12. Divide both sides by 2: x > 6."
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
		],
		explanation: "Subtract 8.25 from 15.5 and apply the negative sign of the larger absolute value: -(15.50 - 8.25) = -7.25."
	},
	{
		id: 23,
		grade: 7,
		domain: "Unit Rates",
		text: "A car travels 180 miles on 6 gallons of gas. What is the unit rate in miles per gallon?",
		type: "numeric-response",
		correctAnswer: "30",
		placeholder: "Enter miles per gallon...",
		explanation: "Divide total miles by total gallons: 180 ÷ 6 = 30 miles per gallon."
	},
	{
		id: 24,
		grade: 7,
		domain: "Angles",
		text: "Angles A and B are complementary. If angle A is 35°, find the measure of angle B in degrees.",
		type: "numeric-response",
		correctAnswer: "55",
		placeholder: "Enter angle measure...",
		explanation: "Complementary angles sum to 90°. Therefore, Angle B = 90° - 35° = 55°."
	},
	{
		id: 25,
		grade: 7,
		domain: "Percent Increase",
		text: "An item costs $50. If the price increases by 10%, what is the new price in dollars?",
		type: "numeric-response",
		correctAnswer: "55",
		placeholder: "Enter new price...",
		explanation: "10% of $50 is 0.10 × 50 = $5. New price = $50 + $5 = $55."
	},
	{
		id: 34,
		grade: 7,
		domain: "One-Step Equations",
		text: "Solve for x: -4x = 28",
		type: "numeric-response",
		correctAnswer: "-7",
		placeholder: "Enter value of x...",
		explanation: "Divide both sides by -4: x = 28 / (-4) = -7."
	},
	{
		id: 35,
		grade: 7,
		domain: "Circle Circumference",
		text: "Find the circumference of a circle with a diameter of 10 cm in terms of π. (e.g. write 10pi)",
		type: "numeric-response",
		correctAnswer: "10pi",
		placeholder: "Enter circumference (e.g. 10pi)...",
		explanation: "Circumference formula: C = π d. Given diameter d = 10 cm, C = 10π cm."
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
		],
		explanation: "Total balls = 4 + 6 + 5 = 15. Number of blue balls = 6. Probability = 6/15, which simplifies to 2/5."
	},
	{
		id: 37,
		grade: 7,
		domain: "Two-Step Equations",
		text: "Solve for x: x/3 - 4 = 2",
		type: "numeric-response",
		correctAnswer: "18",
		placeholder: "Enter value of x...",
		explanation: "Add 4 to both sides: x/3 = 6. Multiply both sides by 3: x = 18."
	},
	{
		id: 38,
		grade: 7,
		domain: "Simple Interest",
		text: "Calculate the simple interest earned on $200 at a 5% interest rate for 3 years.",
		type: "numeric-response",
		correctAnswer: "30",
		placeholder: "Enter interest in dollars...",
		explanation: "Simple interest formula: I = P × r × t = 200 × 0.05 × 3 = $30."
	},
	{
		id: 39,
		grade: 7,
		domain: "Discount Word Problems",
		text: "A jacket originally costs $80 and is on sale for 25% off. What is the sale price in dollars?",
		type: "numeric-response",
		correctAnswer: "60",
		placeholder: "Enter sale price...",
		explanation: "25% discount of $80 is 0.25 × 80 = $20. Sale price = 80 - 20 = $60."
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
		],
		explanation: "Combine like terms: (3x + 2x) + (-5 + 9) = 5x + 4."
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
		],
		explanation: "Pythagorean theorem c² = a² + b²: c² = 6² + 8² = 36 + 64 = 100. c = √100 = 10 cm."
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
		],
		explanation: "Slope formula m = (y₂ - y₁) / (x₂ - x₁) = (8 - 4) / (5 - (-3)) = 4 / 8 = 1/2."
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
		],
		explanation: "Slope-intercept form is y = mx + b. Substitute m = -3 and b = 4 to get y = -3x + 4."
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
		],
		explanation: "Move the decimal 4 places to the right to get 4.5. Because the original number is less than 1, the exponent is negative: 4.5 × 10⁻⁴."
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
		],
		explanation: "Power of a power rule: (aᵐ)ⁿ = aᵐxⁿ. (2³)² = 2⁶ = 64."
	},
	{
		id: 18,
		grade: 8,
		domain: "Volume of Cylinders",
		text: "Find the volume of a cylinder with radius 3 cm and height 10 cm. (Leave in terms of π, e.g. write 90pi)",
		type: "numeric-response",
		correctAnswer: "90pi",
		placeholder: "Enter volume (e.g. 90pi)...",
		explanation: "Cylinder volume formula: V = π r² h = π × (3)² × 10 = π × 9 × 10 = 90π cm³."
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
		],
		explanation: "Test a² + b² = c² for 3, 4, 5: 3² + 4² = 9 + 16 = 25 = 5². It forms a perfect right triangle."
	},
	{
		id: 27,
		grade: 8,
		domain: "Integer Exponents",
		text: "Evaluate: 5⁻² (Write your answer as a fraction, e.g. 1/25)",
		type: "numeric-response",
		correctAnswer: "1/25",
		placeholder: "Enter fraction...",
		explanation: "Negative exponent rule: a⁻ⁿ = 1 / (aⁿ). So 5⁻² = 1 / (5²) = 1/25."
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
		],
		explanation: "Substitute r = 3 into V = 4/3 π r³: V = 4/3 × π × 27 = 36π cm³."
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
		],
		explanation: "Set expressions equal: 2x + 1 = -x + 4. 3x = 3 => x = 1. Substitute x = 1 into y = 2(1) + 1 = 3. Point is (1, 3)."
	},
	{
		id: 42,
		grade: 8,
		domain: "Solving Linear Equations",
		text: "Find the value of x: 3x + 4 = x + 12",
		type: "numeric-response",
		correctAnswer: "4",
		placeholder: "Enter value of x...",
		explanation: "Subtract x from both sides: 2x + 4 = 12. Subtract 4: 2x = 8. Divide by 2: x = 4."
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
		],
		explanation: "Move decimal 6 places left to form 6.2. Since 6,200,000 > 1, the exponent is positive: 6.2 × 10⁶."
	},
	{
		id: 44,
		grade: 8,
		domain: "Roots & Radicals",
		text: "Determine the value of √64 + ∛27",
		type: "numeric-response",
		correctAnswer: "11",
		placeholder: "Enter value...",
		explanation: "Evaluate square root and cube root: √64 = 8, ∛27 = 3. Sum: 8 + 3 = 11."
	},
	{
		id: 45,
		grade: 8,
		domain: "Volume of Cones",
		text: "Find the volume of a cone with radius 3 cm and height 4 cm in terms of π. (V = 1/3 π r² h)",
		type: "numeric-response",
		correctAnswer: "12pi",
		placeholder: "Enter volume (e.g. 12pi)...",
		explanation: "Substitute r = 3 and h = 4 into V = 1/3 π r² h: V = 1/3 × π × 9 × 4 = 12π cm³."
	},
	{
		id: 46,
		grade: 8,
		domain: "Multi-Step Linear Equations",
		text: "Find the value of x in the equation: 2(x - 3) = 4x + 8",
		type: "numeric-response",
		correctAnswer: "-7",
		placeholder: "Enter value of x...",
		explanation: "Expand left side: 2x - 6 = 4x + 8. Subtract 2x: -6 = 2x + 8. Subtract 8: -14 = 2x. Divide by 2: x = -7."
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
	timerInterval: null,
	isExiting: false,
	activeReviewFilter: 'all'
};

/* =========================================================
	AUTHENTICATION & PROFILE MANAGER (SECURE CLIENT-SIDE JS)
	========================================================= */

class AuthenticationManager {
	constructor() {
		this.currentUser = null;
		this.users = [];
		this.allAttempts = [];
		this.init();
	}

	async hashPassword(password, salt) {
		const encoder = new TextEncoder();
		const data = encoder.encode(password + salt);
		const hashBuffer = await crypto.subtle.digest('SHA-256', data);
		const hashArray = Array.from(new Uint8Array(hashBuffer));
		return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
	}

	async init() {
		// Load stored users or populate default models
		const storedUsers = localStorage.getItem('kss_users');
		if (storedUsers) {
			this.users = JSON.parse(storedUsers);
		} else {
			const salt1 = 'kss_salt_demo_1';
			const hash1 = await this.hashPassword('password123', salt1);
			const salt2 = 'kss_salt_demo_2';
			const hash2 = await this.hashPassword('stemstudio2026', salt2);

			this.users = [
				{
					username: 'student1',
					email: 'student1@kidsstemstudio.com',
					passwordHash: hash1,
					salt: salt1,
					createdAt: new Date().toISOString(),
					attempts: []
				},
				{
					username: 'parent_demo',
					email: 'parent@kidsstemstudio.com',
					passwordHash: hash2,
					salt: salt2,
					createdAt: new Date().toISOString(),
					attempts: []
				}
			];
			this.saveUsersToStorage();
		}

		const storedAttempts = localStorage.getItem('kss_attempts');
		if (storedAttempts) {
			this.allAttempts = JSON.parse(storedAttempts);
		}

		const session = localStorage.getItem('kss_session') || sessionStorage.getItem('kss_session');
		if (session) {
			const found = this.users.find(u => u.username.toLowerCase() === session.toLowerCase());
			if (found) {
				this.currentUser = found;
			}
		}

		this.updateHeaderUI();
	}

	saveUsersToStorage() {
		localStorage.setItem('kss_users', JSON.stringify(this.users));
	}

	saveAttemptsToStorage() {
		localStorage.setItem('kss_attempts', JSON.stringify(this.allAttempts));
	}

	async registerUser(username, email, password) {
		username = username.trim();
		email = email.trim();
		if (!username || !email || !password) {
			throw new Error('Please fill in all registration fields.');
		}

		const existing = this.users.find(u => u.username.toLowerCase() === username.toLowerCase() || u.email.toLowerCase() === email.toLowerCase());
		if (existing) {
			throw new Error('Username or email address already registered.');
		}

		const salt = 'kss_salt_' + Math.random().toString(36).substring(2);
		const passwordHash = await this.hashPassword(password, salt);

		const newUser = {
			username: username,
			email: email,
			passwordHash: passwordHash,
			salt: salt,
			createdAt: new Date().toISOString(),
			attempts: []
		};

		this.users.push(newUser);
		this.saveUsersToStorage();
		this.currentUser = newUser;
		localStorage.setItem('kss_session', newUser.username);
		this.updateHeaderUI();
		return newUser;
	}

	async loginUser(usernameOrEmail, password, rememberMe) {
		usernameOrEmail = usernameOrEmail.trim();
		if (!usernameOrEmail || !password) {
			throw new Error('Username/Email and Password are required.');
		}

		try {
			// 1. Try authenticating with WordPress JWT REST API
			const response = await fetch('/wp-json/jwt-auth/v1/token', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					username: usernameOrEmail,
					password: password
				})
			});

			const data = await response.json();

			if (response.ok && data.token) {
				// Success: Create/Load user session linked to WordPress
				let user = this.users.find(u => u.username.toLowerCase() === data.user_nicename.toLowerCase());
				if (!user) {
					user = {
						username: data.user_nicename,
						email: data.user_email,
						createdAt: new Date().toISOString(),
						attempts: []
					};
					this.users.push(user);
					this.saveUsersToStorage();
				}

				this.currentUser = user;
				if (rememberMe) {
					localStorage.setItem('kss_session', user.username);
				} else {
					sessionStorage.setItem('kss_session', user.username);
				}

				this.updateHeaderUI();
				return user;
			} else {
				// If API returned error message, throw it to check fallback next
				throw new Error(data.message || 'WordPress authentication failed.');
			}
		} catch (err) {
			// 2. Fallback: Authenticate locally for offline testing or demo logins (e.g., student1)
			const fallbackUser = this.users.find(u => 
				u.username.toLowerCase() === usernameOrEmail.toLowerCase() || 
				u.email.toLowerCase() === usernameOrEmail.toLowerCase()
			);

			if (fallbackUser && fallbackUser.salt) {
				const computedHash = await this.hashPassword(password, fallbackUser.salt);
				if (computedHash === fallbackUser.passwordHash) {
					this.currentUser = fallbackUser;
					if (rememberMe) {
						localStorage.setItem('kss_session', fallbackUser.username);
					} else {
						sessionStorage.setItem('kss_session', fallbackUser.username);
					}
					this.updateHeaderUI();
					return fallbackUser;
				}
			}

			// If both fail, throw the original authentication error
			throw new Error(err.message || 'Invalid username or password.');
		}
	}

	logoutUser() {
		this.currentUser = null;
		localStorage.removeItem('kss_session');
		sessionStorage.removeItem('kss_session');
		state.currentStep = 1;
		this.updateHeaderUI();
	}

	saveExamAttempt(attemptData) {
		const username = this.currentUser ? this.currentUser.username : 'Guest Student';
		const attempt = {
			id: 'att_' + Date.now(),
			username: username,
			timestamp: new Date().toISOString(),
			score: attemptData.score,
			totalQuestions: 15,
			timeElapsedSeconds: attemptData.timeElapsed,
			recommendedLevel: attemptData.recommendedLevel,
			answers: attemptData.answers
		};

		this.allAttempts.push(attempt);
		this.saveAttemptsToStorage();

		if (this.currentUser) {
			const userObj = this.users.find(u => u.username === this.currentUser.username);
			if (userObj) {
				if (!userObj.attempts) userObj.attempts = [];
				userObj.attempts.push(attempt.id);
				this.saveUsersToStorage();
			}
		}
		return attempt;
	}

	getUserAttempts(username) {
		return this.allAttempts.filter(a => a.username.toLowerCase() === username.toLowerCase());
	}

	updateHeaderUI() {
		const loginGate = document.getElementById('mandatory-login-screen');
		const appContent = document.getElementById('app-content');
		const headerWidget = document.getElementById('user-header-widget');

		if (!this.currentUser) {
			if (loginGate) loginGate.classList.remove('hidden');
			if (appContent) appContent.classList.add('hidden');
		} else {
			if (loginGate) loginGate.classList.add('hidden');
			if (appContent) appContent.classList.remove('hidden');

			if (headerWidget) {
				headerWidget.innerHTML = `
					<div class="flex items-center space-x-3 bg-slate-100 px-3.5 py-1.5 rounded-full border border-slate-200">
						<span class="w-7 h-7 rounded-full bg-kss-teal text-white flex items-center justify-center font-bold text-xs">
							${this.currentUser.username.substring(0, 1).toUpperCase()}
						</span>
						<span class="text-xs font-extrabold text-navy-dark">${this.currentUser.username}</span>
						<button onclick="AuthManager.renderHistoryModal()" class="text-xs font-bold text-sky-600 hover:underline">📜 History</button>
						<button onclick="AuthManager.logoutUser()" class="text-xs font-bold text-rose-500 hover:underline">Logout</button>
					</div>
				`;
			}
			updateStepView();
		}
	}

	renderHistoryModal() {
		const historyModal = document.getElementById('history-modal');
		const container = document.getElementById('user-history-content');
		if (!historyModal || !container) return;

		if (!this.currentUser) {
			container.innerHTML = `<p class="text-slate-500 text-sm">Please log in to view your past test attempts.</p>`;
		} else {
			const userAttempts = this.getUserAttempts(this.currentUser.username);
			if (userAttempts.length === 0) {
				container.innerHTML = `
					<div class="text-center py-8 space-y-2">
						<span class="text-3xl block">📋</span>
						<p class="text-slate-600 font-bold">No math placement attempts recorded yet.</p>
						<p class="text-xs text-slate-400">Complete a math placement exam to track your recommended level and progress!</p>
					</div>
				`;
			} else {
				let html = `<div class="space-y-3">`;
				userAttempts.slice().reverse().forEach((att) => {
					const dt = new Date(att.timestamp).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric', hour: '2-digit', minute: '2-digit' });
					const mins = Math.floor(att.timeElapsedSeconds / 60);
					const secs = att.timeElapsedSeconds % 60;
					html += `
						<div class="bg-slate-50 p-4 rounded-xl border border-slate-200 flex flex-col md:flex-row justify-between items-start md:items-center gap-2">
							<div>
								<span class="text-xs font-bold text-slate-400 block">${dt}</span>
								<h5 class="font-extrabold text-navy-dark text-base">${att.recommendedLevel}</h5>
								<p class="text-xs text-slate-600 font-medium">Time Taken: ${mins}m ${secs}s</p>
							</div>
							<div class="bg-emerald-100 text-emerald-800 font-black px-4 py-2 rounded-xl text-sm self-end md:self-center">
								Score: ${att.score} / 15
							</div>
						</div>
					`;
				});
				html += `</div>`;
				container.innerHTML = html;
			}
		}
		historyModal.classList.remove('hidden');
	}
}

const AuthManager = new AuthenticationManager();

/* =========================================================
	WP-LOGIN DIALOG & TAB SWITCHING HANDLERS
	========================================================= */



function switchAuthTab(tabName) {
	const alertEl = document.getElementById('auth-alert');
	if (alertEl) alertEl.classList.add('hidden');

	const loginForm = document.getElementById('loginform');
	const regForm = document.getElementById('registerform');
	const lostForm = document.getElementById('lostpasswordform');

	const navLoginLinks = document.getElementById('nav-login-links');
	const navBackToLogin = document.getElementById('nav-back-to-login');

	loginForm.classList.add('hidden');
	regForm.classList.add('hidden');
	lostForm.classList.add('hidden');

	if (tabName === 'login') {
		loginForm.classList.remove('hidden');
		navLoginLinks.classList.remove('hidden');
		navBackToLogin.classList.add('hidden');
	} else if (tabName === 'register') {
		regForm.classList.remove('hidden');
		navLoginLinks.classList.add('hidden');
		navBackToLogin.classList.remove('hidden');
	} else if (tabName === 'lostpassword') {
		lostForm.classList.remove('hidden');
		navLoginLinks.classList.add('hidden');
		navBackToLogin.classList.remove('hidden');
	}
}

function togglePasswordVisibility(inputId, btnEl) {
	const input = document.getElementById(inputId);
	if (!input) return;
	if (input.type === 'password') {
		input.type = 'text';
		btnEl.innerHTML = `<span class="dashicons dashicons-hidden"></span>`;
	} else {
		input.type = 'password';
		btnEl.innerHTML = `<span class="dashicons dashicons-visibility"></span>`;
	}
}

function showAuthAlert(msg, isError = true) {
	const alertEl = document.getElementById('auth-alert');
	if (!alertEl) return;
	alertEl.className = `mb-4 p-3 rounded-lg text-xs font-bold text-center ${isError ? 'bg-rose-100 text-rose-700 border border-rose-200' : 'bg-emerald-100 text-emerald-700 border border-emerald-200'}`;
	alertEl.innerText = msg;
	alertEl.classList.remove('hidden');
}

async function handleLoginFormSubmit(e) {
	e.preventDefault();
	const usernameOrEmail = document.getElementById('user_login').value;
	const password = document.getElementById('user_pass').value;
	const rememberMe = document.getElementById('rememberme').checked;

	try {
		await AuthManager.loginUser(usernameOrEmail, password, rememberMe);
		showAuthAlert('Login successful! Unlocking Math Placement Portal...', false);
	} catch (err) {
		showAuthAlert(err.message || 'Login failed. Please check your credentials.');
	}
}

async function handleRegisterFormSubmit(e) {
	e.preventDefault();
	const username = document.getElementById('reg_user').value;
	const email = document.getElementById('reg_email').value;
	const password = document.getElementById('reg_pass').value;

	try {
		await AuthManager.registerUser(username, email, password);
		showAuthAlert('Math Student Account registered successfully!', false);
	} catch (err) {
		showAuthAlert(err.message || 'Registration failed.');
	}
}

function handleLostPasswordSubmit(e) {
	e.preventDefault();
	const input = document.getElementById('user_reset').value;
	if (!input) return;
	showAuthAlert('If an account exists, a password reset link has been dispatched to your email.', false);
}

/* =========================================================
	EXAM CORE CONTROLLER & ADAPTIVE LOGIC
	========================================================= */

function startAssessmentFlow() {
	state.currentStep = 2;
	updateStepView();
}

function startExam() {
	state.currentStep = 3;
	state.currentQuestionIndex = 0;
	state.userAnswers = {};
	state.timeElapsed = 0;
	
	const g6 = questions.filter(q => q.grade === 6);
	const g7 = questions.filter(q => q.grade === 7);
	const g8 = questions.filter(q => q.grade === 8);
	
	const shuffle = arr => arr.slice().sort(() => Math.random() - 0.5);
	
	const set6 = shuffle(g6).slice(0, 5);
	const set7 = shuffle(g7).slice(0, 5);
	const set8 = shuffle(g8).slice(0, 5);
	
	state.questionsServed = [...set6, ...set7, ...set8];
	
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
		} else if (state.currentStep !== 4) {
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
		const isAnswered = state.userAnswers[i] !== undefined && String(state.userAnswers[i]).trim() !== "";
		
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
		alert("Please answer the math question before moving next!");
		return;
	}

	let isCorrect = false;
	if (currentQ.type === "multiple-choice") {
		isCorrect = currentQ.options[userAns] && currentQ.options[userAns].correct;
	} else if (currentQ.type === "numeric-response") {
		isCorrect = String(userAns).trim().toLowerCase() === currentQ.correctAnswer.toLowerCase();
	}

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
	
	// Ensure state.questionsServed contains 15 questions even if ended early
	while (state.questionsServed.length < 15) {
		const servedIds = state.questionsServed.map(q => q.id);
		const available = questions.filter(q => !servedIds.includes(q.id));
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

	const grade8Served = state.questionsServed.filter(q => q.grade === 8);
	const grade7Served = state.questionsServed.filter(q => q.grade === 7);
	
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

	const g8Ratio = getCorrectRatio(grade8Served);
	const g7Ratio = getCorrectRatio(grade7Served);

	let recommendedLevel = "6th Grade Foundation Math";
	if (grade8Served.length >= 3 && g8Ratio >= 0.7) {
		recommendedLevel = "8th Grade Rigorous Math";
	} else if (grade7Served.length >= 3 && g7Ratio >= 0.7) {
		recommendedLevel = "7th Grade Standard Math";
	} else {
		if (state.score >= 11) {
			recommendedLevel = "8th Grade Rigorous Math";
		} else if (state.score >= 7) {
			recommendedLevel = "7th Grade Standard Math";
		}
	}

	state.recommendedLevel = recommendedLevel;

	AuthManager.saveExamAttempt({
		score: state.score,
		timeElapsed: state.timeElapsed,
		recommendedLevel: recommendedLevel,
		answers: answerBreakdown
	});

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

/* =========================================================
	FLUID SECTION: RESULTS & WRONG QUESTION BREAKDOWN
	========================================================= */

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
		btnAll.className = state.activeReviewFilter === 'all' ? "px-4 py-2 text-xs font-extrabold rounded-lg bg-white text-navy-dark shadow-sm" : "px-4 py-2 text-xs font-extrabold rounded-lg text-slate-500 hover:bg-white/50";
	}
	if (btnInc) {
		btnInc.innerText = `Incorrect (${incorrectCount})`;
		btnInc.className = state.activeReviewFilter === 'incorrect' ? "px-4 py-2 text-xs font-extrabold rounded-lg bg-white text-rose-600 shadow-sm" : "px-4 py-2 text-xs font-extrabold rounded-lg text-rose-600 hover:bg-white/50";
	}
	if (btnCor) {
		btnCor.innerText = `Correct (${correctCount})`;
		btnCor.className = state.activeReviewFilter === 'correct' ? "px-4 py-2 text-xs font-extrabold rounded-lg bg-white text-emerald-600 shadow-sm" : "px-4 py-2 text-xs font-extrabold rounded-lg text-emerald-600 hover:bg-white/50";
	}

	let items = state.answerBreakdown;
	if (state.activeReviewFilter === 'incorrect') {
		items = items.filter(i => !i.isCorrect);
	} else if (state.activeReviewFilter === 'correct') {
		items = items.filter(i => i.isCorrect);
	}

	if (items.length === 0) {
		container.innerHTML = `
			<div class="text-center py-6 bg-slate-50 rounded-xl border border-slate-200">
				<p class="text-sm font-bold text-slate-500">No math questions match this filter selection.</p>
			</div>
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
			<div class="bg-white p-6 rounded-2xl review-card ${borderClass} space-y-4 shadow-sm">
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
			</div>
		`;
	});

	container.innerHTML = html;
}

function updateStepView() {
	const landingScreen = document.getElementById("landing-screen");
	const instructionsScreen = document.getElementById("instructions-screen");
	const examScreen = document.getElementById("exam-screen");
	const resultsScreen = document.getElementById("results-screen");

	if (landingScreen) landingScreen.classList.add("hidden");
	if (instructionsScreen) instructionsScreen.classList.add("hidden");
	if (examScreen) examScreen.classList.add("hidden");
	if (resultsScreen) resultsScreen.classList.add("hidden");

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
						<p class="text-sm text-slate-500 leading-relaxed">Solve math questions on scratch paper before selecting your answer.</p>
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
						<h4 class="font-bold text-navy-dark">Standards-Aligned Math</h4>
						<p class="text-sm text-slate-500 leading-relaxed">Covers fundamental core math domains from standard curricula.</p>
					</div>
					<div class="space-y-3 flex flex-col items-center">
						<span class="text-4xl">🔒</span>
						<h4 class="font-bold text-navy-dark">Secure Assessment</h4>
						<p class="text-sm text-slate-500 leading-relaxed">Encrypted student sessions, private math assessment, safe learning environment.</p>
					</div>
					<div class="space-y-3 flex flex-col items-center">
						<span class="text-4xl">💡</span>
						<h4 class="font-bold text-navy-dark">Personalized Results</h4>
						<p class="text-sm text-slate-500 leading-relaxed">Instant level mapping with clear mathematical feedback for parents.</p>
					</div>
					<div class="space-y-3 flex flex-col items-center">
						<span class="text-4xl">🏫</span>
						<h4 class="font-bold text-navy-dark">Educator Developed</h4>
						<p class="text-sm text-slate-500 leading-relaxed">Formulated by math teachers to yield accurate grade benchmarks.</p>
					</div>
				</div>
			`;
		}
	}

	if (state.currentStep === 1) {
		if (landingScreen) landingScreen.classList.remove("hidden");
	} else if (state.currentStep === 2) {
		if (instructionsScreen) instructionsScreen.classList.remove("hidden");
	} else if (state.currentStep === 3) {
		if (examScreen) examScreen.classList.remove("hidden");
		renderQuestion();
	} else if (state.currentStep === 4) {
		if (resultsScreen) resultsScreen.classList.remove("hidden");
		
		document.getElementById("placement-recommendation").innerText = state.recommendedLevel;
		document.getElementById("score-details").innerText = `You answered ${state.score} out of 15 questions correctly.`;
		const minutes = Math.floor(state.timeElapsed / 60);
		const seconds = state.timeElapsed % 60;
		document.getElementById("time-details").innerText = `Time elapsed: ${minutes} minute${minutes !== 1 ? 's' : ''} and ${seconds} second${seconds !== 1 ? 's' : ''}.`;

		const userStatus = document.getElementById("user-save-status");
		if (userStatus) {
			userStatus.innerText = `Math assessment linked to active student account: ${AuthManager.currentUser ? AuthManager.currentUser.username : ''}`;
		}

		renderFluidBreakdown();
	}
}

window.onload = function() {
	updateStepView();
};

window.addEventListener('beforeunload', (e) => {
	if (state.currentStep === 3 && !state.isExiting) {
		e.preventDefault();
		e.returnValue = '';
	}
});

document.addEventListener('click', (e) => {
	const anchor = e.target.closest('a');
	if (anchor && state.currentStep === 3) {
		e.preventDefault();
		state.pendingNavigationUrl = anchor.href;
		state.pendingNavigationTarget = anchor.target;
		openModal('exit-confirm-modal');
	}
});

function handleLogoClick() {
	if (state.currentStep === 3) {
		openModal('exit-confirm-modal');
	} else {
		state.currentStep = 1;
		updateStepView();
	}
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
		finishExam();
	}
}

/* ]]> */
</script>
