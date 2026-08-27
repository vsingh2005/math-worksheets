import os
import re
import shutil

ext_dir = r"C:\Users\singh\Downloads\KSS_6th_Grade_Curriculum"
script_dir = os.path.dirname(os.path.abspath(__file__))
loc_dir = os.path.join(script_dir, "6th_standard")

def extract_body(tex_content):
    match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', tex_content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def extract_preamble(tex_content):
    match = re.search(r'(.*?)\\begin\{document\}', tex_content, re.DOTALL)
    if match:
        return match.group(1)
    return None

for root, dirs, files in os.walk(ext_dir):
    for file in files:
        if file.endswith('.tex') and file.startswith('6_'):
            ext_file_path = os.path.join(root, file)
            rel_path = os.path.relpath(ext_file_path, ext_dir)
            loc_file_path = os.path.join(loc_dir, rel_path)
            
            if os.path.exists(loc_file_path):
                with open(ext_file_path, 'r', encoding='utf-8') as f:
                    ext_content = f.read()
                with open(loc_file_path, 'r', encoding='utf-8') as f:
                    loc_content = f.read()
                    
                ext_body = extract_body(ext_content)
                loc_preamble = extract_preamble(loc_content)
                
                if ext_body and loc_preamble:
                    ext_preamble = extract_preamble(ext_content)
                    if ext_preamble:
                        title_match = re.search(r'\\fancyhead\[C\]\{\\small\\bfseries(.*?)\}', ext_preamble)
                        if title_match:
                            title = title_match.group(1)
                            # Using lambda to avoid escape character issues in replacement string
                            loc_preamble = re.sub(r'\\fancyhead\[C\]\{.*?\}', lambda m: f'\\fancyhead[C]{{\\small\\bfseries{title}}}', loc_preamble)
                            
                    new_content = loc_preamble + "\\begin{document}\n" + ext_body + "\n\\end{document}\n"
                    with open(loc_file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

print("Spliced body contents successfully!")
