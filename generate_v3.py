import re
import os
import shutil

curriculum_file = r"c:\Users\singh\Downloads\math_worksheets_repo\8th_standard\8th Grade Full Year Curriculum.tex"
base_dir = r"c:\Users\singh\Downloads\math_worksheets_repo\8th_standard"

with open(curriculum_file, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r"^\s*(\d+)\s*&\s*(.+?)\s*&\s*(.+?)\s*&\s*(.+?)\s*&\s*(.+?)\s*\\\\", re.MULTILINE)

matches = pattern.findall(content)

template_0 = r"""% [[UPPER_TITLE]] - WORKSHEET 0 (IN-CLASS INSTRUCTION)
\documentclass[12pt, letterpaper, fleqn]{article}

\usepackage{graphicx}
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\usepackage{amsmath, amssymb}
\usepackage{fancyhdr}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{enumitem}
\usepackage{geometry}
\usepackage{tikz}
\usepackage{needspace}
\usepackage{multicol}

\usetikzlibrary{arrows.meta, calc}

\usepackage{times}
\geometry{letterpaper, top=1.25in, bottom=1.25in, marginpar=0.5in}

\newcommand{\logowidth}{3cm}
\setlength{\headheight}{20pt}
\setlength{\footskip}{40pt}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\small\bfseries [[TITLE]]}
\fancyfoot[L]{\raisebox{2pt}{\includegraphics[width=\logowidth]{../kss.png}}}
\fancyfoot[C]{\thepage}
\fancyfoot[R]{[[LESSON_NUM]].0}

\renewcommand{\footrulewidth}{0.2pt}

\definecolor{customteal}{HTML}{2fbdb9}

\newcommand{\blank}{\underline{\hspace{2.2cm}}}
\newcommand{\blanklong}{\underline{\hspace{6.5cm}}}
\newcommand{\blankshorter}{\underline{\hspace{1.5cm}}}

\begin{document}

\textbf{Name:} \underline{\hspace{5cm}}
\hfill
\textbf{Date:} \underline{\hspace{3cm}}\\

\begin{tcolorbox}[colback=customteal!20]
    \large\textcolor{black}{\textbf{Foundation: [[TITLE]]}}
\end{tcolorbox}

\vspace{3mm}

\noindent
\textbf{Description:} [[DESC]]

\vspace{4mm}

\begin{tcolorbox}[colback=white, colframe=black!25, boxrule=0.6pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Conceptual Understanding}

\medskip
\textbf{1.} Explain the core concept behind [[TITLE]] in your own words.

\vspace{2cm}

\textbf{2.} How does the standard [[STD]] apply to this topic?

\vspace{2cm}
\end{tcolorbox}

\vspace{4mm}

\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]
\textbf{Deeper Thinking Problem}

\medskip
\textbf{3.} Provide a real-world example where you would need to use [[TITLE]]. Work out a sample problem.

\vspace{3cm}
\end{tcolorbox}

\end{document}
"""

template_1 = r"""% [[UPPER_TITLE]] - WORKSHEET [[WS_NUM]]
\documentclass[12pt, letterpaper, fleqn]{article}

\usepackage{graphicx}
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\usepackage{amsmath, amssymb}
\usepackage{fancyhdr}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{enumitem}
\usepackage{geometry}
\usepackage{tikz}
\usepackage{needspace}
\usepackage{multicol}

\usetikzlibrary{arrows.meta, calc}

\usepackage{times}
\geometry{letterpaper, top=1.25in, bottom=1.25in, marginpar=0.5in}

\newcommand{\logowidth}{3cm}
\setlength{\headheight}{20pt}
\setlength{\footskip}{40pt}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\small\bfseries [[TITLE]]}
\fancyfoot[L]{\raisebox{2pt}{\includegraphics[width=\logowidth]{../kss.png}}}
\fancyfoot[C]{\thepage}
\fancyfoot[R]{[[LESSON_NUM]].[[WS_NUM]]}

\renewcommand{\footrulewidth}{0.2pt}

\definecolor{customteal}{HTML}{2fbdb9}

\newcommand{\blank}{\underline{\hspace{2.2cm}}}
\newcommand{\blanklong}{\underline{\hspace{6.5cm}}}
\newcommand{\blankshorter}{\underline{\hspace{1.5cm}}}

\begin{document}

\textbf{Name:} \underline{\hspace{5cm}}
\hfill
\textbf{Date:} \underline{\hspace{3cm}}\\

\begin{tcolorbox}[colback=customteal!20]
    \large\textcolor{black}{\textbf{Practice: [[TITLE]]}}
\end{tcolorbox}

\vspace{3mm}

\noindent
\textbf{Description:} [[DESC]]

\vspace{4mm}

\begin{tcolorbox}[colback=customteal!20]
\large\textcolor{black}{\textbf{Apply Concepts}}
\end{tcolorbox}

\vspace{3mm}

\begin{enumerate}[itemsep=2.5cm, leftmargin=0.6cm]

\item Solve a basic problem involving [[TITLE]]. Show your steps.

\item Apply the principles of [[TITLE]] to find the missing value in a given scenario.

\item Write a word problem that requires the use of [[TITLE]] to solve, and then solve it.

\item Review: How is this topic related to the previous lesson?

\end{enumerate}

\vspace{3cm}

\end{document}
"""

for match in matches:
    num_str, unit, title, desc, std = match
    num = int(num_str)
    title = title.replace(r"\&", "&").strip()
    
    clean_title = re.sub(r'[^a-zA-Z0-9]', '_', title)
    clean_title = re.sub(r'_+', '_', clean_title).strip('_')
    
    folder_name = f"Lesson_{num}_{clean_title}"
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    for ws_num in range(4):
        file_name = f"8_{num}_{ws_num}.tex"
        file_path = os.path.join(folder_path, file_name)
        
        args = {
            "[[UPPER_TITLE]]": title.upper(),
            "[[TITLE]]": title,
            "[[DESC]]": desc.replace(r"\&", "&").replace("\n", " ").strip(),
            "[[LESSON_NUM]]": f"8.{num}",
            "[[WS_NUM]]": str(ws_num),
            "[[STD]]": std.strip()
        }
        
        if ws_num == 0:
            content = template_0
        else:
            content = template_1
            
        for k, v in args.items():
            content = content.replace(k, v)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
