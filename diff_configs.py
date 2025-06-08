import os
import difflib

def get_latest_two_files(path="backups"):
    files = sorted(os.listdir(path))
    return files[-2:] if len(files) >= 2 else []

def show_diff(file1, file2):
    with open(os.path.join("backups", file1)) as f1, open(os.path.join("backups", file2)) as f2:
        config1 = f1.readlines()
        config2 = f2.readlines()

    diff = difflib.unified_diff(config1, config2, fromfile=file1, tofile=file2)
    diff_output = "".join(diff)
    return diff_output or "✅ No difference between latest backups."

if __name__ == "__main__":
    latest_files = get_latest_two_files()
    if len(latest_files) == 2:
        print(f"🧠 Comparing: {latest_files[0]} ↔ {latest_files[1]}")
        print(show_diff(*latest_files))
    else:
        print("⚠️ Not enough backups to compare.")
