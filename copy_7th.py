import os
import shutil
import glob

src_dir = r"c:\Users\singh\Downloads\KSS_7th_Grade_Curriculum"
dst_dir = r"c:\Users\singh\Downloads\math_worksheets_repo\7th_standard"

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# We want to copy the placement test and all Lesson_* directories, but ONLY .tex files
tex_files = glob.glob(os.path.join(src_dir, "**", "*.tex"), recursive=True)

copied_count = 0
for tex_file in tex_files:
    rel_path = os.path.relpath(tex_file, src_dir)
    target_path = os.path.join(dst_dir, rel_path)
    
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    shutil.copy2(tex_file, target_path)
    copied_count += 1

print(f"Copied {copied_count} .tex files to 7th_standard")
