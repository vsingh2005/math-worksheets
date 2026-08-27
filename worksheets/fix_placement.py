import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "6th_standard", "Placement Exam.tex")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The proper footer section from standard 6/7/8
proper_footer = r"""\newcommand{\logowidth}{3cm}
\setlength{\headheight}{20pt}
\setlength{\footskip}{40pt}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\small\bfseries 6th Grade Math Curriculum --- Comprehensive Placement Test}
\fancyfoot[L]{\raisebox{2pt}{\includegraphics[width=\logowidth]{kss.png}}}
\fancyfoot[C]{\thepage}

\renewcommand{\footrulewidth}{0.2pt}"""

# Regex to replace the HEADER / FOOTER block
content = re.sub(
    r'\\setlength\{\\headheight\}\{20pt\}.*?\\renewcommand\{\\footrulewidth\}\{0.2pt\}',
    proper_footer.replace('\\', '\\\\'),
    content,
    flags=re.DOTALL
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Placement Exam footers.")
