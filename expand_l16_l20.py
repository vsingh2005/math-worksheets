import os

base_dir = r"c:\Users\singh\Downloads\math_worksheets_repo\8th_standard"

questions_data = {
    16: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Scatter Plots}

\medskip
\textbf{Scatter Plots:} Graphs that use points to display values for two different variables. They help us determine if there is a relationship (an \textbf{association}) between the two variables.

\textbf{Types of Association:}
- \textbf{Positive Association:} As $x$ increases, $y$ increases (points go up from left to right).
- \textbf{Negative Association:} As $x$ increases, $y$ decreases (points go down from left to right).
- \textbf{No Association:} The points are scattered randomly with no clear pattern.

\textbf{Strength \& Form:}
- \textbf{Linear vs. Non-linear:} Do the points look like they form a straight line, or a curve?
- \textbf{Strong vs. Weak:} Are the points tightly packed together forming a clear shape (strong), or spread widely apart (weak)?
- \textbf{Outliers:} Data points that lie far away from the rest of the group.

\vspace{2mm}
\textbf{Example:} A scatter plot compares "Hours Studied" and "Test Score". 
\textit{Interpretation:} It will likely show a \textbf{strong positive linear association}. The more someone studies, the higher their score tends to be.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} What kind of association would you expect between "Age of a car" and "Value of the car"? \vspace{1cm}

\textbf{2.} What kind of association between "Shoe Size" and "Math Grade"? \vspace{1cm}

\textbf{3.} If points on a scatter plot form a U-shape, what is the form of association? \vspace{1cm}

\textbf{4.} Explain what an outlier represents in a dataset tracking height and weight. \vspace{1.5cm}

\textbf{5.} Why are scatter plots useful in real-world data analysis? \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} A scatter plot showing points going downward left to right has a:
A) Positive association B) Negative association C) No association

\item \textbf{[MC]} Points that are very spread out but still show a general upward trend have a:
A) Strong positive association B) Weak positive association C) Weak negative association

\item Expected association: Time spent running vs. Calories burned. \blank
\item Expected association: Outside temperature vs. Hot chocolate sales. \blank
\item Expected association: Number of siblings vs. Height. \blank
\item Expected association: Number of absences vs. Final Grade. \blank
\item Points form a straight line: \blank (Linear/Non-linear).
\item Points form a curve: \blank (Linear/Non-linear).
\item A point far away from the rest of the data is called an: \blank
\item If a scatter plot has no clear pattern, it has \blank association.
\item Is it possible to have a strong non-linear association? (Yes/No) \blank
\item Can an outlier change the general trend of a scatter plot? (Yes/No) \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Draw a rough sketch of a scatter plot with a strong negative linear association.

\item Draw a rough sketch of a scatter plot with a weak positive linear association. Include one clear outlier.

\item A researcher graphs the number of hours students play video games per week against their GPA. She notices a weak negative association. What does this mean in plain English? What does the "weak" part imply?

\item Consider a scatter plot of "Age in years" vs "Height in inches" for humans from age 0 to age 80. Describe the shape of this association. Is it linear? Why or why not?

\item You are plotting the weight of dogs against the length of their tails. You find a point at $(5\text{ lbs}, 20\text{ inches})$. Would this likely be considered an outlier? Explain.

\item How does sample size (the number of points on the graph) affect your ability to determine if an association is strong or weak?

\item Sketch a non-linear association that is strong.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item An ice cream shop owner tracks the daily high temperature and the number of ice cream cones sold for 30 days. He creates a scatter plot and notices a very strong positive linear association. However, one day had a temperature of $95^\circ$ but only 10 cones were sold. 
a) What does the strong positive association tell him about his business?
b) What might explain the outlier on the $95^\circ$ day? (Give a logical real-world reason).

\item A medical study tracks the amount of a certain vitamin people take daily and their risk of catching a cold. The data shows a curve: taking a little bit of the vitamin decreases the risk, but taking massive amounts of the vitamin actually increases the risk again. 
a) Sketch the scatter plot. 
b) Describe the association (Linear/Non-linear, Positive/Negative). 
c) Why is a straight line not appropriate to describe this data?

\item You are tasked with determining if there is a relationship between the population of a city and the number of parks it has. 
a) What variables will you put on the $x$ and $y$ axes? 
b) What kind of association do you predict? 
c) If you find a city with 5 million people but only 2 parks, how will that appear on the graph, and what statistical term describes it?
\end{enumerate}
\vspace{1cm}
"""
    },
    17: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Lines of Best Fit}

\medskip
\textbf{Line of Best Fit (Trend Line):} When data in a scatter plot shows a linear association, we can draw a straight line through the center of the data cloud. This line models the trend of the data.
- The line should have about the same number of points above it as below it.
- It does NOT have to touch every point (or any point at all!).

\textbf{Writing the Equation:} 
Once the line is drawn, you can write its equation in $y = mx + b$ form by picking two points \textbf{ON THE DRAWN LINE} (not necessarily data points) to find the slope $m$ and $y$-intercept $b$.

\textbf{Making Predictions:}
- \textbf{Interpolation:} Predicting a value \textit{inside} the range of your data.
- \textbf{Extrapolation:} Predicting a value \textit{outside} the range of your data (less reliable).

\vspace{2mm}
\textbf{Example:} A line of best fit for "Hours Studied" ($x$) and "Score" ($y$) is $y = 5x + 60$. 
\textit{Prediction:} If a student studies for 4 hours, what score do we expect?
$y = 5(4) + 60 = 20 + 60 = 80$. We predict a score of 80.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} If a scatter plot has a negative association, will the line of best fit have a positive or negative slope? \vspace{1cm}

\textbf{2.} Line of best fit is $y = 2x + 10$. Predict $y$ when $x = 5$. \vspace{1cm}

\textbf{3.} Line of best fit is $y = -3x + 50$. Predict $y$ when $x = 10$. \vspace{1cm}

\textbf{4.} Why might extrapolation be dangerous or inaccurate? \vspace{1.5cm}

\textbf{5.} Can you draw a line of best fit for a scatter plot with "No Association"? \vspace{1cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} A line of best fit should:
A) Connect the first and last point B) Pass through the middle of the data C) Touch every point

\item \textbf{[MC]} Predicting a value far outside the given data range is called:
A) Interpolation B) Extrapolation C) Association

\item True or False: The line of best fit must pass through the origin. \blank
\item Equation is $y = 4x + 20$. Predict $y$ for $x = 3$. \blank
\item Equation is $y = -2x + 100$. Predict $y$ for $x = 15$. \blank
\item Equation is $y = 0.5x + 10$. Predict $y$ for $x = 20$. \blank
\item What does a slope of 0 mean for a line of best fit? \blank
\item If data goes up, the line of best fit has a \blank slope.
\item If a data point is an outlier, should it heavily influence where you draw the line? \blank
\item You pick points $(0, 10)$ and $(5, 30)$ on your trend line. What is $m$? \blank
\item Using the points from \#10, what is $b$? \blank
\item Using the points from \#10, what is the full equation? \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item A line of best fit for a scatter plot tracking "Months since purchase" ($x$) and "Value of laptop" ($y$) passes through $(0, 1200)$ and $(10, 800)$. Calculate the slope and write the equation of the line.

\item Using the equation from \#1, predict the value of the laptop after 24 months. Is this interpolation or extrapolation?

\item Using the equation from \#1, after how many months will the laptop be worth $\$0$? Do you think this prediction is completely realistic?

\item You draw a line of best fit through a scatter plot. Point A on the line is $(2, 15)$. Point B on the line is $(6, 35)$. The actual data point at $x=2$ is $(2, 12)$. Did your line over-predict or under-predict the value at $x=2$? By how much?

\item Explain the process of drawing a "good" line of best fit by hand. What visual cues are you looking for?

\item A student draws a line of best fit that perfectly connects the lowest $x$ value to the highest $x$ value in the dataset, ignoring all the points in between. Explain why this might be a bad line of best fit.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item An agronomist tracks the amount of fertilizer used (in pounds, $x$) and the yield of corn (in bushels, $y$). The line of best fit is $y = 3.5x + 50$. 
a) Interpret the slope in the context of fertilizer and corn yield.
b) Interpret the $y$-intercept. What does it mean when $x=0$?
c) If a farmer uses 100 pounds of fertilizer, what yield is expected?

\item A gym wants to predict how many members will show up based on the outside temperature. They gather data for winter days. The line of best fit is $y = -2x + 150$, where $x$ is the temperature in Fahrenheit and $y$ is the number of members.
a) How many members are expected if it's $30^\circ\text{F}$?
b) What happens to the predicted attendance as it gets colder?
c) At what temperature does the model predict 0 members will show up? 
d) Does the model make sense for a summer day that is $90^\circ\text{F}$? Explain why this highlights the danger of extrapolation.

\item You are given a scatter plot showing a very strong non-linear U-shaped association. A friend insists on drawing a straight line of best fit directly through the middle, which ends up being a flat horizontal line ($y=c$). Explain mathematically why this straight line is a terrible model for making predictions on this dataset.
\end{enumerate}
\vspace{1cm}
"""
    },
    18: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Two-Way Frequency Tables}

\medskip
\textbf{Two-Way Tables:} Used to organize and display categorical data (data that fits into categories, like "Yes/No", "Male/Female", "Dog/Cat") for two different variables at the same time.

\textbf{Frequencies:}
- \textbf{Joint Frequency:} The numbers in the middle of the table (where a row and column intersect). E.g., The number of 8th graders who like Math.
- \textbf{Marginal Frequency:} The totals at the end of the rows and columns (in the margins). E.g., The total number of 8th graders.
- \textbf{Grand Total:} The number in the bottom right corner. The total of everything.

\textbf{Relative Frequencies (Percentages/Decimals):}
Found by dividing a frequency by a total.
- \textbf{Row Relative Frequency:} Divide a cell by the \textit{Row Total}.
- \textbf{Column Relative Frequency:} Divide a cell by the \textit{Column Total}.
- \textbf{Total Relative Frequency:} Divide a cell by the \textit{Grand Total}.

\vspace{2mm}
\textbf{Example:} In a survey of 100 students, 40 play a sport. Out of those 40, 30 also play an instrument. 
\textit{Question:} What is the relative frequency of playing an instrument, GIVEN that a student plays a sport?
\textit{Solution:} We only look at the "Play a Sport" total (40). $30 / 40 = 0.75$ or $75\%$.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} If the Grand Total is 50, and 10 people fit into a specific category, what is the total relative frequency? \vspace{1cm}

\textbf{2.} A table has 20 boys and 30 girls. 15 boys like pizza. What is the relative frequency of liking pizza among boys? \vspace{1cm}

\textbf{3.} Using the same data, what is the relative frequency of being a boy who likes pizza out of everyone? \vspace{1cm}

\textbf{4.} How do you find a marginal frequency if it's missing from the table? \vspace{1cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} Data in a two-way table must be:
A) Numerical B) Categorical C) Linear

\item \textbf{[MC]} The totals at the bottom and right edges of the table are called:
A) Joint frequencies B) Marginal frequencies C) Grand totals

\item Fill in the blank: Grand Total = Sum of all \blank totals.
\item If Row A total is 40 and Row B total is 60, what is the Grand Total? \blank
\item Out of 100 total people, 25 are Left-Handed Boys. Relative frequency = \blank
\item Out of 50 Boys, 25 are Left-Handed. Relative frequency (among boys) = \blank
\item Out of 80 Girls, 20 like Sci-Fi. Relative frequency (among girls) = \blank
\item Joint frequency = 15. Column total = 60. Column relative frequency = \blank
\item Row total = 120. Grand total = 200. Total relative frequency = \blank
\item A cell has 0. What does that mean? \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.8cm, leftmargin=0.6cm]
\item Construct a 2x2 table outline for the variables "Has a Dog" (Yes/No) and "Has a Cat" (Yes/No). Label the margins.

\item In a survey of 200 adults, 120 drink coffee. Of the coffee drinkers, 80 also drink tea. There are 50 adults who drink neither. Fill in the missing information: How many people drink tea but NOT coffee?

\item Using the data from \#2, what is the relative frequency of drinking coffee among all adults surveyed?

\item Using the data from \#2, what is the relative frequency of drinking tea, GIVEN that the adult drinks coffee?

\item A school has 300 8th graders. 180 take Spanish, 120 take French. Of the Spanish students, 50 are in Art. Of the French students, 80 are in Art. What percentage of ALL students are in Art?

\item Using the data from \#5, is there an association between taking French and taking Art? Compare the relative frequencies to justify your answer.

\item Explain the difference between "The percentage of athletes who are injured" and "The percentage of injured people who are athletes". How would you calculate each using a table?
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A medical trial tests a new allergy drug. 500 patients receive the drug, and 500 receive a placebo. Out of those receiving the drug, 400 report relief from symptoms. Out of those receiving the placebo, 150 report relief. 
a) Construct a two-way frequency table.
b) Calculate the column relative frequencies for symptom relief.
c) Based on the data, does the drug appear to be effective? Justify with percentages.

\item A marketing company surveys 1000 people about whether they prefer streaming movies or going to the theater. They break the data down by age (Under 30 vs. 30 and Over). 600 people are Under 30, and 450 of them prefer streaming. 400 people are 30 and Over, and 200 of them prefer streaming.
a) What is the joint frequency of being 30 and Over AND preferring the theater?
b) What is the relative frequency of preferring the theater, given that a person is Under 30?
c) Is there an association between age and movie preference? Explain mathematically.

\item You are given a two-way table filled entirely with relative frequencies (decimals), but none of the actual counts. The grand total cell says 1.00. The cell for "Plays Soccer AND Plays Basketball" says 0.12. If you are told that exactly 36 students play both sports, how many total students were surveyed? Show your reasoning.
\end{enumerate}
\vspace{1cm}
"""
    },
    19: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Properties of Integer Exponents}

\medskip
\textbf{The Rules of Exponents:} (For any non-zero base $x$)
1. \textbf{Product Rule:} When multiplying the same base, ADD the exponents.
   $x^a \cdot x^b = x^{a+b}$
2. \textbf{Quotient Rule:} When dividing the same base, SUBTRACT the exponents.
   $\frac{x^a}{x^b} = x^{a-b}$
3. \textbf{Power of a Power:} When raising a power to a power, MULTIPLY the exponents.
   $(x^a)^b = x^{a \cdot b}$
4. \textbf{Zero Exponent:} Anything to the power of zero is 1.
   $x^0 = 1$
5. \textbf{Negative Exponents:} A negative exponent means "reciprocal". Move it across the fraction line and make it positive.
   $x^{-a} = \frac{1}{x^a}$  and  $\frac{1}{x^{-a}} = x^a$

\vspace{2mm}
\textbf{Example 1:} Simplify $3^4 \cdot 3^2$.
\textit{Solution:} $3^{4+2} = 3^6$.

\textbf{Example 2:} Simplify $\frac{5^3}{5^7}$. Write with a positive exponent.
\textit{Solution:} $5^{3-7} = 5^{-4} = \frac{1}{5^4}$.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Simplify $x^5 \cdot x^8$. \vspace{1cm}

\textbf{2.} Simplify $\frac{y^9}{y^4}$. \vspace{1cm}

\textbf{3.} Simplify $(z^3)^4$. \vspace{1cm}

\textbf{4.} Evaluate $100^0$. \vspace{1cm}

\textbf{5.} Rewrite $4^{-3}$ with a positive exponent. \vspace{1cm}

\textbf{6.} Simplify $2^3 \cdot 2^{-5}$ and write with a positive exponent. \vspace{1cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} What is the value of $7^0$?
A) 0 \quad B) 7 \quad C) 1 \quad D) -7

\item \textbf{[MC]} Which expression is equivalent to $x^{-2}$?
A) $-2x$ \quad B) $\frac{1}{x^2}$ \quad C) $x^{\frac{1}{2}}$

\item $a^4 \cdot a^6 = $ \blank
\item $b^7 / b^2 = $ \blank
\item $(c^2)^5 = $ \blank
\item $x^{-4} \cdot x^4 = $ \blank
\item $5^{-2} = $ \blank (Write as a fraction)
\item $\frac{y^3}{y^8} = $ \blank (Write with positive exponent)
\item $(2x)^3 = $ \blank
\item $m^5 \cdot m^{-2} = $ \blank
\item $\frac{x^{-3}}{x^{-5}} = $ \blank
\item $(-3)^0 = $ \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Simplify fully and leave only positive exponents: $\frac{4^5 \cdot 4^{-2}}{4^6}$

\item Simplify fully: $(3x^2y^4)^3$

\item Simplify fully and leave only positive exponents: $\frac{12a^5 b^{-2}}{4a^2 b^3}$

\item Explain why $x^0 = 1$ using the quotient rule for exponents (Hint: think about $\frac{x^3}{x^3}$).

\item Evaluate without a calculator: $2^{-4} \cdot 2^7$

\item A student simplified $(x^3)^4$ as $x^7$. What mistake did they make, and what is the correct answer?

\item Simplify: $\left(\frac{2}{x}\right)^{-3}$

\item Find the missing exponent $k$: $x^4 \cdot x^k = x^{-2}$
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A computer's memory is measured in bytes. A kilobyte is $2^{10}$ bytes, a megabyte is $2^{20}$ bytes, and a gigabyte is $2^{30}$ bytes. How many kilobytes are exactly in one gigabyte? Use exponent rules to calculate the answer as a power of 2.

\item The intensity of a sound decreases by a factor of $10^{-2}$ when you move a certain distance away. If the original sound intensity is $10^5$ units, what is the new intensity? Express your answer in both exponential form and standard form.

\item In a laboratory, a bacterial culture's population doubles every hour. The population can be modeled by $P = 100 \cdot 2^h$. What is the population at $h = -3$ (3 hours before the experiment started)? Calculate the value and explain what a negative exponent means in the context of time.

\item Prove algebraically that $\left(\frac{a^x}{a^y}\right)^z = \frac{a^{xz}}{a^{yz}}$ for any non-zero base $a$ and integer exponents $x, y, z$.

\item A box has dimensions $2^x, 2^{x+1},$ and $2^{x-2}$. Write an expression for the total volume of the box as a single power of 2.
\end{enumerate}
\vspace{1cm}
"""
    },
    20: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Scientific Notation}

\medskip
\textbf{What is Scientific Notation?} A way of writing very large or very small numbers using a number between 1 and 10 multiplied by a power of 10.
Format: $a \times 10^n$, where $1 \leq a < 10$ and $n$ is an integer.

\textbf{Converting to Scientific Notation:}
- For large numbers (e.g., $45,000$): Move the decimal LEFT until one non-zero digit remains. The exponent is positive. $\rightarrow 4.5 \times 10^4$.
- For small numbers (e.g., $0.0032$): Move the decimal RIGHT until one non-zero digit is to the left. The exponent is negative. $\rightarrow 3.2 \times 10^{-3}$.

\textbf{Operations:}
- \textbf{Multiplying:} Multiply the front numbers ($a$) and ADD the exponents ($n$).
- \textbf{Dividing:} Divide the front numbers ($a$) and SUBTRACT the exponents ($n$).
- *Note:* If the new front number is no longer between 1 and 10, adjust the decimal and the exponent!

\vspace{2mm}
\textbf{Example:} $(3 \times 10^4) \cdot (4 \times 10^5) = 12 \times 10^9$. 
Adjust to proper form: $1.2 \times 10^{10}$.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Write $8,400,000$ in scientific notation. \vspace{1cm}

\textbf{2.} Write $0.000071$ in scientific notation. \vspace{1cm}

\textbf{3.} Write $2.5 \times 10^3$ in standard form. \vspace{1cm}

\textbf{4.} Multiply: $(2 \times 10^3) \cdot (4 \times 10^2)$. \vspace{1cm}

\textbf{5.} Why is $45 \times 10^3$ NOT in correct scientific notation? Fix it. \vspace{1cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} Which of the following is in correct scientific notation?
A) $0.5 \times 10^4$ \quad B) $5 \times 10^4$ \quad C) $50 \times 10^3$

\item \textbf{[MC]} A negative exponent in scientific notation means the number is:
A) Negative B) Between 0 and 1 C) Very large

\item Convert to Sci Not: $150,000 =$ \blank
\item Convert to Sci Not: $0.00092 =$ \blank
\item Convert to Sci Not: $7,000,000,000 =$ \blank
\item Convert to Standard: $4.1 \times 10^5 =$ \blank
\item Convert to Standard: $8.6 \times 10^{-4} =$ \blank
\item Convert to Standard: $1.0 \times 10^2 =$ \blank
\item Multiply: $(3 \times 10^2) \cdot (2 \times 10^4) =$ \blank
\item Divide: $\frac{8 \times 10^6}{2 \times 10^2} =$ \blank
\item Correct the format: $25 \times 10^4 = $ \blank
\item Correct the format: $0.8 \times 10^{-2} = $ \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item The distance to the sun is about $93,000,000\text{ miles}$. Write this in scientific notation.

\item The mass of a dust particle is $0.000000753\text{ kg}$. Write this in scientific notation.

\item Calculate and write the answer in correct scientific notation: $(5 \times 10^4) \cdot (4 \times 10^6)$

\item Calculate and write the answer in correct scientific notation: $\frac{1.2 \times 10^8}{6 \times 10^3}$

\item Add: $(2.4 \times 10^5) + (3.1 \times 10^5)$

\item Add: $(4 \times 10^3) + (5 \times 10^4)$. (Hint: make the exponents match first).

\item Approximately how many times larger is $8 \times 10^7$ than $4 \times 10^3$?

\item Explain why scientists use scientific notation instead of standard form. Give an example where standard form would be incredibly difficult to work with.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item The speed of light is approximately $3 \times 10^8\text{ meters per second}$. If it takes light from the sun about $5 \times 10^2\text{ seconds}$ to reach Earth, calculate the distance from the Earth to the Sun in meters. Express your final answer in scientific notation.

\item A human cell has a mass of about $1.0 \times 10^{-12}\text{ kg}$. If an average human body contains roughly $3.7 \times 10^{13}$ cells, calculate the total mass of the cells in an average human body. 

\item The national debt of a country is $\$2.4 \times 10^{12}$. The population of the country is $3 \times 10^8$. If the debt were divided equally among every person, how much would each person owe? Express your answer in standard form.

\item A computer processor can perform an operation in $2 \times 10^{-9}\text{ seconds}$. How many operations can the processor perform in 1 minute ($6 \times 10^1\text{ seconds}$)?

\item Compare the volume of the Earth and the Moon. The Earth's volume is approximately $1.08 \times 10^{12}\text{ km}^3$. The Moon's volume is approximately $2.19 \times 10^{10}\text{ km}^3$. About how many times larger is the Earth's volume than the Moon's volume? Estimate the ratio.
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
                    
print("Successfully injected EXPANDED custom questions for Lessons 16-20.")
