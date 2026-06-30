import os

base_dir = r"c:\Users\singh\Downloads\math_worksheets_repo\8th_standard"

questions_data = {
    21: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Pythagorean Theorem}

\medskip
\textbf{The Theorem:} For any right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides (the legs).
$$ a^2 + b^2 = c^2 $$
- **Legs ($a$ and $b$):** The two shorter sides that form the right angle.
- **Hypotenuse ($c$):** The longest side, directly across from the right angle.

\textbf{How to use it:}
- \textbf{Finding the Hypotenuse ($c$):} Plug in $a$ and $b$, square them, add them, then take the square root. 
  Example: $a=3, b=4$. $3^2 + 4^2 = c^2 \rightarrow 9 + 16 = 25 = c^2 \rightarrow c = 5$.
- \textbf{Finding a Leg ($a$ or $b$):} Plug in the known leg and the hypotenuse $c$. Square them, subtract the leg's square from $c^2$, then take the square root.
  Example: $a=6, c=10$. $6^2 + b^2 = 10^2 \rightarrow 36 + b^2 = 100 \rightarrow b^2 = 64 \rightarrow b = 8$.

\textbf{Converse of the Theorem:} If $a^2 + b^2 = c^2$ for any triangle, then the triangle MUST be a right triangle.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Find $c$ if $a=5$ and $b=12$. \vspace{1.5cm}

\textbf{2.} Find $a$ if $b=15$ and $c=17$. \vspace{1.5cm}

\textbf{3.} Is a triangle with sides $7, 24, 25$ a right triangle? \vspace{1.5cm}

\textbf{4.} A ladder is $13\text{ ft}$ long. Its base is $5\text{ ft}$ from the wall. How high up the wall does it reach? \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} The hypotenuse is always:
A) The shortest side B) The side adjacent to the right angle C) The longest side

\item \textbf{[MC]} The Pythagorean Theorem only applies to:
A) Isosceles triangles B) Right triangles C) Scalene triangles

\item Find $c$ if $a=6, b=8$. $c=$ \blank
\item Find $c$ if $a=9, b=12$. $c=$ \blank
\item Find $c$ if $a=8, b=15$. $c=$ \blank
\item Find $b$ if $a=7, c=25$. $b=$ \blank
\item Find $a$ if $b=24, c=26$. $a=$ \blank
\item Find $b$ if $a=3, c=5$. $b=$ \blank
\item Is a triangle with sides $5, 12, 13$ a right triangle? (Yes/No) \blank
\item Is a triangle with sides $4, 5, 6$ a right triangle? (Yes/No) \blank
\item Is a triangle with sides $9, 40, 41$ a right triangle? (Yes/No) \blank
\item Does $1^2 + 1^2 = 2^2$? (Yes/No) \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item A rectangular TV screen has a width of $40\text{ inches}$ and a height of $30\text{ inches}$. TVs are measured by their diagonal length. What is the size of this TV?

\item A baseball diamond is a square with $90\text{ ft}$ sides. How far is it from home plate to second base? (Round to one decimal place).

\item A right triangle has a hypotenuse of $20\text{ cm}$. One leg is twice as long as the other. Let the legs be $x$ and $2x$. Set up the Pythagorean Theorem to find the exact lengths of the legs.

\item You are building a wooden ramp. The ramp needs to be $10\text{ feet}$ long (the slanted part) and rise $2\text{ feet}$ off the ground. How far out from the starting point will the base of the ramp extend horizontally? (Round to one decimal place).

\item Determine if the set of numbers $\{10, 24, 26\}$ forms a Pythagorean Triple. Show your mathematical proof.

\item Why is the Converse of the Pythagorean Theorem important in construction and carpentry? How would a builder use the numbers 3, 4, and 5?

\item A cone has a radius of $5\text{ cm}$ and a height of $12\text{ cm}$. Draw the cone and draw a right triangle inside it. What is the "slant height" (the hypotenuse) of the cone?
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A spider is on the floor in the corner of a rectangular room measuring $12\text{ ft}$ by $16\text{ ft}$. The spider wants to crawl to the ceiling in the exact opposite corner. The room is $10\text{ ft}$ high. 
a) First, calculate the diagonal distance across the floor.
b) Use that floor diagonal as a leg in a new right triangle to find the 3D diagonal distance from the bottom corner to the top opposite corner. 

\item Two ships leave a port at the same time. Ship A sails North at $15\text{ miles per hour}$. Ship B sails East at $20\text{ miles per hour}$. After 3 hours, how far apart are the two ships? Draw a diagram and show all work.

\item A flagpole is $30\text{ feet}$ tall. A wire is attached from the top of the pole to a stake in the ground. The stake is $16\text{ feet}$ from the base of the pole. The wire breaks $10\text{ feet}$ from the top. Assuming the bottom part of the wire stays straight and taut, how far is the broken end from the stake? (Hint: find the total length of the wire first).

\item A right triangle has an area of $30\text{ cm}^2$. The two legs have lengths that are consecutive even integers (e.g., $x$ and $x+2$). 
a) Use the area formula ($A = \frac{1}{2}bh$) to find the lengths of the two legs.
b) Once you have the legs, use the Pythagorean Theorem to find the length of the hypotenuse.
\end{enumerate}
\vspace{1cm}
"""
    },
    22: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Distance on the Coordinate Plane}

\medskip
\textbf{Using the Pythagorean Theorem:} You can find the distance between any two points $(x_1, y_1)$ and $(x_2, y_2)$ on a graph by drawing a right triangle.
1. Plot the two points.
2. Draw a horizontal line from one point and a vertical line from the other to form a right angle.
3. The length of the horizontal leg is the difference in $x$-values ($x_2 - x_1$).
4. The length of the vertical leg is the difference in $y$-values ($y_2 - y_1$).
5. Use $a^2 + b^2 = c^2$ to find the hypotenuse, which is the distance!

\textbf{The Distance Formula:} The Distance Formula is just the Pythagorean Theorem rewritten for coordinates:
$$ d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} $$

\vspace{2mm}
\textbf{Example:} Find the distance between $(1, 2)$ and $(4, 6)$.
\textit{Horizontal Leg (Run):} $4 - 1 = 3$.
\textit{Vertical Leg (Rise):} $6 - 2 = 4$.
\textit{Hypotenuse:} $3^2 + 4^2 = c^2 \rightarrow 9 + 16 = 25 = c^2 \rightarrow c = 5$.
The distance is 5 units.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Find the distance between $(0, 0)$ and $(6, 8)$. \vspace{1cm}

\textbf{2.} Find the distance between $(2, 3)$ and $(7, 15)$. \vspace{1cm}

\textbf{3.} Find the distance between $(-4, 1)$ and $(4, 7)$. \vspace{1cm}

\textbf{4.} How is the distance formula related to the slope formula? \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} The horizontal distance between $(2, 5)$ and $(8, 5)$ is:
A) 3 B) 5 C) 6 D) 10

\item \textbf{[MC]} The vertical distance between $(4, -2)$ and $(4, 7)$ is:
A) 5 B) 9 C) -5 D) 0

\item Distance between $(0,0)$ and $(3,4)$: \blank
\item Distance between $(1,1)$ and $(4,5)$: \blank
\item Distance between $(5,2)$ and $(10,14)$: \blank
\item Distance between $(-2,-3)$ and $(3,9)$: \blank
\item Distance between $(0,-5)$ and $(12,0)$: \blank
\item Distance between $(-6,2)$ and $(2,17)$: \blank
\item Calculate $(x_2 - x_1)^2$ for $(-1, 4)$ and $(5, 6)$: \blank
\item Calculate $(y_2 - y_1)^2$ for $(-1, 4)$ and $(5, 6)$: \blank
\item True or False: Distance can be a negative number. \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item A triangle has vertices at $A(1, 2), B(1, 6),$ and $C(4, 2)$. Draw a sketch. Is this a right triangle? Calculate the perimeter of the triangle.

\item Find the length of the line segment connecting $(-5, -5)$ and $(5, 5)$. (Leave in simplest radical form or decimal rounded to one place).

\item A circle is drawn on a coordinate plane with its center at the origin $(0,0)$. The point $(8, 15)$ lies on the circle. What is the radius of the circle?

\item Prove that the triangle with vertices $X(-2, 1), Y(2, 4),$ and $Z(6, 1)$ is an isosceles triangle by calculating the lengths of all three sides.

\item A quadrilateral has vertices $P(0,0), Q(5,0), R(5,5),$ and $S(0,5)$. What shape is this? Calculate the length of the diagonal $PR$.

\item What happens to the distance between two points if you double both the horizontal distance and the vertical distance? (Test it with $(0,0)$ to $(3,4)$ vs $(0,0)$ to $(6,8)$).
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A map is laid out on a coordinate plane where each unit represents 1 mile. A drone takes off from a base at $(-12, 5)$. It flies in a straight line to a drop point at $(12, 12)$, drops a package, and then flies in a straight line to a charging station at $(20, -3)$. Calculate the total distance the drone flew. 

\item You are designing a video game. An enemy is located at $(15, 20)$. Your character's weapon has a maximum range of 25 units. The character is currently at $(-5, 10)$. Are you close enough to hit the enemy? Show your calculations. By how many units do you need to move closer (or how much extra range do you have)?

\item Consider the three points $A(2, 4), B(6, 7),$ and $C(10, 10)$. Calculate the distance from A to B, the distance from B to C, and the distance from A to C. What do you notice about these three distances? What does this tell you about the geometry of the three points?

\item A circle has a center at $(3, -4)$. A point on the edge of the circle is $(8, -4)$. Use the distance formula to find the radius. Then, determine if the point $(0, 0)$ is inside the circle, on the circle, or outside the circle. (Hint: compare the distance from the center to the origin against the radius).
\end{enumerate}
\vspace{1cm}
"""
    },
    23: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Rational vs Irrational Numbers}

\medskip
\textbf{Rational Numbers:} Any number that can be written as a perfect fraction $\frac{a}{b}$ (where $a$ and $b$ are integers and $b \neq 0$).
- Integers: $5, -12, 0$ (because $5 = 5/1$).
- Terminating Decimals: $0.75$ (because it's $3/4$).
- Repeating Decimals: $0.333...$ (because it's $1/3$).
- Perfect Squares: $\sqrt{25} = 5$.

\textbf{Irrational Numbers:} Numbers that CANNOT be written as a simple fraction. Their decimal expansions go on forever \textbf{without repeating} or terminating.
- Famous examples: $\pi$ ($3.14159...$)
- Non-perfect square roots: $\sqrt{2}, \sqrt{3}, \sqrt{10}$.

\vspace{2mm}
\textbf{Example 1:} Is $0.8$ rational or irrational?
\textit{Solution:} It's a terminating decimal ($8/10 = 4/5$). It is \textbf{Rational}.
\textbf{Example 2:} Is $\sqrt{20}$ rational or irrational?
\textit{Solution:} 20 is not a perfect square. The decimal is $4.47213...$ It is \textbf{Irrational}.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Classify as Rational or Irrational: $\sqrt{36}$. \vspace{1cm}

\textbf{2.} Classify as Rational or Irrational: $0.121212...$ \vspace{1cm}

\textbf{3.} Classify as Rational or Irrational: $\sqrt{15}$. \vspace{1cm}

\textbf{4.} Convert the repeating decimal $0.555...$ into a fraction. \vspace{1.5cm}

\textbf{5.} Why is $\pi$ irrational, even though some people use $22/7$ for it? \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} Which of the following is an irrational number?
A) $\sqrt{49}$ B) $0.25$ C) $\pi$ D) $1/3$

\item \textbf{[MC]} Every repeating decimal is a:
A) Rational Number B) Irrational Number C) Integer

\item Rational or Irrational: $\sqrt{81}$ \blank
\item Rational or Irrational: $4.5$ \blank
\item Rational or Irrational: $\sqrt{12}$ \blank
\item Rational or Irrational: $\frac{2}{7}$ \blank
\item Rational or Irrational: $0.33333...$ \blank
\item Rational or Irrational: $3.14159...$ (without pattern) \blank
\item Convert to a fraction: $0.8 = $ \blank
\item Convert to a fraction: $0.111... = $ \blank
\item Rational or Irrational: $0$ \blank
\item Rational or Irrational: $\sqrt{2}$ \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Explain why the square root of 64 is rational, but the square root of 65 is irrational.

\item Convert the repeating decimal $0.777...$ into a fraction using the algebraic method (Let $x = 0.777...$).

\item Convert the repeating decimal $0.454545...$ into a fraction using the algebraic method (Multiply by 100).

\item True or False: The sum of a rational number and an irrational number is always irrational. Provide an example to support your claim (e.g., $2 + \pi$).

\item Is the product of two irrational numbers always irrational? (Hint: think about $\sqrt{2} \cdot \sqrt{2}$). Explain.

\item Classify the number $\frac{\sqrt{25}}{2}$ as rational or irrational, and explain why.

\item Place the following numbers on a rough number line: $0, 1, 2, 3, 4, \pi, \sqrt{2}, \sqrt{9}, 3.5$
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item You are designing a square garden. You want the area of the garden to be exactly $50\text{ square meters}$. What is the exact length of one side of the garden? Is this side length a rational or irrational number? If you wanted the side length to be rational, what is the closest integer area you could choose?

\item Prove algebraically that the repeating decimal $0.123123123...$ is a rational number by converting it into a fraction in simplest form.

\item A carpenter is cutting a diagonal brace for a rectangular gate. The gate is $3\text{ feet}$ wide and $4\text{ feet}$ tall. He calculates the diagonal and gets a number. Is the length of the diagonal rational or irrational? Now, suppose the gate was $3\text{ feet}$ wide and $5\text{ feet}$ tall. Is the new diagonal length rational or irrational? Explain the difference.

\item Consider the equation $x^2 = 10$. Solve for $x$. Is $x$ rational or irrational? Now consider $x^3 = 8$. Solve for $x$. Is $x$ rational or irrational? Generalize a rule about taking roots of numbers that are not perfect powers.
\end{enumerate}
\vspace{1cm}
"""
    },
    24: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Estimating Radicals}

\medskip
\textbf{Estimating Square Roots:} When you have an irrational square root like $\sqrt{30}$, you can estimate its value by finding the perfect squares it sits between.
- The perfect square below 30 is 25 ($\sqrt{25} = 5$).
- The perfect square above 30 is 36 ($\sqrt{36} = 6$).
Therefore, $\sqrt{30}$ must be between 5 and 6.

\textbf{Getting more precise:} 
Because 30 is almost exactly halfway between 25 and 36, $\sqrt{30}$ is approximately $5.5$. 
If it was $\sqrt{26}$ (very close to 25), it would be approx $5.1$.
If it was $\sqrt{35}$ (very close to 36), it would be approx $5.9$.

\textbf{Cube Roots:} The concept is the same! Find the perfect cubes.
Example: $\sqrt[3]{30}$. Perfect cubes are $2^3=8$ and $3^3=27$ and $4^3=64$. 
So $\sqrt[3]{30}$ is slightly more than 3.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Between what two consecutive integers does $\sqrt{50}$ lie? \vspace{1cm}

\textbf{2.} Between what two consecutive integers does $\sqrt{10}$ lie? \vspace{1cm}

\textbf{3.} Estimate $\sqrt{80}$ to one decimal place. \vspace{1cm}

\textbf{4.} Which is greater: $\sqrt{20}$ or $4.5$? \vspace{1cm}

\textbf{5.} Between what two integers does $\sqrt[3]{10}$ lie? \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} $\sqrt{40}$ is between which two integers?
A) 5 and 6 B) 6 and 7 C) 7 and 8

\item \textbf{[MC]} Which is the best estimate for $\sqrt{95}$?
A) 9.1 B) 9.7 C) 10.2

\item $\sqrt{15}$ is between \blank and \blank.
\item $\sqrt{70}$ is between \blank and \blank.
\item $\sqrt{110}$ is between \blank and \blank.
\item $\sqrt{5}$ is between \blank and \blank.
\item Estimate $\sqrt{26}$ to one decimal place: \blank
\item Estimate $\sqrt{99}$ to one decimal place: \blank
\item Which is greater? $\sqrt{18}$ or $4$ \blank
\item Which is greater? $\sqrt{30}$ or $6$ \blank
\item $\sqrt[3]{9}$ is between \blank and \blank.
\item $\sqrt[3]{30}$ is between \blank and \blank.
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Place the following numbers on a number line: $\sqrt{10}, 3.5, \sqrt{17}, 4.1$. Show your reasoning for each placement.

\item A square room has an area of $75\text{ square feet}$. You need to buy baseboards for the perimeter. Estimate the length of one side to the nearest tenth. What is the approximate perimeter?

\item Without using a calculator, determine if $5.8$ is a good estimate for $\sqrt{34}$. (Hint: square $5.8$ or think about distance between perfect squares).

\item Which is a better estimate for $\sqrt{60}$: $7.4$ or $7.7$? Explain your reasoning based on the perfect squares 49 and 64.

\item Estimate the value of $-\sqrt{20}$. Between what two negative integers does it lie?

\item A cube has a volume of $100\text{ cm}^3$. Between what two integers is the length of one edge? Estimate it to one decimal place.

\item Solve for $x$: $x^2 = 45$. Estimate the value of $x$. Don't forget there are two answers!
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item You are trying to fit a circular table through a rectangular doorway. The doorway is $36\text{ inches}$ wide and $80\text{ inches}$ tall. The circular table has a diameter of $86\text{ inches}$. If you tilt the table, the maximum width you can fit through the door is equal to the diagonal of the doorway. Calculate the diagonal of the doorway (using Pythagorean theorem), estimate the square root to one decimal place, and determine if the table will fit.

\item The speed of a tsunami (in meters per second) can be modeled by the equation $s = \sqrt{9.8d}$, where $d$ is the depth of the ocean in meters. If an earthquake occurs at a depth of $4,000\text{ meters}$, the speed is $\sqrt{39,200}$. Estimate this speed to the nearest whole number without a calculator. (Hint: look for perfect squares near 392, like $20^2=400$).

\item Compare these three numbers: $2\pi$, $\sqrt{40}$, and $6.3$. Order them from least to greatest. Show your estimation process for each. 

\item The surface area of a sphere is $S = 4\pi r^2$. A balloon has a surface area of $200\text{ sq inches}$. Estimate the radius $r$ of the balloon. (Use $\pi \approx 3$). Show your algebraic steps and your square root estimation.
\end{enumerate}
\vspace{1cm}
"""
    },
    25: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: 8th Grade Capstone Review}

\medskip
\textbf{Congratulations!} You've reached the end of the 8th grade curriculum. This lesson ties together the major concepts you've learned to prepare you for high school Algebra and Geometry.

\textbf{Core Concepts to Master:}
1. \textbf{Equations & Systems:} Solving multi-step equations ($3x+2=14$), identifying number of solutions, and solving systems by graphing or algebra.
2. \textbf{Linear Functions:} Understanding $y=mx+b$, calculating slope, identifying proportional relationships, and constructing models from word problems.
3. \textbf{Geometry:} The Pythagorean Theorem ($a^2+b^2=c^2$), Volumes of Cylinders/Cones/Spheres, and Transformations (Translations, Reflections, Rotations, Dilations).
4. \textbf{Number System:} Rational vs Irrational numbers, exponent rules ($x^a \cdot x^b = x^{a+b}$), and scientific notation.
5. \textbf{Data:} Scatter plots, lines of best fit, and two-way frequency tables.

\vspace{2mm}
\textit{Use Worksheet 0 as a reference sheet. Worksheets 1-3 will pull questions from across the entire year to test your retention and problem-solving skills.}
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} (Algebra) Solve: $2(x-3) = 4x + 10$. \vspace{1.5cm}

\textbf{2.} (Functions) Find the slope between $(-2, 4)$ and $(3, 14)$. \vspace{1.5cm}

\textbf{3.} (Geometry) Find the hypotenuse if legs are $6$ and $8$. \vspace{1.5cm}

\textbf{4.} (Numbers) Simplify $(x^4 \cdot x^3) / x^2$. \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} Which equation is NOT a function?
A) $y = 3x$ B) $y = x^2$ C) $x = 5$ D) $y = 5$

\item \textbf{[MC]} A translation does what to a shape?
A) Flips it B) Slides it C) Spins it D) Shrinks it

\item Solve: $5x - 2 = 13$. $x =$ \blank
\item Solve: $x/4 + 1 = 5$. $x =$ \blank
\item State the slope: $y = -7x + 2$. $m =$ \blank
\item Find slope between $(0,0)$ and $(5, 10)$. $m =$ \blank
\item Write $3,200,000$ in scientific notation: \blank
\item Simplify: $a^5 \cdot a^{-2} =$ \blank
\item Is $\sqrt{20}$ rational or irrational? \blank
\item Estimate $\sqrt{50}$ to nearest whole number: \blank
\item A cylinder has $r=2, h=5$. Exact volume: \blank
\item If two lines have the same slope, the system has \blank solutions.
\item Translate $(3,4)$ up 2, left 1. New point: \blank
\item Dilate $(2, 5)$ by scale factor 3. New point: \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item \textbf{(Systems)} Solve the system using any method: $y = 2x + 4$ and $y = -x + 10$.

\item \textbf{(Geometry)} A triangle has vertices at $(0,0), (3,0),$ and $(0,4)$. What is the perimeter? (Hint: use Pythagorean Theorem for the hypotenuse).

\item \textbf{(Functions)} A gym charges a $\$50$ sign-up fee plus $\$20$ per month. Write the linear model. How much does 6 months cost?

\item \textbf{(Exponents)} The distance to a star is $4 \times 10^{12}\text{ km}$. A probe travels at $2 \times 10^4\text{ km/hr}$. How many hours will it take to reach the star? (Divide distance by speed).

\item \textbf{(Transformations)} Describe a sequence of two transformations that maps a triangle in Quadrant I to a congruent triangle in Quadrant III.

\item \textbf{(Data)} In a class of 30, 20 like math and 15 like science. 10 like both. Draw a two-way table. What is the relative frequency of liking science given that a student likes math?

\item \textbf{(Equations)} Solve for $x$: $\frac{1}{2}(4x - 8) = 2x - 4$. State the number of solutions.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Capstone Challenges (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item \textbf{(The Architecture Problem)} You are designing a cylindrical water tower. The tank must hold exactly $4,000\pi\text{ cubic feet}$ of water. To paint the outside (curved surface only, not the top/bottom), the paint costs $\$2$ per square foot. (Surface area of cylinder curve $= 2\pi r h$). If you choose a radius of $10\text{ feet}$, find the required height. Then calculate the total cost to paint the tower.

\item \textbf{(The Physics Problem)} Two trains leave stations that are $300\text{ miles}$ apart, heading directly toward each other. Train A travels at $60\text{ mph}$. Train B travels at $90\text{ mph}$. Write a system of equations for their distance from Station A over time. Solve the system to find out exactly how many hours it takes for them to crash, and how far they are from Station A.

\item \textbf{(The Finance Problem)} You have $\$10,000$. Bank A offers a simple proportional interest of $\$500$ per year ($y = 500x + 10000$). Bank B offers an equation $y = 1000x + 8000$. Bank C offers a compound non-linear interest $y = 10000(1.05)^x$. 
a) At what year do Bank A and Bank B have the exact same amount?
b) Evaluate Bank C at year 2. Is it a linear function? Explain why.

\item \textbf{(The Geometry Proof)} A large square has side length $(a+b)$. Inside it are 4 identical right triangles with legs $a$ and $b$, and hypotenuse $c$. This leaves a smaller tilted square inside with area $c^2$. The area of the large square is $(a+b)^2 = a^2 + 2ab + b^2$. The area of the 4 triangles is $4(\frac{1}{2}ab) = 2ab$. By setting the large area equal to the sum of the inner pieces ($4 \text{ triangles} + \text{inner square}$), prove the Pythagorean Theorem.
\end{enumerate}
\vspace{1cm}
"""
    }
}

for lesson_num, ws_data in questions_data.items():
    folders = [d for d in os.listdir(base_dir) if d.startswith(f"Lesson_{lesson_num}_")]
    if not folders:
        continue
    folder_name = folders[0]
    
    for ws_num, content_block in ws_data.items():
        file_path = os.path.join(base_dir, folder_name, f"8_{lesson_num}_{ws_num}.tex")
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
            
        if ws_num == 0:
            parts = file_content.split(r"\begin{tcolorbox}[colback=white, colframe=black!25")
            if len(parts) == 2:
                new_content = parts[0] + content_block + "\n\\end{document}\n"
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
        else:
            search_str = r"\begin{tcolorbox}[colback=customteal!20]"
            parts = file_content.split(search_str)
            if len(parts) >= 2:
                new_content = parts[0] + content_block + "\n\\end{document}\n"
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                    
print("Successfully injected EXPANDED custom questions for Lessons 21-25.")
