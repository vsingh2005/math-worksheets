import os
import shutil

repo_dir = r"C:\Users\singh\Downloads\math_worksheets_repo"
sixth_dir = os.path.join(repo_dir, "6th_standard")

if not os.path.exists(sixth_dir):
    os.makedirs(sixth_dir)

# move all Lesson_* and 6th_Grade_Placement_Test etc if they exist
for item in os.listdir(repo_dir):
    if item == "6th_standard" or item == ".git":
        continue
    src = os.path.join(repo_dir, item)
    dst = os.path.join(sixth_dir, item)
    shutil.move(src, dst)
    print(f"Moved {item} to 6th_standard")
