import os

year = input("Year: ")
lang = input("Language: ")
day = input("Day: ").zfill(2)

os.chdir(f"{year}/{lang}/day{day}")

if lang == "python":
    os.system(f"python -m day{day}")
