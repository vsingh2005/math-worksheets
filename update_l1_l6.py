import os
import re
import glob

base_dir = r"c:\Users\singh\Downloads\math_worksheets_repo\8th_standard"

# Map of Lesson Number to the Questions block for Worksheets 0 to 3
questions_data = {
    1: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Conceptual Understanding}

\medskip
\textbf{1.} A translation slides a figure, a reflection flips it, and a rotation turns it. Explain why the size and shape of a figure do not change when any of these three transformations are applied.

\vspace{2cm}

\textbf{2.} On a coordinate plane, if a point $A(x, y)$ is translated 3 units right and 2 units down, what are the coordinates of the new point $A'$?

\vspace{2cm}
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Deeper Thinking Problem}

\medskip
\textbf{3.} Draw a triangle on a coordinate plane with vertices $P(-2, 1)$, $Q(1, 4)$, and $R(2, -1)$. First, reflect the triangle across the $y$-axis to form $P'Q'R'$. Then, translate it 1 unit up. List the final coordinates.
\vspace{3cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Multiple Choice \& Practice}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.5cm, leftmargin=0.6cm]
\item \textbf{[Multiple Choice]} Which transformation represents a ``flip'' over a line?
\begin{enumerate}[label=\Alph*)]
    \item Translation
    \item Reflection
    \item Rotation
    \item Dilation
\end{enumerate}

\item Translate the point $(-4, 5)$ by moving it 6 units to the right and 1 unit down. What is the new coordinate?

\item Reflect the point $(3, 2)$ across the $x$-axis. What is the new coordinate?

\item Rotate the point $(1, 4)$ by $90^\circ$ clockwise around the origin $(0,0)$. Where does it land?
\end{enumerate}
\vspace{2cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Short Answer Applications}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item A square has vertices at $(1, 1)$, $(1, 3)$, $(3, 3)$, and $(3, 1)$. Apply a translation of $(x-2, y+1)$ to all four vertices. List the new coordinates.

\item If a figure is reflected across the $y$-axis, what happens to the $x$ and $y$ coordinates of each point? Write a general rule $(x, y) \rightarrow (?, ?)$.

\item A triangle is rotated $180^\circ$ around the origin. If one of its vertices was at $(-5, -2)$, what are the coordinates of its image?

\item Draw or describe a situation where a translation and a reflection yield the exact same image.
\end{enumerate}
\vspace{2cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Advanced Word Problems}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item A video game designer wants to program a character to jump from a platform at $(2, 5)$ to another platform at $(7, 8)$. Write the translation rule $(x, y) \rightarrow (x+a, y+b)$ that represents this jump.

\item In a mirror maze, a laser beam originates at $(-3, -4)$ and is reflected across the $x$-axis by a mirror. It is then reflected across the $y$-axis by a second mirror. What are the final coordinates of the laser beam's target?

\item A drone maps a rectangular field with corners at $(0,0)$, $(0, 10)$, $(20, 10)$, and $(20, 0)$. The drone operator rotates the map $90^\circ$ counterclockwise on their screen. What are the new coordinates of the field's corners on the screen?

\item Prove that rotating a figure $180^\circ$ is mathematically the same as reflecting it across the $x$-axis and then reflecting it across the $y$-axis.
\end{enumerate}
\vspace{2cm}
"""
    },
    2: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Conceptual Understanding}

\medskip
\textbf{1.} What does it mean for two figures to be "congruent"? How can you prove two figures are congruent using sequences of transformations?

\vspace{2cm}

\textbf{2.} If you apply a translation followed by a reflection, does the final figure have the same size and shape as the original? Why or why not?

\vspace{2cm}
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Deeper Thinking Problem}

\medskip
\textbf{3.} Figure A is a triangle with vertices $(1, 1)$, $(1, 4)$, and $(3, 1)$. Figure B is a triangle with vertices $(-1, 1)$, $(-1, 4)$, and $(-3, 1)$. Describe a sequence of rigid transformations that maps Figure A onto Figure B.
\vspace{3cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Identifying Sequences}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=1.5cm, leftmargin=0.6cm]
\item \textbf{[Multiple Choice]} Which sequence of transformations maps the point $(2, 3)$ to $(-2, -3)$?
\begin{enumerate}[label=\Alph*)]
    \item Reflect across $x$-axis, then translate down 6
    \item Reflect across $y$-axis, then reflect across $x$-axis
    \item Translate left 4, then up 6
    \item Rotate $90^\circ$ clockwise
\end{enumerate}

\item Point $M(4, 5)$ is translated left 2 units, then reflected across the $x$-axis. Find $M''$.

\item Can a figure be mapped onto a congruent figure using only rotations and translations (no reflections)? Explain briefly.
\end{enumerate}
\vspace{2cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Constructing Sequences}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item A polygon is mapped onto another polygon by translating it down 3 units and reflecting it across the $y$-axis. If a vertex of the image is at $(4, -1)$, what was the coordinate of the original vertex?

\item Determine whether the following statement is true or false: "The order in which you perform a sequence of transformations does not matter." Provide a counter-example if false.

\item Find a sequence of two rigid motions that maps the segment from $(1, 1)$ to $(1, 4)$ onto the segment from $(2, 2)$ to $(5, 2)$.
\end{enumerate}
\vspace{2cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Complex Proofs \& Applications}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item A robotics arm is programmed to move objects using sequences of transformations. It picks up a box at $(0, 5)$ and needs to place it perfectly at $(-5, 0)$ with the same orientation. Describe the rigid motions the arm must execute.

\item In graphic design, a logo is copied and transformed. The original logo is in Quadrant I. The designer wants a mirror image of the logo placed in Quadrant III. Describe a sequence of two transformations to achieve this.

\item Two friends are comparing shapes. Shape $X$ and Shape $Y$ have the same side lengths and angle measures, but Shape $Y$ is a mirror image of Shape $X$. Can Shape $X$ be mapped onto Shape $Y$ using only translations and rotations? Explain your reasoning.
\end{enumerate}
\vspace{2cm}
"""
    },
    3: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Conceptual Understanding}

\medskip
\textbf{1.} When two parallel lines are cut by a transversal, name three pairs of angles that are congruent.

\vspace{2cm}

\textbf{2.} What is the sum of the interior angles of a triangle? How can parallel line theorems help prove this?

\vspace{2cm}
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Deeper Thinking Problem}

\medskip
\textbf{3.} Lines $l$ and $m$ are parallel. A transversal cuts through them. One of the interior angles measures $110^\circ$. Find the measures of the other seven angles formed by the intersection and label them as corresponding, alternate interior, or supplementary to the $110^\circ$ angle.
\vspace{3cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Identifying Angles}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item \textbf{[Multiple Choice]} If two parallel lines are cut by a transversal, which of the following angle pairs are supplementary (add up to $180^\circ$)?
\begin{enumerate}[label=\Alph*)]
    \item Alternate interior angles
    \item Corresponding angles
    \item Vertical angles
    \item Same-side interior angles
\end{enumerate}

\item In a triangle, two angles measure $45^\circ$ and $65^\circ$. What is the measure of the third angle?

\item True or False: Alternate exterior angles are congruent when lines are parallel.

\item An exterior angle of a triangle measures $120^\circ$. If one of the remote interior angles is $50^\circ$, what is the measure of the other remote interior angle?
\end{enumerate}
\vspace{2cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Solving for Unknowns}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item Two parallel lines are intersected by a transversal. The measure of an acute angle is given by $(3x + 15)^\circ$ and the measure of the corresponding angle is $(5x - 5)^\circ$. Find $x$.

\item In a triangle, the angles are represented by $x$, $2x$, and $3x$. Find the measure of each angle. What kind of triangle is this?

\item Two parallel lines are cut by a transversal. Same-side interior angles measure $(4y + 20)^\circ$ and $(6y - 10)^\circ$. Calculate the value of $y$ and the measure of both angles.
\end{enumerate}
\vspace{2cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Real-World Geometry Problems}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item A city planner is designing a set of parallel streets intersected by a diagonal avenue. She wants the acute angle at the intersection to be exactly $40^\circ$. Calculate the measures of all other angles at the intersection points to ensure the design meets safety codes.

\item The frame of a bicycle forms a triangle. If the top tube and the down tube meet at a $65^\circ$ angle, and the down tube and the seat tube meet at a $45^\circ$ angle, what is the angle between the top tube and the seat tube?

\item Prove that the sum of the interior angles of a triangle is $180^\circ$ by drawing a line parallel to one side of the triangle that passes through the opposite vertex.
\end{enumerate}
\vspace{2cm}
"""
    },
    4: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Conceptual Understanding}

\medskip
\textbf{1.} What is a dilation? Explain what a scale factor greater than 1 does to a figure versus a scale factor between 0 and 1.

\vspace{2cm}

\textbf{2.} Does a dilation preserve the angle measures of a shape? Does it preserve side lengths?

\vspace{2cm}
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Deeper Thinking Problem}

\medskip
\textbf{3.} A rectangle with vertices $(0,0)$, $(0,2)$, $(4,2)$, and $(4,0)$ is dilated with the center of dilation at the origin $(0,0)$ and a scale factor of $\frac{1}{2}$. What are the new coordinates? Draw a quick sketch of both rectangles on the same coordinate plane.
\vspace{3cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Applying Scale Factors}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item \textbf{[Multiple Choice]} If a square with a side length of 5 is dilated by a scale factor of 3, what is the new side length?
\begin{enumerate}[label=\Alph*)]
    \item 8
    \item 15
    \item 1.66
    \item 45
\end{enumerate}

\item Point $P(2, -6)$ is dilated from the origin by a scale factor of $0.5$. Find $P'$.

\item A triangle has an area of $10\text{ cm}^2$. If it is dilated by a scale factor of 2, what happens to its side lengths?

\item A photograph is $4\text{ inches}$ wide and $6\text{ inches}$ tall. It is enlarged by a scale factor of $1.5$. What are the new dimensions?
\end{enumerate}
\vspace{2cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Coordinate Geometry with Dilations}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item A pentagon is dilated from the origin resulting in a new pentagon. If a vertex at $(4, 8)$ maps to $(1, 2)$, what is the scale factor of the dilation?

\item A segment with endpoints $A(-3, 6)$ and $B(9, -3)$ is dilated by a scale factor of $\frac{2}{3}$ centered at the origin. Find the length of the new segment $A'B'$. (Hint: find the new coordinates first, or use the original length).

\item Write the algebraic rule for a dilation centered at the origin with a scale factor of $k$. Use notation $(x, y) \rightarrow (?, ?)$.
\end{enumerate}
\vspace{2cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Scale Models & Real-World Application}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item An architect is creating a blueprint for a house. The actual living room is $20\text{ feet}$ long and $15\text{ feet}$ wide. On the blueprint, the living room is $8\text{ inches}$ long. What is the scale factor from the actual room to the blueprint? How wide is the room on the blueprint?

\item A toy manufacturer makes a model car that is a dilation of a real car. The real car is $180\text{ inches}$ long and the model is $5\text{ inches}$ long. If the real car's wheel has a diameter of $24\text{ inches}$, what is the diameter of the model car's wheel?

\item When you zoom in on a digital map by $200\%$, you are applying a dilation with what scale factor? If a park is represented by a $2\text{ cm}$ by $3\text{ cm}$ rectangle on screen, what are its dimensions after zooming in?
\end{enumerate}
\vspace{2cm}
"""
    },
    5: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Conceptual Understanding}

\medskip
\textbf{1.} What makes two figures "similar"? Compare and contrast similarity with congruence.

\vspace{2cm}

\textbf{2.} If Figure A is similar to Figure B, what must be true about their corresponding angles and their corresponding side lengths?

\vspace{2cm}
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Deeper Thinking Problem}

\medskip
\textbf{3.} Describe a sequence of transformations (including a dilation) that maps a $2\times2$ square centered at the origin onto a $6\times6$ square whose bottom-left corner is at $(4, 4)$.
\vspace{3cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Identifying Similar Figures}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item \textbf{[Multiple Choice]} Which of the following is ALWAYS true about similar triangles?
\begin{enumerate}[label=\Alph*)]
    \item They have the same perimeter.
    \item They have exactly the same side lengths.
    \item They have proportional side lengths and equal angle measures.
    \item They are right triangles.
\end{enumerate}

\item Triangle $ABC$ is similar to Triangle $DEF$. If angle $A$ is $50^\circ$ and angle $B$ is $60^\circ$, what is the measure of angle $F$?

\item A rectangle is $4\text{ cm}$ wide and $10\text{ cm}$ long. Is it similar to a rectangle that is $6\text{ cm}$ wide and $15\text{ cm}$ long? Prove it using ratios.
\end{enumerate}
\vspace{2cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Solving for Unknown Sides}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item Two triangles are similar. The sides of the smaller triangle are $3\text{ m}$, $4\text{ m}$, and $5\text{ m}$. The longest side of the larger triangle is $15\text{ m}$. Find the lengths of the other two sides.

\item A 6-foot tall person casts a shadow that is $4\text{ feet}$ long. At the same time, a nearby tree casts a shadow that is $20\text{ feet}$ long. Assuming the triangles formed by the objects and their shadows are similar, how tall is the tree?

\item Quadrilateral $WXYZ$ is similar to Quadrilateral $PQRS$. The scale factor from $WXYZ$ to $PQRS$ is $3:1$. If $PQ = 7\text{ cm}$, find $WX$.
\end{enumerate}
\vspace{2cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Proving Similarity}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item A painter is painting a mural on a large wall. His original sketch is $8\text{ inches}$ by $12\text{ inches}$. The wall is $10\text{ feet}$ tall. If he wants the mural to be similar to the sketch and fill the height of the wall, how wide will the mural be in feet?

\item Prove that any two squares are always similar to each other. Use the definition of similarity (rigid motions and dilations) in your explanation.

\item In $\triangle ABC$, line segment $DE$ is drawn parallel to side $BC$, intersecting $AB$ at $D$ and $AC$ at $E$. Prove that $\triangle ADE$ is similar to $\triangle ABC$.
\end{enumerate}
\vspace{2cm}
"""
    },
    6: {
        0: r"""
\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Conceptual Understanding}

\medskip
\textbf{1.} What is slope? How is the slope of a line related to the ratio of the vertical change to the horizontal change (rise over run)?

\vspace{2cm}

\textbf{2.} Explain how you can use similar triangles to prove that the slope is the same between any two distinct points on a non-vertical line.

\vspace{2cm}
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Deeper Thinking Problem}

\medskip
\textbf{3.} Draw a line passing through the origin $(0,0)$ and the point $(4, 2)$. Pick a third point on this line. Draw two different right triangles using these points to calculate the slope. Show that both triangles yield the same slope $m = \frac{1}{2}$.
\vspace{3cm}
\end{tcolorbox}
""",
        1: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Calculating Slope}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]
\item \textbf{[Multiple Choice]} The formula to calculate slope $m$ between two points $(x_1, y_1)$ and $(x_2, y_2)$ is:
\begin{enumerate}[label=\Alph*)]
    \item $m = \frac{x_2 - x_1}{y_2 - y_1}$
    \item $m = \frac{y_2 - y_1}{x_2 - x_1}$
    \item $m = y_2 - y_1 \cdot x_2 - x_1$
    \item $m = \frac{x_1 + x_2}{2}$
\end{enumerate}

\item Find the slope of the line that passes through $(1, 3)$ and $(3, 7)$.

\item Find the slope of the line passing through $(-2, 5)$ and $(4, -1)$.

\item Write the equation $y = mx$ for a line that passes through the origin and has a slope of $3$.
\end{enumerate}
\vspace{2cm}
""",
        2: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Similar Triangles on Lines}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item A line passes through $(0,0)$, $(2, 3)$, and $(4, 6)$. Create two similar triangles: one using $(0,0)$ and $(2,3)$, and another using $(2,3)$ and $(4,6)$. Calculate the rise over run for both to prove the slope is constant.

\item Find the equation of a proportional relationship (which passes through the origin) if it includes the point $(5, 15)$.

\item True or False: If two right triangles are drawn along the same line, the ratio of their legs (vertical to horizontal) will always be equivalent to the line's slope. Justify your answer.
\end{enumerate}
\vspace{2cm}
""",
        3: r"""
\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Applications of Slope}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]
\item A ramp needs to be built with a slope of $\frac{1}{12}$ to meet accessibility standards. If the ramp must reach a doorway that is $2\text{ feet}$ above the ground, how far from the building must the ramp start (horizontal distance)? Show your work using a proportion or similar triangles.

\item Water is filling a tank at a constant rate. After $2\text{ minutes}$, there are $10\text{ gallons}$ in the tank. After $5\text{ minutes}$, there are $25\text{ gallons}$. Graph this relationship, draw a slope triangle, and write the equation of the line in $y = mx$ form. What does the slope represent in this context?

\item Explain why the equation for any line passing through the origin can be written as $y = mx$. Use the definition of slope in your explanation.
\end{enumerate}
\vspace{2cm}
"""
    }
}

for lesson_num, ws_data in questions_data.items():
    # find the folder for this lesson
    # folder name starts with f"Lesson_{lesson_num}_"
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
            
        # We want to replace everything from the first \begin{tcolorbox}[colback=white...
        # or \begin{tcolorbox}[colback=customteal!20]\n\large\textcolor{black}{\textbf{Apply Concepts}}
        # basically, the main content area.
        
        if ws_num == 0:
            # For worksheet 0, split at \begin{tcolorbox}[colback=white, colframe=black!25
            parts = file_content.split(r"\begin{tcolorbox}[colback=white, colframe=black!25")
            if len(parts) == 2:
                new_content = parts[0] + content_block + "\n\\end{document}\n"
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
        else:
            # For worksheet 1, 2, 3, split at \begin{tcolorbox}[colback=customteal!20] \large\textcolor{black}{\textbf{Apply Concepts}}
            search_str = r"\begin{tcolorbox}[colback=customteal!20]" + "\n" + r"\large\textcolor{black}{\textbf{Apply Concepts}}"
            parts = file_content.split(search_str)
            if len(parts) == 2:
                # keep up to \noindent \textbf{Description:} ... \vspace{4mm}
                new_content = parts[0] + content_block + "\n\\end{document}\n"
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                    
print("Successfully injected custom questions for Lessons 1-6.")
