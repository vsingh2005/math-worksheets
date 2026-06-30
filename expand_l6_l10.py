import os

base_dir = r"c:\Users\singh\Downloads\math_worksheets_repo\8th_standard"

questions_data = {
    6: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Slope \& Similar Triangles}

\medskip
\textbf{What is Slope?} Slope ($m$) is a number that describes the steepness and direction of a line. It is calculated as the ratio of the vertical change (rise) to the horizontal change (run) between any two points on the line.
$$ m = \frac{\text{Rise}}{\text{Run}} = \frac{y_2 - y_1}{x_2 - x_1} $$

\textbf{Similar Triangles and Slope:} If you draw right triangles using the rise and run between any two pairs of points on the same line, those triangles will always be \textbf{similar}. Because they are similar, the ratio of their corresponding sides (the rise over the run) will always be equal. This proves that a line has a \textbf{constant slope} everywhere.

\vspace{2mm}
\textbf{Example:} A line passes through $(0,0)$, $(2,3)$, and $(4,6)$. 
Triangle 1 is formed by $(0,0)$ and $(2,3)$. Rise = 3, Run = 2. Slope = $3/2$.
Triangle 2 is formed by $(2,3)$ and $(4,6)$. Rise = $6-3=3$, Run = $4-2=2$. Slope = $3/2$.
Because the triangles are similar, the slope is the same.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Find the slope of the line passing through $(1, 2)$ and $(4, 8)$. \vspace{1.5cm}

\textbf{2.} A slope triangle has a rise of 10 and a run of 4. What is the slope? \vspace{1.5cm}

\textbf{3.} If a line has a slope of $-2$, and passes through $(0, 5)$, find another point on the line. \vspace{1.5cm}

\textbf{4.} Explain why any two slope triangles drawn on the same line are similar. \vspace{1.5cm}

\textbf{5.} What does a slope of zero look like on a graph? \vspace{1cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} The slope formula is:
A) $(x_2-x_1)/(y_2-y_1)$ \quad B) $(y_2-y_1)/(x_2-x_1)$ \quad C) $y = mx+b$

\item \textbf{[MC]} A horizontal line has a slope of:
A) 1 \quad B) Undefined \quad C) 0 \quad D) $-1$

\item \textbf{[MC]} A vertical line has a slope of:
A) 1 \quad B) Undefined \quad C) 0 \quad D) $-1$

\item \textbf{[MC]} If a line goes down from left to right, its slope is:
A) Positive \quad B) Negative \quad C) Zero

\item Find the slope between $(0, 0)$ and $(3, 9)$. \blank
\item Find the slope between $(2, 4)$ and $(5, 10)$. \blank
\item Find the slope between $(-1, -2)$ and $(1, 4)$. \blank
\item Find the slope between $(4, 7)$ and $(8, 7)$. \blank
\item Find the slope between $(3, -5)$ and $(3, 2)$. \blank
\item Rise = 15, Run = 5. Slope = \blank
\item Rise = -8, Run = 2. Slope = \blank
\item Find the slope between $(10, 20)$ and $(5, 10)$. \blank
\item True or False: All slope triangles on a straight line are congruent. \blank
\item True or False: All slope triangles on a straight line are similar. \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Create two different similar right triangles on the line that passes through $(0,0)$ and $(3, 4)$. Show that the rise/run ratio is identical for both.

\item Find the missing coordinate $y$ if the line passing through $(2, 5)$ and $(4, y)$ has a slope of 3.

\item Find the missing coordinate $x$ if the line passing through $(x, 8)$ and $(5, 2)$ has a slope of $-2$.

\item A line has a slope of $\frac{2}{3}$. If it starts at $(-3, 1)$, what are the coordinates of the next two points if you apply the slope twice?

\item Graphically, what is the difference between a line with a slope of 5 and a line with a slope of $\frac{1}{5}$?

\item Write the equation of a proportional relationship that passes through the origin and the point $(7, 21)$.

\item Two students calculate the slope between $(-2, 5)$ and $(4, -7)$. Student A does $\frac{-7 - 5}{4 - (-2)}$. Student B does $\frac{5 - (-7)}{-2 - 4}$. Do they get the same answer? Prove it.

\item Why is the slope of a vertical line undefined? Use the slope formula to explain.

\item A proportional relationship has a slope of $4.5$. What is the unit rate?

\item A line passes through $(a, b)$ and $(c, d)$. Write the slope formula using these variables.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A ramp needs to be built with a slope of $\frac{1}{12}$ to meet accessibility standards. If the ramp must reach a doorway that is $2.5\text{ feet}$ above the ground, how far from the building must the ramp start (horizontal distance)? Show your work using similar triangles.

\item Water is filling a tank at a constant rate. After $3\text{ minutes}$, there are $12\text{ gallons}$ in the tank. After $8\text{ minutes}$, there are $32\text{ gallons}$. Calculate the slope. What does the slope represent in this context?

\item An airplane is descending towards a runway. At a horizontal distance of $10\text{ miles}$ away, its altitude is $30,000\text{ feet}$. At $5\text{ miles}$ away, its altitude is $15,000\text{ feet}$. Calculate the slope of the descent (in feet per mile) and use it to determine the altitude at $2\text{ miles}$ away.

\item Prove that the equation for any line passing through the origin can be written as $y = mx$. Use the definition of slope, a generic point $(x,y)$, and the origin $(0,0)$.

\item You are analyzing the growth of two plants. Plant A grows from $5\text{ cm}$ to $15\text{ cm}$ in 5 days. Plant B grows from $10\text{ cm}$ to $22\text{ cm}$ in 4 days. Which plant has a steeper slope on a growth graph? What does the steeper slope mean?

\item A mountain road rises $400\text{ feet}$ vertically for every $2000\text{ feet}$ of horizontal distance. What is the slope? If a car drives up the road and covers a horizontal distance of $3\text{ miles}$ ($15,840\text{ feet}$), how much elevation did it gain?
\end{enumerate}
\vspace{1cm}
"""
    },
    7: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Proportional Relationships \& Slope}

\medskip
\textbf{Proportional Relationships:} A relationship where two quantities always have the same ratio. On a graph, this is a straight line that \textbf{always passes through the origin $(0,0)$}. The equation is always of the form $y = mx$.

\textbf{Unit Rate and Slope:} In a proportional relationship, the \textbf{unit rate} (the value of $y$ when $x=1$) is exactly the same as the \textbf{slope} ($m$) of the line.
$$ \text{Slope } m = \frac{\text{Change in } y}{\text{Change in } x} = \text{Unit Rate} $$

\textbf{Comparing Relationships:} You can compare the slopes of two different proportional relationships even if they are presented in different formats (e.g., comparing a graph to an equation or a table).

\vspace{2mm}
\textbf{Example:} Car A travels $120\text{ miles}$ in 2 hours (from a table). Car B's distance is given by $y = 55x$ (where $x$ is hours). Which car is faster?
\textit{Solution:} Car A's slope/unit rate is $120/2 = 60\text{ mph}$. Car B's slope/unit rate is $55\text{ mph}$. Car A is faster because its slope is steeper.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} An equation is $y = 4.5x$. What is the slope? What is the unit rate? \vspace{1cm}

\textbf{2.} A table shows $x=2, y=10$ and $x=4, y=20$. Is it proportional? What is $m$? \vspace{1.5cm}

\textbf{3.} Graph $y = \frac{1}{2}x$. Does it pass through the origin? \vspace{1cm}

\textbf{4.} Brand A costs $\$15$ for 3 shirts. Brand B is represented by $y = 4x$. Which is more expensive per shirt? \vspace{1.5cm}

\textbf{5.} Why must a proportional graph pass through $(0,0)$? \vspace{1.0cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} The equation for a proportional relationship is:
A) $y = mx + b$ \quad B) $y = mx$ \quad C) $y = x^2$

\item \textbf{[MC]} A proportional graph MUST pass through:
A) $(0, 1)$ \quad B) $(1, 1)$ \quad C) $(0, 0)$ \quad D) $(1, 0)$

\item \textbf{[MC]} The slope of $y = 8x$ is:
A) 8 \quad B) $x$ \quad C) $y$ \quad D) 0

\item Is the relationship $y = 3x + 2$ proportional? (Yes/No) \blank
\item Is the relationship $y = \frac{3}{4}x$ proportional? (Yes/No) \blank
\item Find the unit rate: $60\text{ miles}$ in 3 hours. \blank
\item Find the unit rate: $\$20$ for 5 books. \blank
\item Find the slope of the table: $(1, 4), (2, 8), (3, 12)$. \blank
\item Find the slope of the table: $(2, 7), (4, 14), (6, 21)$. \blank
\item What is the slope of $y = 2.5x$? \blank
\item Write the equation for a proportional relationship with slope 7. \blank
\item If $y$ is proportional to $x$, and $y = 10$ when $x = 2$, find $y$ when $x = 5$. \blank
\item Which is steeper: $y = 4x$ or $y = 5x$? \blank
\item Which is steeper: $y = 0.5x$ or $y = \frac{1}{4}x$? \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Runner A's distance is given by the equation $d = 8t$ (where $d$ is miles and $t$ is hours). Runner B runs $15\text{ miles}$ in 2 hours. Who is faster? Justify your answer using unit rates.

\item A recipe calls for 3 cups of flour to make 24 cookies. Write an equation relating the number of cookies ($y$) to cups of flour ($x$). What is the constant of proportionality?

\item Determine if the following table represents a proportional relationship. If so, write the equation.
$x = 3, 6, 9$ | $y = 12, 24, 36$

\item Determine if the following table represents a proportional relationship. If so, write the equation.
$x = 2, 4, 6$ | $y = 5, 9, 13$

\item A graph shows a straight line passing through $(0,0)$ and $(5, 30)$. Write the equation for the line. What is the unit rate?

\item Two jobs pay hourly. Job 1 pays $\$45$ for 3 hours. Job 2 is represented by $y = 16x$. Which job has the better hourly pay? By how much?

\item Write a word problem that can be modeled by the equation $y = 1.25x$.

\item If the cost of apples is proportional to the weight, and 4 lbs cost $\$5.00$, how much do 10 lbs cost?

\item Explain why the points $(1, k)$ and $(0,0)$ are enough to define any proportional relationship. What does $k$ represent?
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item You are comparing three internet providers. Provider A charges according to the equation $y = 45x$ (where $y$ is total cost and $x$ is months). Provider B's cost is shown in a table: 2 months for $\$100$, 4 months for $\$200$. Provider C charges $\$55$ per month but gives the first month free. Which providers represent a proportional relationship? Which one is the cheapest over a 12-month period?

\item The amount of fuel a plane consumes is proportional to the hours flown. The plane consumes $1,500\text{ gallons}$ in 4 hours. Write an equation for this relationship. If the plane has $2,500\text{ gallons}$ in its tank, is that enough to complete a 7-hour flight? Explain.

\item Two cars are driving on a highway. Car X's distance over time is graphed as a line passing through $(0,0)$ and $(4, 260)$. Car Y's distance is given by $d = 62t$. If they both start at the same time and place, how far apart will they be after 5 hours?

\item In chemistry, Charles's Law states that the volume of a gas is proportional to its absolute temperature. At $300\text{ Kelvin}$, a gas takes up $2\text{ Liters}$. Write the equation $V = mT$. What is the volume at $450\text{ Kelvin}$?

\item A water tank is leaking. A sensor records that after 15 minutes, $45\text{ liters}$ have leaked out. Assuming a constant proportional leak rate, how many liters will leak out in a full 24-hour day?

\item A currency exchange claims a proportional relationship between US Dollars ($D$) and Euros ($E$). If $\$50$ USD exchanges for $42$ Euros, write the equation to convert USD to Euros. Use it to convert $\$350$ USD. If the bank charges a flat $\$5$ fee per transaction on top of the rate, is the relationship still proportional? Why or why not?
\end{enumerate}
\vspace{1cm}
"""
    },
    8: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Slope-Intercept Form}

\medskip
\textbf{The Equation of a Line:} Most linear relationships are NOT proportional (they don't start at 0,0). To represent any straight line, we use \textbf{Slope-Intercept Form}:
$$ y = mx + b $$
- **$m$** is the **slope** (the rate of change, rise/run).
- **$b$** is the **$y$-intercept** (where the line crosses the $y$-axis, the starting value when $x=0$).

\textbf{Graphing with $y=mx+b$:}
1. Plot the $y$-intercept ($b$) on the $y$-axis at $(0, b)$.
2. Use the slope ($m$) as rise over run to find the next point.
3. Draw a line through the points.

\vspace{2mm}
\textbf{Example:} Graph $y = \frac{2}{3}x - 4$.
\textit{Step 1:} The $y$-intercept is $-4$. Plot $(0, -4)$.
\textit{Step 2:} The slope is $2/3$. From $(0, -4)$, go UP 2 and RIGHT 3. Plot the point $(3, -2)$.
\textit{Step 3:} Draw the line.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Identify $m$ and $b$ for $y = -3x + 7$. \vspace{1cm}

\textbf{2.} Write the equation of a line with slope $5$ and $y$-intercept $-2$. \vspace{1cm}

\textbf{3.} A gym charges a $\$20$ sign-up fee plus $\$15$ a month. Write the equation. What is $b$? \vspace{1.5cm}

\textbf{4.} Convert the proportional equation $y = 4x$ into slope-intercept form. What is $b$? \vspace{1.0cm}

\textbf{5.} Why do we call $b$ the "initial value" in word problems? \vspace{1.0cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} In $y = mx+b$, what does $b$ represent?
A) Slope B) $x$-intercept C) $y$-intercept D) Rate of change

\item \textbf{[MC]} Which equation has a slope of $-4$ and a $y$-intercept of 5?
A) $y = 5x - 4$ B) $y = -4x + 5$ C) $y = -4x - 5$ D) $y = 4x + 5$

\item State $m$ and $b$: $y = 2x + 9$. $m=$ \blank, $b=$ \blank
\item State $m$ and $b$: $y = -x - 3$. $m=$ \blank, $b=$ \blank
\item State $m$ and $b$: $y = \frac{3}{4}x + 1$. $m=$ \blank, $b=$ \blank
\item State $m$ and $b$: $y = 7$. $m=$ \blank, $b=$ \blank
\item State $m$ and $b$: $y = 5x$. $m=$ \blank, $b=$ \blank
\item Write the equation: slope $= 3$, $y$-int $= -2$. \blank
\item Write the equation: slope $= -0.5$, $y$-int $= 10$. \blank
\item Write the equation: slope $= 0$, $y$-int $= 4$. \blank
\item If a line crosses the $y$-axis at $(0, -6)$, what is $b$? \blank
\item What is the $y$-intercept of the proportional line $y = 12x$? \blank
\item Is $y = 2x + 1$ a proportional relationship? (Yes/No) \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item A line has a slope of $2$ and passes through the point $(3, 10)$. Use $y = mx + b$ to solve for $b$, then write the full equation.

\item A line passes through $(0, 5)$ and $(2, 11)$. What is the $y$-intercept? What is the slope? Write the equation.

\item A taxi charges a flat fee of $\$3.00$ plus $\$2.50$ per mile. Write the linear equation. What is the $y$-intercept in this context?

\item Rewrite the equation $2y = 6x + 8$ into slope-intercept form ($y=mx+b$). What are $m$ and $b$?

\item A plant is $4\text{ cm}$ tall when planted, and grows $1.5\text{ cm}$ per week. Write the equation. Find the height after 6 weeks.

\item Given the table: $(0, 2), (1, 5), (2, 8), (3, 11)$. What is the $y$-intercept? What is the slope? Write the equation.

\item Given the table: $(2, 10), (4, 18), (6, 26)$. Find the slope. Use it to work backward and find the $y$-intercept. Write the equation.

\item Is the line $y = 4x - 2$ parallel to the line $y = 4x + 7$? How do you know?

\item Graph the line $y = -\frac{1}{2}x + 4$ on a coordinate plane. What are the coordinates of the $y$-intercept and the $x$-intercept?
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A cell phone company offers a plan that charges a $\$35$ monthly access fee plus $\$5$ for every gigabyte of data used. Write the equation in $y=mx+b$ form. If your budget is $\$65$ for the month, how many full gigabytes can you use?

\item A scuba diver is at an elevation of $-20\text{ feet}$ (below sea level) and begins ascending at a constant rate of $2\text{ feet}$ per second. Write an equation modeling the diver's elevation $y$ over time $x$. How long will it take the diver to reach the surface ($y=0$)?

\item Find the equation of the line that passes through the points $(-3, -7)$ and $(1, 5)$. First find the slope, then plug in one point to solve for $b$.

\item Two friends are saving money. Friend A starts with $\$50$ and saves $\$15$ a week. Friend B starts with $\$0$ but saves $\$25$ a week. Write the equation for each friend. After how many weeks will they have the exact same amount of money?

\item A car depreciates (loses value) over time. It was purchased new for $\$24,000$. After 3 years, it is worth $\$18,000$. Assuming the depreciation is linear, calculate the slope (depreciation per year). Write the equation for the car's value. In what year will the car be worth $\$0$?

\item Explain the mathematical difference between a proportional relationship and a general linear relationship. Provide an equation and a real-world example for each to support your explanation.
\end{enumerate}
\vspace{1cm}
"""
    },
    9: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Constructing \& Interpreting Linear Models}

\medskip
\textbf{Real-World Linear Models:} Many real-world scenarios feature a constant rate of change (slope) and a starting amount ($y$-intercept). We model these with $y = mx + b$.

\textbf{Constructing a Model from Data:}
If you are given two points (e.g., in year 2 sales were $\$500$, in year 5 sales were $\$1100$):
1. Calculate the rate of change: $m = \frac{1100 - 500}{5 - 2} = \frac{600}{3} = 200$. (Sales increase by $\$200$ per year).
2. Find the initial value $b$ by working backward to year 0: $500 - 2(200) = 100$.
3. The model is $y = 200x + 100$.

\textbf{Interpreting the Model:}
- \textbf{Slope ($m$):} What is changing per unit of time/item? (e.g., dollars per hour, degrees per minute).
- \textbf{$y$-intercept ($b$):} What was the starting condition? (e.g., base fee, starting temperature).
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} A plumber charges a $\$50$ house call fee plus $\$40$ per hour. Write the model. \vspace{1.5cm}

\textbf{2.} Interpret the slope and $y$-intercept in the model $y = -5x + 100$ where $y$ is water in a tank (gallons) and $x$ is minutes. \vspace{1.5cm}

\textbf{3.} At 2 hours, you traveled $100\text{ miles}$. At 4 hours, you traveled $200\text{ miles}$. Write the model. \vspace{1.5cm}

\textbf{4.} A savings account model is $y = 50x + 200$. What does the $200$ represent? \vspace{1cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} In a model representing cost over time, the $y$-intercept usually represents:
A) Hourly rate B) Total cost C) Initial/flat fee D) Time

\item \textbf{[MC]} If temperature drops $2^\circ$ per hour, the slope is:
A) 2 B) -2 C) 0 D) Undefined

\item Model: $y = 15x + 30$. What is the initial value? \blank
\item Model: $y = -10x + 500$. What is the rate of change? \blank
\item A subscription is $\$10$/month plus a $\$20$ sign-up fee. Model: $y = $ \blank
\item A candle is $12\text{ in}$ tall and burns at $1\text{ in}$ per hour. Model: $y = $ \blank
\item A bank account starts at $\$0$ and gains $\$25$ per week. Model: $y = $ \blank
\item Interpret $m$ in $y = 2.5x + 10$ (taxi cost $y$ for $x$ miles). \blank
\item Interpret $b$ in $y = 2.5x + 10$ (taxi cost $y$ for $x$ miles). \blank
\item Points are $(0, 100)$ and $(2, 150)$. Rate of change is \blank
\item Using points $(0, 100)$ and $(2, 150)$, write the equation. \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item A catering company charges a setup fee and a per-person rate. The total cost for 10 people is $\$150$. The cost for 20 people is $\$250$. Calculate the per-person rate (slope). 

\item Using the slope from \#1, calculate the setup fee ($y$-intercept). Write the full linear model.

\item An airplane is at $30,000\text{ ft}$. It descends at $1,500\text{ ft}$ per minute. Write the linear model. What does the $y$-intercept represent? What does the slope represent?

\item Using the model from \#3, find the altitude of the airplane after 12 minutes.

\item The equation $C = 0.15m + 40$ models the monthly cost ($C$) of renting a car for $m$ miles driven. Interpret the meaning of $0.15$ and $40$ in the context of the problem.

\item At week 3, a tomato plant is $14\text{ inches}$ tall. At week 5, it is $20\text{ inches}$ tall. Write the linear model for the plant's height over time. 

\item What was the plant's height at week 0? Does this make sense in real life?

\item An online store charges shipping based on a linear model. Buying 2 items costs $\$12$ in shipping. Buying 5 items costs $\$18$ in shipping. Construct the linear model. What is the base fee for shipping?
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item You are reviewing data for a city's population. In the year 2010 (Year 0), the population was $45,000$. In 2020 (Year 10), the population was $52,500$. Assume the growth is linear. Construct a model $P = mt + b$. What is the projected population for the year 2035 (Year 25)?

\item A swimming pool containing $10,000\text{ gallons}$ of water is being drained. After 2 hours, there are $8,500\text{ gallons}$ left. Construct a linear model for the volume of water $V$ after $t$ hours. At what time $t$ will the pool be exactly half empty? How long until it is completely empty?

\item A car rental agency has two pricing options. Option A is $\$50$ a day with unlimited miles. Option B is $\$30$ a day plus $\$0.20$ per mile. You need the car for 1 day. Write a model for Option B. For what number of miles will the cost of Option B exactly equal the cost of Option A? 

\item A tech startup had $\$1,200,000$ in the bank in month 2. By month 6, they had $\$800,000$ left. Assuming a constant burn rate (linear decrease), write the equation for their bank balance. In what month will the startup run out of money (balance = 0) if they don't secure more funding?

\item Consider the equation $F = \frac{9}{5}C + 32$ which converts Celsius to Fahrenheit. Interpret the slope and the $y$-intercept in the context of temperatures. What does the 32 mean physically? What does the $\frac{9}{5}$ mean physically?
\end{enumerate}
\vspace{1cm}
"""
    },
    10: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Solving Linear Equations}

\medskip
\textbf{Goal:} To isolate the variable (e.g., $x$) on one side of the equal sign. 

\textbf{Steps to Solve Multi-Step Equations:}
1. \textbf{Distribute} to clear parentheses if necessary.
2. \textbf{Combine Like Terms} on each side of the equation.
3. \textbf{Move Variables} to one side by adding or subtracting.
4. \textbf{Isolate the Variable} using inverse operations (add/sub, then mult/div).

\textbf{Number of Solutions:}
- \textbf{One Solution:} You get $x = \text{number}$ (e.g., $x=5$). The lines intersect once.
- \textbf{No Solution:} The variables cancel out and leave a false statement (e.g., $4 = 7$). The lines are parallel.
- \textbf{Infinite Solutions:} The variables cancel out and leave a true statement (e.g., $3 = 3$). The lines are identical.

\vspace{2mm}
\textbf{Example:} Solve $3(x - 2) = 2x + 4$.
\textit{Step 1 (Distribute):} $3x - 6 = 2x + 4$.
\textit{Step 2 (Move $x$):} Subtract $2x$ from both sides $\rightarrow x - 6 = 4$.
\textit{Step 3 (Isolate):} Add 6 to both sides $\rightarrow x = 10$. (One solution).
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Solve: $2x + 5 = 13$ \vspace{1cm}

\textbf{2.} Solve: $4(x + 1) = 4x + 4$. What type of solution is this? \vspace{1.5cm}

\textbf{3.} Solve: $5x - 2 = 5x + 9$. What type of solution is this? \vspace{1.5cm}

\textbf{4.} Solve: $3(2x - 4) = 4x + 10$. \vspace{2.0cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} What is the first step to solve $2(x+3) = 14$?
A) Add 3 B) Subtract 14 C) Distribute the 2 D) Subtract $x$

\item \textbf{[MC]} If an equation ends in $5 = 5$, how many solutions does it have?
A) One B) Zero C) Infinite

\item \textbf{[MC]} If an equation ends in $8 = 2$, how many solutions does it have?
A) One B) Zero C) Infinite

\item Solve: $x + 7 = 20$. $x =$ \blank
\item Solve: $3x = 15$. $x =$ \blank
\item Solve: $\frac{x}{4} = 8$. $x =$ \blank
\item Solve: $2x - 4 = 10$. $x =$ \blank
\item Solve: $5x + 1 = 26$. $x =$ \blank
\item Solve: $-3x = 21$. $x =$ \blank
\item Solve: $7 - x = 12$. $x =$ \blank
\item Distribute and simplify: $4(x - 2)$. Answer: \blank
\item Combine like terms: $3x + 5 - x + 2$. Answer: \blank
\item What type of solution is $2x = 2x$? \blank
\item What type of solution is $3x + 1 = 3x + 4$? \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Solve for $x$: $4x - 7 = 2x + 9$

\item Solve for $y$: $5(y + 2) = 3y - 6$

\item Solve for $w$: $-2(w - 4) = -2w + 8$. State the number of solutions.

\item Solve for $z$: $6z + 3 - 2z = 4(z + 1)$. State the number of solutions.

\item Solve for $k$: $\frac{1}{2}(4k - 6) = 3k + 5$

\item Write an equation that has NO solution. Explain why it has no solution.

\item Two competing health clubs have different payment plans. Club A charges a $\$40$ sign-up fee plus $\$10$ per month. Club B has no sign-up fee but charges $\$18$ per month. Set up an equation to find out after how many months the total cost will be the same. Solve the equation.

\item Solve: $3(2x - 1) + 4 = 5x + 1 + x$. State the number of solutions.

\item The perimeter of a rectangle is $30\text{ cm}$. The length is $2x + 1$ and the width is $x$. Set up an equation and solve for $x$. Then find the length and width.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A rental car company offers two deals. Deal A: $\$30$ per day plus $\$0.15$ per mile. Deal B: $\$50$ per day with unlimited free miles. If you rent the car for 3 days, set up an equation to find exactly how many miles you would need to drive for the costs to be equal. Solve it.

\item Solve the complex equation for $x$. Show every step clearly: 
$$ \frac{2}{3}(6x - 9) + 4 = -\frac{1}{2}(4x + 8) + 12 $$

\item Create your own multi-step linear equation that requires distribution on both sides and results in $x = 5$ as the single solution. Work it out to prove it.

\item Three siblings have ages represented by consecutive integers. The sum of their ages is 45. Let $x$ be the youngest sibling's age. Set up an equation and find the ages of all three siblings.

\item Explain the geometric meaning of "infinite solutions" when comparing two linear equations. If you graph the left side of the equation as $y_1$ and the right side as $y_2$, what does the graph look like?

\item A rectangular garden has a length that is $4\text{ feet}$ less than 3 times its width. If the perimeter is $64\text{ feet}$, construct an equation, solve for the width, and find the exact dimensions and area of the garden.
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
                    
print("Successfully injected EXPANDED custom questions for Lessons 6-10.")
