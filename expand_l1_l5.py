import os

base_dir = r"c:\Users\singh\Downloads\math_worksheets_repo\8th_standard"

questions_data = {
    1: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Rigid Transformations}

\medskip
\textbf{Translations:} A translation ``slides'' a figure horizontally, vertically, or both. Every point moves the exact same distance and direction. If we translate by $(a, b)$, the rule is $(x, y) \rightarrow (x+a, y+b)$.

\textbf{Reflections:} A reflection ``flips'' a figure over a line (like the $x$-axis or $y$-axis), creating a mirror image.
- Across $x$-axis: $(x, y) \rightarrow (x, -y)$
- Across $y$-axis: $(x, y) \rightarrow (-x, y)$

\textbf{Rotations:} A rotation ``turns'' a figure around a center point (usually the origin). 
- $90^\circ$ clockwise: $(x, y) \rightarrow (y, -x)$
- $90^\circ$ counter-clockwise: $(x, y) \rightarrow (-y, x)$
- $180^\circ$ rotation: $(x, y) \rightarrow (-x, -y)$

\textbf{Rigid Motion:} All of these are \textit{rigid motions} because they preserve the size and shape (angle measures and side lengths) of the original figure. The image is \textbf{congruent} to the pre-image.

\vspace{2mm}
\textbf{Example 1:} Translate $A(-2, 3)$ right 4 units and down 5 units.
\textit{Solution:} $(x, y) \rightarrow (x+4, y-5)$. So, $A' = (-2+4, 3-5) = (2, -2)$.

\textbf{Example 2:} Reflect $B(4, -1)$ across the $y$-axis.
\textit{Solution:} $(x, y) \rightarrow (-x, y)$. So, $B' = (-4, -1)$.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Translate the point $(3, 4)$ left 2 units and up 1 unit. What is the new coordinate? \vspace{1cm}

\textbf{2.} Reflect the point $(-5, -6)$ across the $x$-axis. \vspace{1cm}

\textbf{3.} Rotate the point $(2, 7)$ by $180^\circ$ around the origin. \vspace{1cm}

\textbf{4.} A triangle has vertices at $X(1, 1)$, $Y(4, 1)$, and $Z(4, 5)$. If you reflect it across the $y$-axis and then translate it up 3 units, what are the coordinates of $X''$, $Y''$, and $Z''$? \vspace{2.5cm}

\textbf{5.} Why do we call translations, reflections, and rotations "rigid motions"? \vspace{1.5cm}

\textbf{6.} True or False: Rotating a shape changes its perimeter. \vspace{1cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} Which transformation represents a ``slide''?
A) Translation \quad B) Reflection \quad C) Rotation \quad D) Dilation

\item \textbf{[MC]} Which transformation represents a ``flip'' over a line?
A) Translation \quad B) Reflection \quad C) Rotation \quad D) Dilation

\item \textbf{[MC]} Which transformation represents a ``turn''?
A) Translation \quad B) Reflection \quad C) Rotation \quad D) Dilation

\item \textbf{[MC]} If $(x,y) \rightarrow (x+3, y-2)$, what is this?
A) Translation right 3, down 2 \quad B) Translation left 3, up 2 \quad C) Reflection

\item Translate $(-4, 5)$ right 6 units, down 1 unit. New coordinate: \blank

\item Translate $(0, -2)$ left 4 units, up 7 units. New coordinate: \blank

\item Translate $(3, 3)$ using the rule $(x-5, y+2)$. New coordinate: \blank

\item Reflect $(3, 2)$ across the $x$-axis. New coordinate: \blank

\item Reflect $(-4, 8)$ across the $y$-axis. New coordinate: \blank

\item Reflect $(0, -5)$ across the $x$-axis. New coordinate: \blank

\item Rotate $(1, 4)$ by $90^\circ$ clockwise around origin. New coordinate: \blank

\item Rotate $(-2, -3)$ by $180^\circ$ around origin. New coordinate: \blank

\item Rotate $(5, 0)$ by $90^\circ$ counter-clockwise around origin. New coordinate: \blank

\item Does a translation change the size of the shape? \blank

\item Does a reflection change the angles of the shape? \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item A square has vertices at $A(1, 1)$, $B(1, 3)$, $C(3, 3)$, and $D(3, 1)$. Apply a translation of $(x-2, y+1)$. List the new coordinates $A', B', C', D'$.

\item If a figure is reflected across the $y$-axis, write the general rule $(x, y) \rightarrow (?, ?)$. Use it to reflect the point $(8, -12)$.

\item A triangle is rotated $180^\circ$ around the origin. If one of its vertices was at $(-5, -2)$, what are the coordinates of its image?

\item Draw or describe a situation where a translation and a reflection yield the exact same image. (Hint: Think about lines of symmetry).

\item A trapezoid has a vertex at $T(4, -7)$. It undergoes a transformation and the new vertex is $T'(-4, -7)$. Identify the specific transformation that occurred.

\item Find the rule for the translation that maps $M(-3, 4)$ onto $M'(5, -1)$.

\item A line segment $PQ$ is rotated $90^\circ$ clockwise. The original endpoints are $P(0, 5)$ and $Q(3, 8)$. Find $P'$ and $Q'$.

\item If you translate a point $(x, y)$ by $(a, b)$ and then translate it again by $(-a, -b)$, where does the point end up? Explain.

\item A hexagon is reflected across the $x$-axis. What is the distance between the original vertex $H(2, 6)$ and its image $H'$?

\item Describe the difference between rotating $90^\circ$ clockwise versus $270^\circ$ counter-clockwise.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A video game designer is programming a character to jump from a platform at $(2, 5)$ to another platform at $(7, 8)$. Write the algebraic translation rule $(x, y) \rightarrow (x+a, y+b)$ that represents this jump.

\item In a mirror maze, a laser beam originates at $(-3, -4)$. It is first reflected across the $x$-axis by a mirror, and then immediately reflected across the $y$-axis by a second mirror. What are the final coordinates of the laser beam? What single transformation represents this sequence?

\item A drone maps a rectangular field with corners at $(0,0)$, $(0, 10)$, $(20, 10)$, and $(20, 0)$. The drone operator rotates the map $90^\circ$ counter-clockwise on their digital screen. What are the new coordinates of the field's corners on the screen?

\item Prove that rotating a figure $180^\circ$ is mathematically equivalent to reflecting it across the $x$-axis and then reflecting it across the $y$-axis. Show your work using the coordinate rules for these transformations.

\item A robotic arm picks up an object at $(12, 15)$. It translates the object left 5 units, rotates it $90^\circ$ clockwise around the origin, and then reflects it across the $y$-axis. What is the final resting coordinate of the object?

\item A city planner places a park entrance at $(5, 5)$. They want to place a second entrance symmetrically across the main road, which is represented by the line $y = x$. What are the coordinates of the second entrance? (Think about how reflecting across $y = x$ swaps coordinates).

\item You are designing a logo. You start with a triangle at $A(1,1), B(4,1), C(1,5)$. You translate it by $(x+3, y+3)$ and then rotate it $180^\circ$. Calculate the final coordinates of all three vertices.

\item Explain in 2-3 sentences why rigid motions are essential in manufacturing and engineering when creating identical parts for an assembly line.
\end{enumerate}
\vspace{1cm}
"""
    },
    2: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Sequences of Transformations}

\medskip
\textbf{Sequences:} Often, a single transformation is not enough to move a figure to its target location. We can chain multiple rigid motions together, which is called a \textit{sequence of transformations}.
For example: A translation followed by a reflection.

\textbf{Congruence:} Two figures are defined as \textbf{congruent} if you can map one exactly onto the other using a sequence of rigid motions (translations, reflections, rotations). Because rigid motions preserve size and shape, any sequence of them will also preserve size and shape.

\textbf{Order Matters:} The order in which you perform the transformations is critical. Translating and then reflecting often results in a different final image than reflecting and then translating!

\vspace{2mm}
\textbf{Example 1:} Point $A(2, 3)$. Reflect across $x$-axis, then translate by $(x-1, y+4)$.
\textit{Step 1 (Reflection):} $(2, 3) \rightarrow (2, -3)$
\textit{Step 2 (Translation):} $(2, -3) \rightarrow (2-1, -3+4) = (1, 1)$. 
Final image is $A''(1, 1)$.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Point $B(4, 5)$ is translated left 2 units, then reflected across the $y$-axis. Find $B''$. \vspace{1.5cm}

\textbf{2.} Are a pre-image and its final image congruent after a sequence of 5 rigid motions? \vspace{1.5cm}

\textbf{3.} Describe a sequence of two transformations that maps $(1, 1)$ to $(-1, -1)$. \vspace{2.0cm}

\textbf{4.} If Figure X can be mapped onto Figure Y using a rotation and a translation, what can we confidently say about the area of Figure X compared to Figure Y? \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} Two figures are congruent if:
A) They are the same color B) One maps to the other via rigid motions C) One is a dilation

\item \textbf{[MC]} Does the order of transformations matter?
A) Always B) Never C) Sometimes D) Only for dilations

\item Point $M(4, 5)$ is translated left 2 units. New coordinate: \blank
\item Take the answer from \#3 and reflect it across the $x$-axis. New coordinate: \blank
\item Point $P(0, -3)$ is rotated $180^\circ$. New coordinate: \blank
\item Take the answer from \#5 and translate it by $(x+3, y+3)$. New coordinate: \blank
\item Translate $(5, 5)$ by $(x-5, y-5)$. New coordinate: \blank
\item Take the answer from \#7 and reflect across $y$-axis. New coordinate: \blank
\item Reflect $(2, 4)$ across the $x$-axis, then across the $x$-axis again. Where is it? \blank
\item Reflect $(-3, 7)$ across the $y$-axis, then translate down 2 units. \blank
\item Rotate $(1, 0)$ $90^\circ$ clockwise, then translate up 4 units. \blank
\item If Figure A maps to Figure B, and Figure B maps to Figure C using rigid motions, are A and C congruent? \blank
\item Which single transformation is equivalent to reflecting across the $x$-axis then the $y$-axis? \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item A polygon is mapped onto another polygon by translating it down 3 units and reflecting it across the $y$-axis. If a vertex of the image is at $(4, -1)$, what was the coordinate of the original vertex?

\item Determine whether the following statement is true or false: "The order in which you perform a sequence of transformations does not matter." Provide a coordinate counter-example to prove your point.

\item Find a sequence of two rigid motions that maps the segment from $(1, 1)$ to $(1, 4)$ onto the segment from $(-1, 1)$ to $(-1, 4)$.

\item Triangle $DEF$ has vertices at $D(2, 2)$, $E(5, 2)$, $F(2, 6)$. Apply the following sequence: 1) Reflect across the $x$-axis. 2) Translate left 4 units. What are the final vertices?

\item Is a translation of $(x+2, y+2)$ followed by another translation of $(x+3, y-1)$ the same as a single translation of $(x+5, y+1)$? Show why.

\item You reflect a point across the $x$-axis, and then rotate it $90^\circ$ clockwise. The final point is $(3, 5)$. Where did you start?

\item Why do we use sequences of transformations in geometry to prove congruence instead of just measuring with a ruler?

\item Can a sequence of purely translations map a triangle pointing "up" to a triangle pointing "down"? Why or why not?

\item Write a coordinate rule for the sequence: reflection across the $y$-axis followed by a rotation of $180^\circ$.

\item Apply the rule from \#9 to the point $(-6, -8)$.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A robotics arm is programmed to move objects using sequences of transformations. It picks up a box at $(0, 5)$ and needs to place it perfectly at $(-5, 0)$ with the same orientation. Describe the rigid motions the arm must execute.

\item In graphic design, a logo is copied and transformed. The original logo is in Quadrant I. The designer wants an upside-down mirror image of the logo placed in Quadrant III. Describe a sequence of three transformations to achieve this.

\item Two friends are comparing shapes. Shape $X$ and Shape $Y$ have the same side lengths and angle measures, but Shape $Y$ is a mirror image of Shape $X$. Can Shape $X$ be mapped onto Shape $Y$ using only translations and rotations? Explain your reasoning in detail.

\item A choreographer is designing a dance routine on a coordinate grid stage. A dancer starts at $(4, 4)$. The dancer must reflect across the $y$-axis, run to the origin (translation), and then rotate $270^\circ$ counter-clockwise around the origin. Trace the dancer's exact coordinates at each step.

\item Consider a rectangle with vertices $(2, 2)$, $(6, 2)$, $(6, 4)$, and $(2, 4)$. Map this rectangle to Quadrant II using a rotation, and then map it to Quadrant IV using a translation. List all coordinate sets.

\item Prove that any two congruent line segments in the coordinate plane can be mapped onto each other using no more than three rigid transformations. 

\item A satellite dish is adjusted by a sequence of rotations. It rotates $45^\circ$ clockwise, then $135^\circ$ counter-clockwise, then $180^\circ$ clockwise. What is the net single rotation of the satellite dish?
\end{enumerate}
\vspace{1cm}
"""
    },
    3: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Angles \& Parallel Lines}

\medskip
\textbf{Transversals:} When two parallel lines are cut by a third line (the transversal), eight angles are formed. These angles have special relationships:
- \textbf{Corresponding Angles:} In the same position at each intersection. They are \textbf{congruent} ($=$).
- \textbf{Alternate Interior Angles:} On opposite sides of the transversal and between the parallel lines. They are \textbf{congruent} ($=$).
- \textbf{Alternate Exterior Angles:} On opposite sides of the transversal and outside the parallel lines. They are \textbf{congruent} ($=$).
- \textbf{Same-Side Interior Angles:} On the same side of the transversal, between the lines. They are \textbf{supplementary} (add to $180^\circ$).

\textbf{Triangles:} 
- The sum of the interior angles of any triangle is exactly $180^\circ$.
- \textbf{Exterior Angle Theorem:} The measure of an exterior angle of a triangle is equal to the sum of the measures of its two remote interior angles.

\vspace{2mm}
\textbf{Example:} Parallel lines $l$ and $m$ are cut by transversal $t$. If one acute angle is $50^\circ$, what are the other angles?
\textit{Solution:} All acute angles will be $50^\circ$. All obtuse angles will be $180^\circ - 50^\circ = 130^\circ$.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} If two corresponding angles are $(2x)^\circ$ and $80^\circ$, find $x$. \vspace{1.5cm}

\textbf{2.} If two same-side interior angles are $100^\circ$ and $(y+20)^\circ$, find $y$. \vspace{1.5cm}

\textbf{3.} In a triangle, two angles measure $40^\circ$ and $70^\circ$. What is the third angle? \vspace{1.5cm}

\textbf{4.} An exterior angle of a triangle is $110^\circ$. One remote interior angle is $40^\circ$. What is the other remote interior angle? \vspace{1.5cm}

\textbf{5.} Why do same-side interior angles add up to $180^\circ$? \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} Which angle pairs are supplementary when lines are parallel?
A) Alternate interior B) Corresponding C) Same-side interior D) Vertical

\item \textbf{[MC]} The sum of interior angles in a triangle is:
A) $90^\circ$ B) $180^\circ$ C) $360^\circ$ D) $270^\circ$

\item If an alternate interior angle is $45^\circ$, what is its pair? \blank
\item If a corresponding angle is $110^\circ$, what is its pair? \blank
\item If a same-side interior angle is $60^\circ$, what is its pair? \blank
\item In a triangle, angles are $50^\circ, 60^\circ,$ and $x^\circ$. Find $x$. \blank
\item In a right triangle, one angle is $30^\circ$. Find the other acute angle. \blank
\item Vertical angles are always: \blank (congruent or supplementary)
\item Alternate exterior angles are always: \blank (congruent or supplementary)
\item Linear pairs add up to: \blank degrees.
\item Exterior angle = $130^\circ$. Remote interior #1 = $70^\circ$. Remote interior #2 = \blank
\item Exterior angle = $90^\circ$. Remote interior #1 = $45^\circ$. Remote interior #2 = \blank
\item Triangle angles: $x, x, x$. Find $x$. \blank
\item Triangle angles: $90^\circ, x, x$. Find $x$. \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Two parallel lines are intersected by a transversal. The measure of an acute angle is given by $(3x + 15)^\circ$ and the measure of the corresponding angle is $(5x - 5)^\circ$. Find $x$.

\item In a triangle, the angles are represented by $x^\circ$, $(2x)^\circ$, and $(3x)^\circ$. Find the measure of each angle. What kind of triangle is this?

\item Two parallel lines are cut by a transversal. Same-side interior angles measure $(4y + 20)^\circ$ and $(6y - 10)^\circ$. Calculate the value of $y$ and the measure of both angles.

\item An exterior angle of a triangle measures $(5z)^\circ$. The remote interior angles measure $40^\circ$ and $(2z + 5)^\circ$. Solve for $z$.

\item A transversal cuts parallel lines $p$ and $q$. The alternate exterior angles are $(7x - 12)^\circ$ and $(5x + 18)^\circ$. Find $x$ and the angle measures.

\item Can a triangle have two obtuse angles? Explain mathematically using the Triangle Sum Theorem.

\item If one angle of a linear pair is twice as large as the other, find both angles.

\item In $\triangle ABC$, $\angle A = (x+10)^\circ$, $\angle B = (x-10)^\circ$, and $\angle C = (2x)^\circ$. Find $x$.

\item A transversal is drawn perpendicular to one parallel line. What must be true about its intersection with the other parallel line?

\item Using the properties of parallel lines, explain how to prove that alternate interior angles are congruent.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A city planner is designing a set of parallel streets intersected by a diagonal avenue. She wants the acute angle at the intersection to be exactly $40^\circ$. Calculate the measures of all other angles at the intersection points to ensure the design meets safety codes.

\item The frame of a bicycle forms a triangle. If the top tube and the down tube meet at a $65^\circ$ angle, and the down tube and the seat tube meet at a $45^\circ$ angle, what is the angle between the top tube and the seat tube?

\item Prove that the sum of the interior angles of a triangle is $180^\circ$ by drawing a horizontal line parallel to the base of the triangle that passes through the opposite top vertex. Use alternate interior angles in your proof.

\item A truss for a bridge features a large outer triangle divided into smaller triangles. One large exterior angle is measured at $145^\circ$. Inside, one of the remote interior angles is $(3x + 10)^\circ$ and the other is $(2x + 15)^\circ$. Determine the exact angles of the truss structure.

\item Two laser beams are fired parallel to each other. A mirror reflects a third beam that acts as a transversal, cutting through both parallel beams. If the same-side interior angles created by the reflection are $(10x)^\circ$ and $(8x)^\circ$, at what exact angle did the beam hit the mirrors?

\item Describe a real-world scenario (like carpentry, architecture, or navigation) where knowing that alternate interior angles are congruent is absolutely necessary.

\item A quilt pattern uses parallel strips of fabric crossed by diagonal stitching. To keep the pattern uniform, the sewer must ensure that the alternate exterior angles match. If they measure $(x^2 - 10)^\circ$ and $(26)^\circ$, what are the possible values for $x$?
\end{enumerate}
\vspace{1cm}
"""
    },
    4: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Dilations \& Scale Factor}

\medskip
\textbf{Dilations:} A dilation is a transformation that changes the \textit{size} of a figure but not its \textit{shape}. It produces a \textbf{similar} figure, not a congruent one.
- The \textbf{center of dilation} is the fixed point from which the shape shrinks or expands (often the origin).
- The \textbf{scale factor ($k$)} determines how much the figure grows or shrinks.

\textbf{Scale Factor Rules:}
- If $k > 1$, the figure represents an \textbf{enlargement}.
- If $0 < k < 1$, the figure represents a \textbf{reduction}.
- If $k = 1$, the figure stays the exact same size (congruent).
- Coordinate rule for dilations centered at the origin: $(x, y) \rightarrow (kx, ky)$.

\vspace{2mm}
\textbf{Example 1:} Dilate $A(4, -6)$ by a scale factor of $k = \frac{1}{2}$ from the origin.
\textit{Solution:} Multiply coordinates by $\frac{1}{2}$. $A' = (2, -3)$.

\textbf{Example 2:} A line segment is $5\text{ cm}$ long. It is dilated by $k = 3$. New length?
\textit{Solution:} $5 \times 3 = 15\text{ cm}$.
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Point $P(2, -6)$ is dilated from the origin by $k=0.5$. Find $P'$. \vspace{1.5cm}

\textbf{2.} A square has side length 4. What is its side length after a dilation of $k=2.5$? \vspace{1.5cm}

\textbf{3.} If $A(3, 4)$ dilates to $A'(12, 16)$, what is the scale factor? \vspace{1.5cm}

\textbf{4.} True or False: Dilations preserve the angle measures of a triangle. \vspace{1.5cm}

\textbf{5.} A rectangle with area $10\text{ cm}^2$ is dilated by $k=3$. Is the new area $30\text{ cm}^2$? Why or why not? \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} Which scale factor represents a reduction?
A) 1.5 B) 2 C) 0.8 D) 1

\item \textbf{[MC]} The rule $(x, y) \rightarrow (4x, 4y)$ means:
A) Translate by 4 B) Enlarge by 4 C) Reduce by 4 D) Rotate by 4

\item Dilate $(2, 4)$ by $k=3$. New coordinate: \blank
\item Dilate $(10, -5)$ by $k=0.2$. New coordinate: \blank
\item Dilate $(-4, -8)$ by $k=1/2$. New coordinate: \blank
\item Side length = 5. Dilate by $k=4$. New side length: \blank
\item Perimeter = 20. Dilate by $k=2$. New perimeter: \blank
\item Angle = $45^\circ$. Dilate by $k=3$. New angle: \blank
\item Original point: $(1, 1)$. Image point: $(5, 5)$. Scale factor = \blank
\item Original point: $(6, 9)$. Image point: $(2, 3)$. Scale factor = \blank
\item Dilate origin $(0,0)$ by $k=10$. New coordinate: \blank
\item If a dilation produces a congruent figure, $k = $ \blank
\item \textbf{[MC]} Do dilations preserve distance? A) Yes B) No
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item A pentagon is dilated from the origin resulting in a new pentagon. If a vertex at $(4, 8)$ maps to $(1, 2)$, what is the scale factor of the dilation?

\item A segment with endpoints $A(-3, 6)$ and $B(9, -3)$ is dilated by a scale factor of $\frac{2}{3}$ centered at the origin. Find the length of the new segment $A'B'$. (Hint: find the new coordinates first).

\item Write the algebraic rule for a dilation centered at the origin with a scale factor of $k$. Use notation $(x, y) \rightarrow (?, ?)$.

\item A photograph is $4\text{ inches}$ wide and $6\text{ inches}$ tall. It is enlarged by a scale factor of $1.5$. What are the new dimensions?

\item Triangle $XYZ$ has vertices $X(0, 2)$, $Y(4, 2)$, $Z(4, 5)$. Dilate it by $k=3$. Find $X', Y', Z'$.

\item If you dilate a figure by $k=2$, what happens to its perimeter? What happens to its area?

\item Explain why a dilation with scale factor $k=1$ is considered an "identity" transformation.

\item Point $C(-2, 5)$ is dilated to $C'(-8, 20)$. Point $D(1, -3)$ is dilated using the same scale factor. What is $D'$?

\item If a shape is dilated by $k=0.1$, describe what the image looks like compared to the original.

\item Are dilations considered "rigid motions"? Explain why or why not.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item An architect is creating a blueprint for a house. The actual living room is $20\text{ feet}$ long and $15\text{ feet}$ wide. On the blueprint, the living room is $8\text{ inches}$ long. What is the scale factor from the actual room to the blueprint? How wide is the room on the blueprint?

\item A toy manufacturer makes a model car that is a dilation of a real car. The real car is $180\text{ inches}$ long and the model is $5\text{ inches}$ long. If the real car's wheel has a diameter of $24\text{ inches}$, what is the diameter of the model car's wheel?

\item When you zoom in on a digital map by $200\%$, you are applying a dilation. What is the scale factor? If a park is represented by a $2\text{ cm}$ by $3\text{ cm}$ rectangle on screen originally, what are its dimensions after zooming in?

\item A movie projector dilates the image on a small $35\text{ mm}$ wide film strip onto a massive theater screen that is $14\text{ meters}$ wide ($14,000\text{ mm}$). Calculate the scale factor. If a character is $10\text{ mm}$ tall on the film strip, how tall are they on the screen in meters?

\item You create a custom sticker that is $2\text{ inches}$ by $2\text{ inches}$. You want to print a massive wall decal version using a scale factor of $15$. What will the area of the wall decal be? How does this compare to the area of the sticker?

\item Prove that dilations map parallel lines to parallel lines. You can use a coordinate plane example with two parallel line segments.

\item A magnifying glass enlarges objects by a scale factor of $4.5$. An ant is viewed under the glass and appears to be $1.8\text{ inches}$ long. How long is the actual ant?
\end{enumerate}
\vspace{1cm}
"""
    },
    5: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Instructional Guide: Similar Figures}

\medskip
\textbf{Similarity ($\sim$):} Two figures are similar if one can be mapped onto the other using a sequence of rigid motions and/or \textbf{dilations}. 
- \textbf{Corresponding Angles} are exactly EQUAL (congruent).
- \textbf{Corresponding Sides} are PROPORTIONAL (they have the same ratio or scale factor).

\textbf{Checking for Similarity:} To prove two triangles are similar, you only need to show that two angles of one triangle are congruent to two angles of the other triangle. This is called the \textbf{AA Similarity Criterion} (Angle-Angle).

\textbf{Setting up Proportions:} If $\triangle ABC \sim \triangle DEF$, then the ratios of their sides are equal: 
$$ \frac{AB}{DE} = \frac{BC}{EF} = \frac{AC}{DF} $$

\vspace{2mm}
\textbf{Example 1:} Triangle A has angles $40^\circ, 60^\circ, 80^\circ$. Triangle B has angles $40^\circ$ and $80^\circ$. Are they similar?
\textit{Solution:} Yes, by AA Similarity, they share at least two equal angles.

\textbf{Example 2:} A rectangle is $2\times4$. Another is $6\times12$. Are they similar?
\textit{Solution:} Check ratios: $\frac{6}{2} = 3$ and $\frac{12}{4} = 3$. Yes, proportional!
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Guided Practice (Mixed Difficulty)}

\medskip
\textbf{1.} Triangle $XYZ \sim$ Triangle $LMN$. If $\angle X = 50^\circ$, what is $\angle L$? \vspace{1.5cm}

\textbf{2.} Rectangle $A$ is $3\text{ cm}$ by $5\text{ cm}$. Rectangle $B$ is $9\text{ cm}$ by $x\text{ cm}$. If they are similar, find $x$. \vspace{1.5cm}

\textbf{3.} A 5-ft tall student casts a 2-ft shadow. A flagpole casts a 10-ft shadow. How tall is the flagpole? \vspace{1.5cm}

\textbf{4.} Do all similar figures have the same perimeter? \vspace{1.0cm}

\textbf{5.} State the AA Similarity rule in your own words. \vspace{1.5cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Basic Practice (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.0cm, leftmargin=0.6cm]
\item \textbf{[MC]} What must be true for two triangles to be similar?
A) Same area B) Proportional sides, equal angles C) Equal sides

\item \textbf{[MC]} AA Similarity stands for:
A) Area-Area B) Angle-Angle C) Altitude-Altitude

\item If $\triangle ABC \sim \triangle DEF$, and $\angle A = 70^\circ$, then $\angle D =$ \blank
\item If two squares are different sizes, are they similar? (Yes/No) \blank
\item If two rectangles have different shapes, are they similar? (Yes/No) \blank
\item Side ratios: $\frac{10}{5} = \frac{x}{3}$. Find $x$. \blank
\item Side ratios: $\frac{12}{4} = \frac{15}{y}$. Find $y$. \blank
\item Triangle 1 has angles $90^\circ, 45^\circ, 45^\circ$. Triangle 2 has $90^\circ, 45^\circ$. Similar? \blank
\item A $2\times3$ rectangle is dilated by 4. What are the new dimensions? \blank
\item True or False: Congruent figures are also similar figures. \blank
\item True or False: Similar figures are always congruent figures. \blank
\item Scale factor from a $4\text{ cm}$ side to a $20\text{ cm}$ side is: \blank
\item What happens to the angles of a shape when it is dilated? \blank
\end{enumerate}
\vspace{1cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item Two triangles are similar. The sides of the smaller triangle are $3\text{ m}$, $4\text{ m}$, and $5\text{ m}$. The longest side of the larger triangle is $15\text{ m}$. Find the lengths of the other two sides.

\item Quadrilateral $WXYZ$ is similar to Quadrilateral $PQRS$. The scale factor from $WXYZ$ to $PQRS$ is $3:1$. If $PQ = 7\text{ cm}$, find $WX$.

\item Explain why any two circles are always similar to each other.

\item In $\triangle ABC$, line segment $DE$ is drawn parallel to side $BC$, intersecting $AB$ at $D$ and $AC$ at $E$. Explain why $\triangle ADE \sim \triangle ABC$.

\item Are all rhombuses similar? Provide an example to justify your answer.

\item A 6-foot tall person casts a shadow that is $4\text{ feet}$ long. At the same time, a nearby tree casts a shadow that is $20\text{ feet}$ long. Set up a proportion and find the height of the tree.

\item A photograph is $5\text{ inches}$ by $7\text{ inches}$. If you want to make a similar poster that is $35\text{ inches}$ long, how wide must it be?

\item Prove that two equilateral triangles of different sizes are similar using the AA criterion.

\item The ratio of the sides of two similar polygons is $2:5$. If the perimeter of the smaller polygon is $40$, what is the perimeter of the larger polygon?

\item Can a right triangle and an obtuse triangle ever be similar? Explain.
\end{enumerate}
\vspace{1cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems (30-45 mins)}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.2cm, leftmargin=0.6cm]
\item A painter is painting a mural on a large wall. His original sketch is $8\text{ inches}$ by $12\text{ inches}$. The wall is $10\text{ feet}$ tall. If he wants the mural to be mathematically similar to the sketch and fill the height of the wall, how wide will the mural be in feet?

\item To measure the distance across a wide river, a surveyor sets up two similar right triangles on one side of the river using stakes. The small triangle has legs of $10\text{ meters}$ and $15\text{ meters}$. The large triangle shares the $10\text{ m}$ leg but extends across the river. If the total distance down the bank is $60\text{ meters}$, how wide is the river? (Draw a sketch).

\item A computer screen has an aspect ratio (width to height) of $16:9$. If a movie is shot in an aspect ratio of $4:3$ and is displayed on the screen, will the images be similar? Explain what happens to the picture if it's forced to fit the $16:9$ screen.

\item Prove that if $\triangle ABC \sim \triangle DEF$ with a scale factor of $k$, then the Area of $\triangle DEF$ is exactly $k^2$ times the Area of $\triangle ABC$. Use the formula for the area of a triangle.

\item You want to create a scale model of the Eiffel Tower. The real tower is $330\text{ meters}$ tall and its square base is $125\text{ meters}$ on each side. If your model is exactly $1\text{ meter}$ tall, how wide must the base of your model be in centimeters to maintain similarity?

\item A mirror is placed flat on the ground. You stand $2\text{ meters}$ away from the mirror and can see the top of a building in it. The building is $20\text{ meters}$ away from the mirror. If your eyes are $1.5\text{ meters}$ above the ground, how tall is the building? (Hint: The angles of reflection are equal, creating similar triangles).
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
            
        # Clean out existing content area and replace with the new expanded content
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
                # keep up to \noindent \textbf{Description:} ... \vspace{4mm}
                # parts[0] contains everything up to the first customteal box.
                new_content = parts[0] + content_block + "\n\\end{document}\n"
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                    
print("Successfully injected EXPANDED custom questions for Lessons 1-5.")
