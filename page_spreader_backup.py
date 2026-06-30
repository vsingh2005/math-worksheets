import os
import re

base_dir = r"c:\Users\singh\Downloads\math_worksheets_repo\8th_standard"

def process_file(file_path, ws_num):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the enumerate block
    enum_match = re.search(r'\\begin\{enumerate\}.*?\n(.*?)\\end\{enumerate\}', content, re.DOTALL)
    if not enum_match:
        return # Skip if no enumerate found (some WS0 might not have it if parsing fails)
        
    items_text = enum_match.group(1)
    # Split items
    items = re.split(r'\\item', items_text)
    items = [item.strip() for item in items if item.strip()]
    
    if len(items) == 0:
        return
        
    # Get the preamble / header (everything before the FIRST tcolorbox after \begin{document})
    # Wait, in the existing files, we have a customteal box for title.
    # We should grab everything up to \begin{enumerate}
    pre_enum = content[:enum_match.start()]
    post_enum = content[enum_match.end():]
    
    # We want to replace the title box in pre_enum with Part A, Part B, etc.
    # Let's just append the new parts.
    
    new_content = ""
    
    # Extract the original title box if possible
    title_box_match = re.search(r'\\begin\{tcolorbox\}\[colback=customteal!20\](.*?)\\end\{tcolorbox\}', pre_enum, re.DOTALL)
    title_text = "Practice"
    if title_box_match:
        # try to get the text inside \textbf{}
        bold_match = re.search(r'\\textbf\{(.*?)\}', title_box_match.group(1))
        if bold_match:
            title_text = bold_match.group(1)
            
    # For WS0, the structure is different (it has an instructional box)
    if ws_num == '0':
        # Split items into 3 parts
        chunk_size = max(2, len(items) // 3)
        chunks = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
        
        # We want to duplicate the instructional box for each part.
        instr_box_match = re.search(r'(\\begin\{tcolorbox\}\[colback=white, colframe=black!25.*?\\end\{tcolorbox\})', pre_enum, re.DOTALL)
        instr_box = instr_box_match.group(1) if instr_box_match else ""
        
        # Build new body
        body = ""
        part_names = ['A', 'B', 'C', 'D', 'E']
        for i, chunk in enumerate(chunks):
            if i > 0:
                body += "\\newpage\n\n"
            
            body += f"% --- PART {part_names[i]} ---\n"
            body += instr_box + "\n\n\\vspace{4mm}\n\n"
            body += "\\begin{tcolorbox}[colback=yellow!15, colframe=orange, boxrule=1.5pt, arc=4mm, left=6mm, right=6mm, top=5mm, bottom=5mm]\n"
            body += f"\\textbf{{Guided Practice Part {part_names[i]}}}\n\n\\medskip\n"
            body += "\\begin{enumerate}[itemsep=2.0cm, leftmargin=0.6cm]\n"
            for item in chunk:
                body += "\\item " + item + "\n"
            body += "\\end{enumerate}\n\\end{tcolorbox}\n\n"
            
        # Replace everything from the first instructional box down
        if instr_box_match:
            before_instr = pre_enum[:instr_box_match.start()]
            new_file_content = before_instr + body + "\\vspace{1cm}\n\\end{document}\n"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_file_content)
                
    else:
        # Worksheets 1, 2, 3
        if ws_num == '1':
            num_chunks = 3
            itemsep = "2.5cm"
        elif ws_num == '2':
            num_chunks = 3
            itemsep = "4.5cm"
        else:
            num_chunks = 3
            itemsep = "6.0cm"
            
        chunk_size = max(1, len(items) // num_chunks)
        chunks = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
        
        body = ""
        part_names = ['A', 'B', 'C', 'D', 'E']
        for i, chunk in enumerate(chunks):
            if i >= len(part_names): break # safeguard
            if i > 0:
                body += "\\newpage\n\n"
            
            body += f"% --- PART {part_names[i]} ---\n"
            body += "\\begin{tcolorbox}[colback=customteal!20]\n"
            body += f"\\large\\textcolor{{black}}{{\\textbf{{Part {part_names[i]}: {title_text}}}}}\n"
            body += "\\end{tcolorbox}\n\n\\vspace{3mm}\n\n"
            
            body += f"\\begin{{enumerate}}[itemsep={itemsep}, leftmargin=0.6cm]\n"
            for item in chunk:
                body += "\\item " + item + "\n"
            body += "\\end{enumerate}\n\n"
            
        # Replace the title box and everything after
        if title_box_match:
            before_title = pre_enum[:title_box_match.start()]
            new_file_content = before_title + body + "\\end{document}\n"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_file_content)

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.tex') and file.startswith('8_'):
            ws_num = file.split('_')[2].replace('.tex', '')
            file_path = os.path.join(root, file)
            process_file(file_path, ws_num)
            
print("Successfully spread questions across multiple pages (4-6 pages per worksheet).")
