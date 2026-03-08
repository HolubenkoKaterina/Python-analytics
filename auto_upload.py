import os
import shutil
import subprocess
from datetime import datetime

SOURCE_FOLDER = r"C:\Users\user\Desktop\питон для гита"
REPO_FOLDER   = r"C:\Users\user\Documents\Object-oriented-programming-tasks"

def run_git(cmd):
    subprocess.run(cmd, cwd=REPO_FOLDER, shell=True)

def main():
    files = [
        f for f in os.listdir(SOURCE_FOLDER)
        if os.path.isfile(os.path.join(SOURCE_FOLDER, f))
    ]

    if not files:
        print("Файлов нет")
        return

    # берем ОДИН файл
    file = files[0]

    src = os.path.join(SOURCE_FOLDER, file)
    dst = os.path.join(REPO_FOLDER, file)

    shutil.move(src, dst)

    run_git("git add .")
    run_git(f'git commit -m "daily upload {file} {datetime.now().strftime("%Y-%m-%d")}"')
    run_git("git push")

    print(f"Загружен файл: {file}")

if __name__ == "__main__":
    main()
