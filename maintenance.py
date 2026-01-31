import os
import shutil
from datetime import datetime

log_file = os.getenv("LOG_FILE_PATH", "logs/app.log")
backup_file = log_file + ".bak"
max_size = 1024

def main():
    print(f"[{datetime.now()}] starting maintenance...")

    if not os.path.exists(log_file):
        print(f"ERROR: {log_file} does not exists")
        exit(1)

    size = os.path.getsize(log_file)
    print(f"Current size: {size} bytes")

    if size > max_size:
        print("file is too Large. Rotating...")
        shutil.move(log_file, backup_file)

        with open(log_file, "w") as f:
            f.write("---Starting new log---")

        print(f"rotation done backup at: {backup_file}")
    else:
        print("Size is Ok. No action.")

if __name__ == "__main__":
    main()


