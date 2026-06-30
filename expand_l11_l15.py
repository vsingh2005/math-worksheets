import os

base_dir = r"c:\Users\singh\Downloads\math_worksheets_repo\8th_standard"

questions_data = {
    11: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Solving Systems by Graphing}

\medskip
\textbf{System of Equations:} A set of two or more equations with the same variables. To "solve" a system means to find the $(x, y)$ coordinate that makes BOTH equations true.

\textbf{Solving by Graphing:}
1. Ensure both equations are in slope-intercept form ($y = mx + b$).
2. Graph the first line using its $y$-intercept and slope.
3. Graph the second line on the same coordinate plane.
4. \textbf{Find the intersection point.} The coordinate $(x, y)$ where they cross is the solution!

\textbf{Types of Solutions:}
- \textbf{One Solution:} The lines intersect at exactly one point (different slopes).
- \textbf{No Solution:} The lines are parallel and never intersect (same slope, different $y$-intercepts).
- \textbf{Infinite Solutions:} The lines are exactly the same (same slope, same $y$-intercept).

\vspace{2mm}
\textbf{Example:} Solve the system $y = 2x + 1$ and $y = -x + 4$.
\textit{Graph Line 1:} Start at 1, go up 2, right 1.
\textit{Graph Line 2:} Start at 4, go down 1, right 1.
\textit{Intersection:} They cross at $(1, 3)$. 
Check: $3 = 2(1)+1$ (True). $3 = -(1)+4$ (True).
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} How many solutions does a system have if the lines are parallel? \vspace{1cm}

\textbf{2.} Is $(2, 5)$ a solution to $y = 3x - 1$ and $y = x + 3$? Show your check. \vspace{1.5cm}

\textbf{3.} Without graphing, how many solutions does this system have? $y = 4x - 2$ and $y = 4x + 5$. \vspace{1.5cm}

\textbf{4.} Graph $y = x$ and $y = -x + 2$. What is the solution? \vspace{2.0cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} The solution to a graphed system of equations is:
A) The $x$-intercept B) The $y$-intercept C) The intersection point D) The slope

\item \textbf{[MC]} If two lines have the same slope and different $y$-intercepts, they have:
A) 1 solution B) No solution C) Infinite solutions

\item Is $(1, 4)$ a solution to $y = 2x + 2$ and $y = -x + 5$? (Yes/No) \blank
\item Is $(0, 0)$ a solution to $y = x$ and $y = 3x$? (Yes/No) \blank
\item Is $(-2, 3)$ a solution to $y = -2x - 1$ and $y = x + 5$? (Yes/No) \blank
\item What is the solution if two lines cross at the origin? \blank
\item Line A: $y = 5x + 2$. Line B: $y = 5x + 2$. Solutions? \blank
\item Line A: $y = 2x - 1$. Line B: $y = 2x + 4$. Solutions? \blank
\item Line A: $y = \frac{1}{2}x$. Line B: $y = -x + 3$. How many solutions? \blank
\item To graph $2x + y = 6$, first rewrite it as: $y = $ \blank
\item To graph $y - 3x = 4$, first rewrite it as: $y = $ \blank
\item The lines $x = 4$ and $y = 2$ intersect at: \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Graph the system on a coordinate plane and find the solution: 
$y = -2x + 4$ 
$y = x - 5$

\item Graph the system on a coordinate plane and find the solution:
$y = \frac{1}{2}x - 2$
$y = -\frac{1}{2}x + 2$

\item Rewrite both equations in slope-intercept form, then determine the number of solutions without graphing:
$3x + y = 7$
$6x + 2y = 10$

\item Rewrite both equations in slope-intercept form, then determine the number of solutions without graphing:
$-x + y = 4$
$2y = 2x + 8$

\item A system has the solution $(3, -2)$. Write two different linear equations that intersect at this exact point.

\item Why is graphing not always the most accurate method to solve a system of equations? Give an example of a solution that would be hard to read on a graph.

\item Graph $x = -3$ and $y = 2x + 5$. What is the intersection point?

\item Determine if the system $y = 1.5x - 4$ and $3y = 4.5x - 12$ has one, none, or infinite solutions. Prove it mathematically.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item Two rival companies offer cloud storage. Company A charges a $\$10$ setup fee plus $\$2$ per month. Company B has no setup fee but charges $\$4$ per month. Write a system of equations. Graph them to find the break-even point (when they cost the same). Explain what the solution means for a customer.

\item A small theater sells adult tickets for $\$10$ and child tickets for $\$5$. One evening, they sold a total of 20 tickets and made $\$160$. Let $x$ be adult tickets and $y$ be child tickets. Write the system of equations. Rewrite the equations in $y=mx+b$ form, graph them, and find how many of each ticket were sold.

\item Two cars start at different positions on a highway. Car 1 starts at mile marker 10 and drives $60\text{ mph}$. Car 2 starts at mile marker 40 and drives $50\text{ mph}$. Write the system of equations. At what time ($x$) will Car 1 catch up to Car 2, and at what mile marker ($y$)? (Solve by analyzing the equations or graphing).

\item Construct a system of equations that has NO solution, where one equation is $2y = 8x - 12$. Explain how you built the second equation to guarantee they will never intersect.

\item A student graphed the system $y = 3x - 1$ and $y = -2x + 9$ and found the intersection at $(2, 5)$. Prove the student is correct algebraically by plugging the coordinate into both equations. If the student had found $(1, 2)$, what would the algebraic check look like?
\end{enumerate}
\vspace{1cm}
"""
    },
    12: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Solving Systems Algebraically}

\medskip
\textbf{Method 1: Substitution}
Best when one equation is already solved for a variable (e.g., $y = 2x + 1$).
1. Substitute the expression for that variable into the OTHER equation.
2. Solve the new equation for the remaining variable.
3. Plug that answer back into either original equation to find the second variable.

\textbf{Method 2: Elimination (Linear Combinations)}
Best when both equations are in Standard Form ($Ax + By = C$).
1. Multiply one or both equations by a number so that one variable has opposite coefficients (e.g., $3x$ and $-3x$).
2. ADD the two equations together vertically. One variable will "eliminate" (cancel out).
3. Solve for the remaining variable.
4. Plug it back in to find the eliminated variable.

\vspace{2mm}
\textbf{Example (Substitution):} $y = x + 3$ and $2x + y = 9$.
Substitute $(x+3)$ for $y$: $2x + (x+3) = 9 \rightarrow 3x + 3 = 9 \rightarrow 3x = 6 \rightarrow x = 2$.
Plug $x=2$ back in: $y = 2 + 3 = 5$. Solution: $(2, 5)$.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Solve by substitution: $y = 3x$ and $x + y = 12$. \vspace{1.5cm}

\textbf{2.} Solve by substitution: $x = y - 2$ and $4x + y = 7$. \vspace{1.5cm}

\textbf{3.} Solve by elimination: $x + y = 10$ and $x - y = 4$. \vspace{1.5cm}

\textbf{4.} Solve by elimination: $2x + 3y = 12$ and $-2x + y = 4$. \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} Which method is best for: $y = 5x$ and $2x + 3y = 17$?
A) Graphing B) Substitution C) Elimination

\item \textbf{[MC]} Which method is best for: $3x + 4y = 10$ and $-3x + 2y = 8$?
A) Graphing B) Substitution C) Elimination

\item If $y = x+1$ and $y = 2x-3$, substitute to set up the first step: \blank = \blank
\item Add the equations vertically: $(x+y=5) + (x-y=1)$. Result: \blank
\item Solve: $y = 2x$ and $x + y = 9$. $x=$ \blank, $y=$ \blank
\item Solve: $y = x-2$ and $3x + y = 10$. $x=$ \blank, $y=$ \blank
\item Solve: $x + y = 8$ and $x - y = 2$. $x=$ \blank, $y=$ \blank
\item Solve: $2x + y = 10$ and $-2x + 3y = 6$. $y=$ \blank, $x=$ \blank
\item If you add $5x + 2y = 10$ and $3x - 2y = 6$, what variable eliminates? \blank
\item If you have $4x + y = 7$ and $x + y = 4$, what should you multiply the second equation by to eliminate $y$? \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Solve using Substitution: $y = 2x - 5$ and $3x - y = 8$.

\item Solve using Substitution: $x = -4y + 1$ and $2x + 5y = -7$.

\item Solve using Elimination (multiply one equation first): 
$x + 3y = 6$
$2x - y = 5$

\item Solve using Elimination (multiply both equations first):
$3x + 2y = 16$
$2x + 5y = 18$

\item Solve the system: $y = 4x - 1$ and $y = 4x + 6$. What happens mathematically? What is the solution?

\item Solve the system: $2x + 4y = 8$ and $x + 2y = 4$. What happens mathematically? What is the solution?

\item A student tried to solve $x + y = 10$ and $2x + y = 15$ by adding them. They got $3x + 2y = 25$ and got stuck. Explain their mistake and what they should have done instead.

\item Write a system of equations in standard form that can be solved perfectly by elimination without multiplying either equation by a number.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A test has 20 questions worth a total of 100 points. The test consists of True/False questions worth 3 points each and Multiple Choice questions worth 11 points each. Let $x$ be T/F and $y$ be MC. Write a system of equations and solve using elimination to find how many of each question type are on the test.

\item A farm raises chickens and cows. You count 35 heads and 110 legs. Write a system of equations representing the number of chickens ($x$) and cows ($y$). Solve the system using substitution to find how many of each animal are on the farm.

\item The perimeter of a rectangle is $42\text{ cm}$. The length is $3\text{ cm}$ more than twice the width. Let $L$ be length and $W$ be width. Write the system of equations and solve it using substitution to find the exact dimensions.

\item A coffee shop sells a house blend for $\$8$ per pound and a premium blend for $\$12$ per pound. They want to create a $20\text{-pound}$ mixture that sells for $\$10.50$ per pound. Write a system of equations and solve using elimination to determine how many pounds of each blend they should use.

\item Prove that the system $3x - 6y = 12$ and $-x + 2y = -4$ has infinite solutions. Show your algebraic steps clearly. What does this mean if you were to graph them?
\end{enumerate}
\vspace{1cm}
"""
    },
    13: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Understanding Functions}

\medskip
\textbf{What is a Function?} A function is a specific rule or relationship where every \textbf{input} ($x$-value, domain) has exactly ONE \textbf{output} ($y$-value, range). 
- Think of it like a machine: if you put a '2' in, it must spit out the exact same answer every single time. If it spits out '5' on Monday and '7' on Tuesday for the same input of '2', it is NOT a function.

\textbf{How to test for a function:}
- \textbf{Ordered Pairs/Tables:} Look at the $x$-values. If any $x$-value repeats and has a different $y$-value, it is NOT a function. (Repeating $y$-values are perfectly fine!).
- \textbf{Graphs (The Vertical Line Test):} If you can draw a vertical line anywhere on the graph and it touches the line/curve more than once, it is NOT a function.

\vspace{2mm}
\textbf{Example 1:} $\{(1, 2), (3, 4), (5, 6), (1, 8)\}$. NOT a function because the input 1 has two different outputs (2 and 8).
\textbf{Example 2:} $\{(1, 5), (2, 5), (3, 5)\}$. YES, a function. Each input has only one output. (It's okay that they all equal 5).
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Is $\{(0,0), (1,2), (2,4), (3,6)\}$ a function? \vspace{1cm}

\textbf{2.} Is $\{(4,1), (4,2), (4,3)\}$ a function? \vspace{1cm}

\textbf{3.} If a graph is a perfect circle, does it pass the vertical line test? \vspace{1cm}

\textbf{4.} A table has $x$-values: 2, 4, 6, 8 and $y$-values 10, 10, 10, 10. Is it a function? \vspace{1.5cm}

\textbf{5.} Why is it a problem in the real world if a vending machine is NOT a function? (e.g., input button A1). \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} The set of all input values is called the:
A) Range B) Domain C) Output D) Rule

\item \textbf{[MC]} Which of the following is the Vertical Line Test used for?
A) Finding the slope B) Finding $y$-intercept C) Testing if a graph is a function

\item Is this a function? $\{(1,1), (2,2), (3,3)\}$ (Yes/No) \blank
\item Is this a function? $\{(1,5), (1,6), (2,7)\}$ (Yes/No) \blank
\item Is this a function? $\{(-2, 4), (0, 0), (2, 4)\}$ (Yes/No) \blank
\item A horizontal line graph: Function or Not? \blank
\item A vertical line graph: Function or Not? \blank
\item A U-shaped parabola opening upwards: Function or Not? \blank
\item A sideways U-shaped parabola: Function or Not? \blank
\item Table: $x = [1, 2, 3, 2], y = [4, 5, 6, 7]$. Function? \blank
\item Table: $x = [5, 6, 7, 8], y = [1, 1, 1, 1]$. Function? \blank
\item If $y = x^2$, is it a function? (Every $x$ gives one $y$). \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Create a mapping diagram (two ovals with arrows) that represents a relationship that is NOT a function. Explain why.

\item Explain why the equation $x = y^2$ does NOT represent a function when you plug in $x = 4$.

\item Is the relationship between a person's fingerprint (input) and their identity (output) a function? Why or why not?

\item Is the relationship between a person's age (input) and their height (output) a function across a whole population? Explain.

\item You are given the set of points $\{(-3, 5), (-1, 7), (0, 8), (x, 10)\}$. What value(s) can $x$ NOT be if this set is to remain a function?

\item A student says, "Because the $y$-values repeat in the table, it is not a function." Correct the student's misunderstanding.

\item Write the equation of a line that is NOT a function. 

\item Draw a graph of a function that consists of exactly 4 disconnected points. List the coordinate pairs.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A car rental company uses a function to determine the cost of renting a car. The cost $C(d)$ is a function of the days $d$ rented. The formula is $C(d) = 45d + 20$. Calculate the output for an input of $d = 5$. Does every valid input have exactly one output?

\item Consider a school database where the input is a Student ID number and the output is the student's legal name. Is this a function? Now reverse it: The input is the student's legal name and the output is the Student ID number. Is the reversed relationship a function? Explain why.

\item A thermometer displays the temperature outside. Let the input $t$ be the time of day, and the output $T$ be the temperature. Is temperature a function of time? Now, let the input be the temperature, and the output be the time of day. Is time a function of temperature? Detail your reasoning.

\item Create a real-world scenario (not used in previous problems) that represents a relationship that is a function. Then, explain how changing the independent and dependent variables (swapping inputs and outputs) makes it no longer a function.
\end{enumerate}
\vspace{1cm}
"""
    },
    14: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Qualitative Graphs}

\medskip
\textbf{Qualitative Graphs:} These are graphs without numbers on the axes. They are used to visually describe the relationship between two quantities (how one changes as the other changes). 
For example: Distance over time, speed over time, or volume over time.

\textbf{Reading the Curve:}
- \textbf{Straight Line (Linear):} Constant rate of change (e.g., driving at a steady $60\text{ mph}$).
- \textbf{Curved Line (Non-linear):} Changing rate (e.g., speeding up or slowing down).
- \textbf{Positive Slope (Going up):} The $y$-value is increasing.
- \textbf{Negative Slope (Going down):} The $y$-value is decreasing.
- \textbf{Horizontal Line (Flat):} The $y$-value is \textbf{not changing} (e.g., stopped, or constant speed if the $y$-axis is speed).

\vspace{2mm}
\textbf{Example:} A graph shows "Distance from Home" on the $y$-axis and "Time" on the $x$-axis. The line goes up, flattens out, then goes back down to the $x$-axis.
\textit{Interpretation:} A person walked away from home at a steady pace, stopped for a while (flat line), and then walked back home.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} If a "Speed vs. Time" graph is a flat horizontal line, what is the car doing? \vspace{1.5cm}

\textbf{2.} If a "Distance vs. Time" graph is a flat horizontal line, what is the car doing? \vspace{1.5cm}

\textbf{3.} Draw a quick sketch of a graph showing a bathtub filling up, sitting full for a bath, and then draining. \vspace{2cm}

\textbf{4.} A curve starts flat and gets steeper and steeper going up. Is the rate of change increasing or decreasing? \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} On a distance-time graph, a steeper straight line means:
A) Moving slower B) Moving faster C) Stopped

\item \textbf{[MC]} On a speed-time graph, a line going down to the $x$-axis means:
A) Slowing down to a stop B) Going backwards C) Driving uphill

\item A graph of water in a pool vs. time goes down. The pool is: \blank (Filling/Draining)
\item Distance vs Time graph is flat. The object is: \blank
\item Speed vs Time graph is flat. The object is: \blank
\item A curve on a distance-time graph means the speed is: \blank (Constant/Changing)
\item You throw a ball in the air. Height vs Time graph shape: \blank (U-shape/Upside-down U)
\item Your bank balance if you deposit $\$10$ every day: \blank (Straight line up/Curve up)
\item The amount of fuel in a car during a long road trip: \blank (Line up/Line down)
\item \textbf{[MC]} A graph showing an airplane's altitude during a flight from takeoff to landing looks like: A) A circle B) A trapezoid C) A straight line down
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Sketch a qualitative graph representing a person's heart rate ($y$-axis) over time ($x$-axis) as they rest, run a sprint, and then cool down. Label the three sections.

\item A graph shows the Volume of water in a cylinder ($y$-axis) over time ($x$-axis) as it fills from a constant hose. Will the graph be a straight line or a curve? Why?

\item Now, imagine filling a cone (pointy end down) with water at a constant rate. Will the Height of the water ($y$-axis) over time ($x$-axis) be a straight line or a curve? Will it get steeper or flatter over time? Explain.

\item Describe a real-world situation that matches this graph: Distance from home increases steadily, drops suddenly back to zero, and then stays at zero.

\item Describe a real-world situation that matches this graph: Speed increases quickly, stays constant for a long time, then decreases quickly.

\item A student drops a bowling ball from a roof. Sketch a graph of its Speed vs Time. Now sketch a graph of its Distance from the ground vs Time. Explain the difference.

\item What does it mean if a graph of "Temperature of Coffee" over "Time" starts high, decreases rapidly, but then levels out and becomes perfectly horizontal?
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item You are on a Ferris wheel. Sketch a qualitative graph of your \textbf{Height above the ground} ($y$-axis) versus \textbf{Time} ($x$-axis) for three full rotations. Include the boarding process. Explain why the graph is a smooth wave rather than zigzagging straight lines.

\item A commuter bikes to work. The route involves a long flat stretch, a steep uphill climb, a flat rest at the top, and a steep downhill coast. Sketch a \textbf{Speed vs Time} graph and a \textbf{Distance vs Time} graph for this journey. Write a paragraph comparing how the uphill section looks on both graphs.

\item An hourglass is flipped over. Let the $y$-axis be the Volume of sand in the TOP half, and the $x$-axis be Time. Sketch the graph. Now, let the $y$-axis be the Volume of sand in the BOTTOM half. Sketch that graph. How do the two graphs relate to each other mathematically?

\item You pour water from a pitcher at a perfectly constant rate into a vase shaped like a sphere (a round fishbowl). Sketch a qualitative graph of the \textbf{Water Height} ($y$-axis) vs \textbf{Time} ($x$-axis). Explain in detail why the slope of the curve changes the way it does at the bottom, middle, and top of the bowl.
\end{enumerate}
\vspace{1cm}
"""
    },
    15: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Volume of Cylinders, Cones, \& Spheres}

\medskip
\textbf{The Cylinder:} A cylinder has a circular base and straight sides. 
$$ V_{\text{cylinder}} = \pi r^2 h $$
(Area of the base $\times$ height).

\textbf{The Cone:} A cone fits perfectly inside a cylinder with the same radius and height, but it takes up exactly $\frac{1}{3}$ of the space.
$$ V_{\text{cone}} = \frac{1}{3} \pi r^2 h $$

\textbf{The Sphere:} A perfectly round 3D object. The volume depends only on its radius.
$$ V_{\text{sphere}} = \frac{4}{3} \pi r^3 $$

\textbf{Exact vs. Approximate:} 
- \textbf{Exact form:} Leave the symbol $\pi$ in the answer (e.g., $12\pi\text{ cm}^3$).
- \textbf{Approximate form:} Multiply by $3.14$ or use the $\pi$ button on a calculator (e.g., $37.68\text{ cm}^3$).

\vspace{2mm}
\textbf{Example:} Find the exact volume of a cone with radius $3$ and height $10$.
\textit{Solution:} $V = \frac{1}{3} \pi (3^2)(10) = \frac{1}{3} \pi (9)(10) = 30\pi$.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Find the exact volume of a cylinder with $r=2, h=5$. \vspace{1cm}

\textbf{2.} Find the exact volume of a cone with $r=2, h=5$. \vspace{1cm}

\textbf{3.} Find the exact volume of a sphere with $r=3$. \vspace{1cm}

\textbf{4.} If a diameter is 10, what is the radius? \vspace{1cm}

\textbf{5.} A cylinder and a cone have the same base and height. The cylinder holds $90\text{ mL}$ of water. How much does the cone hold? \vspace{1cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} The volume of a cone is what fraction of a cylinder with the same dimensions?
A) $1/2$ \quad B) $1/3$ \quad C) $3/4$ \quad D) $2/3$

\item \textbf{[MC]} Which formula is for a sphere?
A) $\pi r^2 h$ \quad B) $\frac{1}{3} \pi r^2 h$ \quad C) $\frac{4}{3} \pi r^3$

\item Cylinder: $r=4, h=10$. Exact volume: \blank
\item Cylinder: $d=6, h=8$. Exact volume: \blank
\item Cone: $r=3, h=4$. Exact volume: \blank
\item Cone: $d=10, h=6$. Exact volume: \blank
\item Sphere: $r=6$. Exact volume: \blank
\item Sphere: $d=12$. Exact volume: \blank
\item Use $\pi \approx 3.14$: Cylinder $r=1, h=10$. Approx volume: \blank
\item Use $\pi \approx 3.14$: Cone $r=3, h=10$. Approx volume: \blank
\item A cylinder has volume $300\pi$. A cone with the same base/height has volume \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item A soup can (cylinder) has a diameter of $8\text{ cm}$ and a height of $11\text{ cm}$. Calculate the approximate volume of soup it holds (use $\pi \approx 3.14$).

\item A cone-shaped paper cup has a radius of $4\text{ cm}$ and holds exactly $48\pi\text{ cm}^3$ of water. Work backward using the formula to find the height of the cup.

\item A basketball (sphere) has a diameter of $9\text{ inches}$. Find the exact volume of air inside the basketball.

\item You have a block of wax with a volume of $1000\text{ cm}^3$. You melt it down to make cylindrical candles with a radius of $2\text{ cm}$ and a height of $10\text{ cm}$. How many FULL candles can you make? (Use $3.14$).

\item A silo is made of a cylinder with a half-sphere (hemisphere) on top. The radius of the silo is $10\text{ ft}$, and the cylindrical part is $40\text{ ft}$ tall. Find the exact total volume of the silo.

\item Which holds more: a cylinder with $r=3, h=4$ or a cylinder with $r=4, h=3$? Show the math to prove it.

\item A tennis ball has a radius of $3\text{ cm}$. Three tennis balls fit perfectly tightly stacked inside a cylindrical can. What is the volume of the cylindrical can? What is the total volume of the 3 balls? How much empty space is in the can?
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item An ice cream cone is filled completely with solid ice cream, and then a perfect hemisphere (half-sphere) scoop is placed perfectly on top. The cone has a diameter of $6\text{ cm}$ and a height of $12\text{ cm}$. The hemisphere scoop exactly matches the diameter of the cone. Calculate the total exact volume of the ice cream. 

\item A manufacturer is designing a cylindrical water tank. The tank needs to hold exactly $1,000\pi\text{ cubic feet}$ of water. 
a) If the architect restricts the radius to $10\text{ feet}$, how tall must the tank be?
b) If the architect restricts the height to $40\text{ feet}$, what must the radius be?

\item Archimedes discovered that a sphere inscribed perfectly inside a cylinder (touching the sides, top, and bottom) takes up exactly $\frac{2}{3}$ of the cylinder's volume. Prove this using the volume formulas. (Hint: let the sphere's radius be $r$. What must the cylinder's radius and height be in terms of $r$?).

\item A giant hourglass consists of two identical cones connected at their tips. Each cone has a radius of $15\text{ cm}$ and a height of $40\text{ cm}$. Sand falls from the top cone to the bottom cone at a rate of $50\text{ cm}^3$ per second. If the top cone is completely full, how long will it take for all the sand to empty into the bottom cone? (Give answer in minutes, using $\pi \approx 3.14$).
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
                    
print("Successfully injected EXPANDED custom questions for Lessons 11-15.")
