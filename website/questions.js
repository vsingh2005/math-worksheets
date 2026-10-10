let questions = [
  // --- GRADE 3 (ELEMENTARY EASY) ---
  {
    id: 101,
    grade: 3,
    domain: "Multiplication Concepts",
    text: "A bakery boxes donuts in groups of 6. If a customer buys 4 boxes, how many donuts do they get in total?",
    type: "multiple-choice",
    options: [
      { text: "24", correct: true },
      { text: "10", correct: false },
      { text: "18", correct: false },
      { text: "12", correct: false }
    ],
    explanation: "Multiply the number of boxes by the number of donuts per box: 4 x 6 = 24."
  },
  {
    id: 102,
    grade: 3,
    domain: "Multiplication Properties",
    text: "Which equation shows the Commutative Property of Multiplication?",
    type: "multiple-choice",
    options: [
      { text: "4 x 5 = 5 x 4", correct: true },
      { text: "4 x 5 = 20", correct: false },
      { text: "(4 x 2) x 5 = 4 x (2 x 5)", correct: false },
      { text: "4 x 0 = 0", correct: false }
    ],
    explanation: "The Commutative Property of Multiplication states that changing the order of factors does not change the product: a x b = b x a."
  },
  {
    id: 103,
    grade: 3,
    domain: "Division Concepts",
    text: "If 32 books are shared equally among 4 shelves, how many books go on each shelf?",
    type: "numeric-response",
    correctAnswer: "8",
    placeholder: "Enter number of books...",
    explanation: "Divide the total books by the number of shelves: 32 / 4 = 8 books per shelf."
  },
  {
    id: 104,
    grade: 3,
    domain: "Multiplication Facts",
    text: "Find the product: 7 x 8",
    type: "numeric-response",
    correctAnswer: "56",
    placeholder: "Enter product...",
    explanation: "Using multiplication facts, 7 groups of 8 is equal to 56."
  },
  {
    id: 105,
    grade: 3,
    domain: "Multi-Step Word Problems",
    text: "Jack has 5 boxes of pencils with 8 pencils in each box. He gives 12 pencils to his sister. How many pencils does Jack have left?",
    type: "multiple-choice",
    options: [
      { text: "28", correct: true },
      { text: "40", correct: false },
      { text: "20", correct: false },
      { text: "32", correct: false }
    ],
    explanation: "First find total pencils: 5 x 8 = 40. Then subtract what he gave away: 40 - 12 = 28."
  },
  {
    id: 106,
    grade: 3,
    domain: "Rounding Numbers",
    text: "Round 283 to the nearest hundred.",
    type: "numeric-response",
    correctAnswer: "300",
    placeholder: "Round to nearest hundred...",
    explanation: "The tens digit of 283 is 8 (which is 5 or more), so round up to the next hundred: 300."
  },
  {
    id: 107,
    grade: 3,
    domain: "Base-Ten Arithmetic",
    text: "Solve: 456 + 287",
    type: "numeric-response",
    correctAnswer: "743",
    placeholder: "Enter sum...",
    explanation: "Perform standard addition: 456 + 287 = 743."
  },
  {
    id: 108,
    grade: 3,
    domain: "Multiplying by Multiples of 10",
    text: "Multiply: 6 x 40",
    type: "numeric-response",
    correctAnswer: "240",
    placeholder: "Enter product...",
    explanation: "Multiply 6 by the tens digit (4) to get 24, then append the zero: 240."
  },
  {
    id: 109,
    grade: 3,
    domain: "Fraction Concepts",
    text: "A pizza is cut into 8 equal slices. If Emily eats 3 slices, what fraction of the pizza did she eat?",
    type: "multiple-choice",
    options: [
      { text: "3/8", correct: true },
      { text: "1/8", correct: false },
      { text: "5/8", correct: false },
      { text: "3/5", correct: false }
    ],
    explanation: "Emily ate 3 out of the 8 total equal parts, which is represented by the fraction 3/8."
  },
  {
    id: 110,
    grade: 3,
    domain: "Fractions as Whole Numbers",
    text: "Which fraction is equivalent to 1 whole?",
    type: "multiple-choice",
    options: [
      { text: "4/4", correct: true },
      { text: "1/4", correct: false },
      { text: "4/1", correct: false },
      { text: "2/4", correct: false }
    ],
    explanation: "A fraction where the numerator matches the denominator represents all parts of a single whole: 4/4 = 1."
  },
  {
    id: 111,
    grade: 3,
    domain: "Comparing Fractions",
    text: "Which comparison is true?",
    type: "multiple-choice",
    options: [
      { text: "1/3 > 1/4", correct: true },
      { text: "1/3 < 1/4", correct: false },
      { text: "1/3 = 1/4", correct: false },
      { text: "2/3 < 2/4", correct: false }
    ],
    explanation: "When comparing unit fractions (with a numerator of 1), the fraction with the smaller denominator has larger parts: 1/3 > 1/4."
  },
  {
    id: 112,
    grade: 3,
    domain: "Elapsed Time",
    text: "A movie starts at 4:15 PM and ends at 5:05 PM. How many minutes long was the movie?",
    type: "numeric-response",
    correctAnswer: "50",
    placeholder: "Enter duration in minutes...",
    explanation: "From 4:15 PM to 5:00 PM is 45 minutes. From 5:00 PM to 5:05 PM is 5 minutes. 45 + 5 = 50 minutes."
  },
  {
    id: 113,
    grade: 3,
    domain: "Measurement Units",
    text: "Which metric unit is best to measure the mass of a single paperclip?",
    type: "multiple-choice",
    options: [
      { text: "Grams (g)", correct: true },
      { text: "Kilograms (kg)", correct: false },
      { text: "Liters (L)", correct: false },
      { text: "Meters (m)", correct: false }
    ],
    explanation: "A single paperclip is very light, making Grams (g) the most appropriate metric unit of mass."
  },
  {
    id: 114,
    grade: 3,
    domain: "Area of Rectangles",
    text: "Find the area of a rectangle with a length of 7 cm and a width of 5 cm.",
    type: "numeric-response",
    correctAnswer: "35",
    placeholder: "Enter area in sq cm...",
    explanation: "Area of a rectangle is length times width: 7 cm x 5 cm = 35 square cm."
  },
  {
    id: 115,
    grade: 3,
    domain: "Perimeter of Polygons",
    text: "A square garden has a side length of 6 meters. What is its perimeter in meters?",
    type: "numeric-response",
    correctAnswer: "24",
    placeholder: "Enter perimeter in meters...",
    explanation: "A square has 4 equal sides. Perimeter = 4 x 6 meters = 24 meters."
  },

  // --- GRADE 4 (ELEMENTARY MEDIUM) ---
  {
    id: 201,
    grade: 4,
    domain: "Multiplicative Comparison",
    text: "A red hat costs $8. A blue jacket costs 6 times as much as the red hat. How much does the blue jacket cost in dollars?",
    type: "numeric-response",
    correctAnswer: "48",
    placeholder: "Enter price in dollars...",
    explanation: "Multiply the hat price by 6: 8 x 6 = $48."
  },
  {
    id: 202,
    grade: 4,
    domain: "Multi-Step Word Problems",
    text: "A classroom has 3 rows of desks with 8 desks in each row. The teacher adds 4 more desks. If the desks are grouped into sets of 4, how many sets are there?",
    type: "multiple-choice",
    options: [
      { text: "7", correct: true },
      { text: "8", correct: false },
      { text: "6", correct: false },
      { text: "9", correct: false }
    ],
    explanation: "Initial desks: 3 x 8 = 24. Total desks after adding 4: 24 + 4 = 28. Divided into sets of 4: 28 / 4 = 7 sets."
  },
  {
    id: 203,
    grade: 4,
    domain: "Factors & Multiples",
    text: "Identify the prime number from the following choices:",
    type: "multiple-choice",
    options: [
      { text: "17", correct: true },
      { text: "15", correct: false },
      { text: "9", correct: false },
      { text: "21", correct: false }
    ],
    explanation: "A prime number has only 1 and itself as factors. 17 is prime. 15 (3x5), 9 (3x3), and 21 (3x7) are composite."
  },
  {
    id: 204,
    grade: 4,
    domain: "Place Value Structures",
    text: "In the number 5,420, the value of the digit 5 is how many times larger than the digit 5 in the number 520?",
    type: "numeric-response",
    correctAnswer: "10",
    placeholder: "Enter multiplier...",
    explanation: "The 5 in 5,420 is in the thousands place (5,000) and the 5 in 520 is in the hundreds place (500). 5,000 is 10 times 500."
  },
  {
    id: 205,
    grade: 4,
    domain: "Rounding Large Numbers",
    text: "Round 45,782 to the nearest thousand.",
    type: "numeric-response",
    correctAnswer: "46000",
    placeholder: "Round to nearest thousand...",
    explanation: "The hundreds digit is 7 (which is >= 5), so round the thousands digit up: 46,000."
  },
  {
    id: 206,
    grade: 4,
    domain: "Multi-Digit Arithmetic",
    text: "Solve: 12,459 - 8,634",
    type: "numeric-response",
    correctAnswer: "3825",
    placeholder: "Enter difference...",
    explanation: "Perform standard multi-digit subtraction: 12,459 - 8,634 = 3,825."
  },
  {
    id: 207,
    grade: 4,
    domain: "Multi-Digit Multiplication",
    text: "Multiply: 24 x 15",
    type: "numeric-response",
    correctAnswer: "360",
    placeholder: "Enter product...",
    explanation: "24 x 15 = 360."
  },
  {
    id: 208,
    grade: 4,
    domain: "Division with Remainders",
    text: "Find the quotient and remainder: 125 divided by 4.",
    type: "multiple-choice",
    options: [
      { text: "31 R1", correct: true },
      { text: "31", correct: false },
      { text: "30 R5", correct: false },
      { text: "32 R1", correct: false }
    ],
    explanation: "4 goes into 125 exactly 31 times (31 x 4 = 124), with a remainder of 1 (125 - 124 = 1)."
  },
  {
    id: 209,
    grade: 4,
    domain: "Fraction Equivalence",
    text: "Which fraction is equivalent to 2/3?",
    type: "multiple-choice",
    options: [
      { text: "8/12", correct: true },
      { text: "4/9", correct: false },
      { text: "6/8", correct: false },
      { text: "5/6", correct: false }
    ],
    explanation: "Multiply the numerator and denominator of 2/3 by 4: (2 x 4) / (3 x 4) = 8/12."
  },
  {
    id: 210,
    grade: 4,
    domain: "Comparing Fractions",
    text: "Compare the fractions: 3/5 and 2/3. Which statement is correct?",
    type: "multiple-choice",
    options: [
      { text: "3/5 < 2/3", correct: true },
      { text: "3/5 > 2/3", correct: false },
      { text: "3/5 = 2/3", correct: false },
      { text: "2/3 < 3/5", correct: false }
    ],
    explanation: "Using a common denominator of 15: 3/5 = 9/15 and 2/3 = 10/15. Since 9/15 < 10/15, 3/5 < 2/3."
  },
  {
    id: 211,
    grade: 4,
    domain: "Decimal Fractions",
    text: "Add: 2/10 + 35/100. Write your answer as a decimal.",
    type: "numeric-response",
    correctAnswer: "0.55",
    placeholder: "Enter decimal value...",
    explanation: "Convert 2/10 to 20/100. Add: 20/100 + 35/100 = 55/100 = 0.55."
  },
  {
    id: 212,
    grade: 4,
    domain: "Fraction Multiplication",
    text: "A recipe requires 3/4 cup of sugar. If you make 5 batches, how many cups of sugar do you need?",
    type: "multiple-choice",
    options: [
      { text: "3 3/4", correct: true },
      { text: "15/4", correct: false },
      { text: "2 1/4", correct: false },
      { text: "3 1/4", correct: false }
    ],
    explanation: "Multiply 5 by 3/4: 5 x 3/4 = 15/4. Convert to a mixed number: 15/4 = 3 3/4."
  },
  {
    id: 213,
    grade: 4,
    domain: "Measurement Conversions",
    text: "Convert 4 kilometers into meters.",
    type: "numeric-response",
    correctAnswer: "4000",
    placeholder: "Enter meters...",
    explanation: "Since 1 kilometer = 1,000 meters, multiply 4 by 1,000: 4,000 meters."
  },
  {
    id: 214,
    grade: 4,
    domain: "Complementary Angles",
    text: "Angle A and Angle B are complementary (sum to 90 degrees). If Angle A is 27 degrees, what is the measure of Angle B in degrees?",
    type: "numeric-response",
    correctAnswer: "63",
    placeholder: "Enter degrees...",
    explanation: "Complementary angles sum to 90 degrees. So, Angle B = 90 - 27 = 63 degrees."
  },
  {
    id: 215,
    grade: 4,
    domain: "Geometric Terms",
    text: "Which geometric term describes lines that cross each other at a perfect 90-degree angle?",
    type: "multiple-choice",
    options: [
      { text: "Perpendicular lines", correct: true },
      { text: "Parallel lines", correct: false },
      { text: "Intersecting lines", correct: false },
      { text: "Ray lines", correct: false }
    ],
    explanation: "Lines that cross and form right (90-degree) angles are perpendicular."
  },

  // --- GRADE 5 (ELEMENTARY HARD) ---
  {
    id: 301,
    grade: 5,
    domain: "Numerical Expressions",
    text: "Evaluate the numerical expression: 3 x (8 - 2) + 4",
    type: "numeric-response",
    correctAnswer: "22",
    placeholder: "Enter value...",
    explanation: "Perform operations inside parentheses first: 8 - 2 = 6. Next, multiply: 3 x 6 = 18. Finally, add: 18 + 4 = 22."
  },
  {
    id: 302,
    grade: 5,
    domain: "Powers of 10",
    text: "What is the value of 10³?",
    type: "multiple-choice",
    options: [
      { text: "1,000", correct: true },
      { text: "100", correct: false },
      { text: "10,000", correct: false },
      { text: "30", correct: false }
    ],
    explanation: "10 raised to the power of 3 means multiplying 10 by itself three times: 10 x 10 x 10 = 1,000."
  },
  {
    id: 303,
    grade: 5,
    domain: "Rounding Decimals",
    text: "Round the decimal 14.568 to the nearest hundredth.",
    type: "numeric-response",
    correctAnswer: "14.57",
    placeholder: "Enter rounded decimal...",
    explanation: "The thousandths digit is 8 (which is >= 5), so round the hundredths digit up from 6 to 7: 14.57."
  },
  {
    id: 304,
    grade: 5,
    domain: "Multi-Digit Multiplication",
    text: "Find the product: 135 x 24",
    type: "numeric-response",
    correctAnswer: "3240",
    placeholder: "Enter product...",
    explanation: "Multiply the numbers: 135 x 24 = 3,240."
  },
  {
    id: 305,
    grade: 5,
    domain: "Multi-Digit Division",
    text: "Divide: 1,512 divided by 12",
    type: "numeric-response",
    correctAnswer: "126",
    placeholder: "Enter quotient...",
    explanation: "Perform long division: 1512 / 12 = 126."
  },
  {
    id: 306,
    grade: 5,
    domain: "Decimals Addition",
    text: "Solve: 24.5 + 8.76",
    type: "numeric-response",
    correctAnswer: "33.26",
    placeholder: "Enter sum...",
    explanation: "Align place values and add: 24.50 + 8.76 = 33.26."
  },
  {
    id: 307,
    grade: 5,
    domain: "Decimals Division",
    text: "Divide: 4.8 divided by 0.6",
    type: "numeric-response",
    correctAnswer: "8",
    placeholder: "Enter quotient...",
    explanation: "4.8 / 0.6 is equivalent to 48 / 6, which equals 8."
  },
  {
    id: 308,
    grade: 5,
    domain: "Adding Fractions",
    text: "Solve: 1/2 + 2/5",
    type: "multiple-choice",
    options: [
      { text: "9/10", correct: true },
      { text: "3/7", correct: false },
      { text: "3/10", correct: false },
      { text: "4/5", correct: false }
    ],
    explanation: "Find a common denominator of 10: 1/2 = 5/10 and 2/5 = 4/10. Add: 5/10 + 4/10 = 9/10."
  },
  {
    id: 309,
    grade: 5,
    domain: "Subtracting Mixed Numbers",
    text: "Subtract: 3 1/4 - 1 1/2",
    type: "multiple-choice",
    options: [
      { text: "1 3/4", correct: true },
      { text: "2 1/4", correct: false },
      { text: "1 1/4", correct: false },
      { text: "2 3/4", correct: false }
    ],
    explanation: "Convert to improper fractions: 13/4 - 3/2 = 13/4 - 6/4 = 7/4. Convert back to mixed number: 1 3/4."
  },
  {
    id: 310,
    grade: 5,
    domain: "Fractions as Division",
    text: "Three friends share 4 identical sub sandwiches equally. How much sandwich does each friend receive?",
    type: "multiple-choice",
    options: [
      { text: "4/3 sandwich", correct: true },
      { text: "3/4 sandwich", correct: false },
      { text: "1 1/4 sandwich", correct: false },
      { text: "1/3 sandwich", correct: false }
    ],
    explanation: "Dividing 4 sandwich wholes among 3 people is represented by the division problem 4 / 3, which is 4/3 sandwiches."
  },
  {
    id: 311,
    grade: 5,
    domain: "Multiplying Fractions",
    text: "Multiply: 2/3 x 4/5. Write your answer as a fraction (e.g., 8/15).",
    type: "numeric-response",
    correctAnswer: "8/15",
    placeholder: "Enter fraction...",
    explanation: "Multiply numerators and multiply denominators: (2 x 4) / (3 x 5) = 8/15."
  },
  {
    id: 312,
    grade: 5,
    domain: "Dividing Fractions",
    text: "Divide: 1/3 divided by 4. Write your answer as a fraction (e.g., 1/12).",
    type: "numeric-response",
    correctAnswer: "1/12",
    placeholder: "Enter fraction...",
    explanation: "Dividing by 4 is the same as multiplying by 1/4: (1/3) x (1/4) = 1/12."
  },
  {
    id: 313,
    grade: 5,
    domain: "Volume of Prisms",
    text: "A rectangular jewelry box has a length of 8 cm, a width of 5 cm, and a height of 3 cm. Find its volume in cubic cm.",
    type: "numeric-response",
    correctAnswer: "120",
    placeholder: "Enter volume...",
    explanation: "Volume is length x width x height: 8 cm x 5 cm x 3 cm = 120 cubic cm."
  },
  {
    id: 314,
    grade: 5,
    domain: "Coordinate Geometry",
    text: "What are the coordinates of the origin on the coordinate plane?",
    type: "multiple-choice",
    options: [
      { text: "(0, 0)", correct: true },
      { text: "(1, 1)", correct: false },
      { text: "(0, 1)", correct: false },
      { text: "(1, 0)", correct: false }
    ],
    explanation: "The origin is where the horizontal x-axis and vertical y-axis intersect, defined by coordinates (0, 0)."
  },
  {
    id: 315,
    grade: 5,
    domain: "Classifying 2D Shapes",
    text: "Which statement is true?",
    type: "multiple-choice",
    options: [
      { text: "All squares are rectangles", correct: true },
      { text: "All rectangles are squares", correct: false },
      { text: "No trapezoid is a quadrilateral", correct: false },
      { text: "All rhombuses are squares", correct: false }
    ],
    explanation: "A square is defined as a regular quadrilateral having 4 equal sides and 4 right angles. Since a rectangle requires 4 right angles, all squares are rectangles."
  },
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
    text: "Solve the inequality: 2x - 5> 7",
    type: "multiple-choice",
    options: [
      { text: "x> 6", correct: true },
      { text: "x> 1", correct: false },
      { text: "x <6", correct: false },
      { text: "x> 12", correct: false }
    ],
    explanation: "Add 5 to both sides: 2x> 12. Divide both sides by 2: x> 6."
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
    text: "Find the volume of a cylinder with radius 3 cm and height 10 cm. (Leave in terms of π, e.g. write 50pi)",
    type: "numeric-response",
    correctAnswer: "90pi",
    placeholder: "Enter volume (e.g. 50pi)...",
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
    explanation: "Move decimal 6 places left to form 6.2. Since 6,200,000> 1, the exponent is positive: 6.2 × 10⁶."
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
