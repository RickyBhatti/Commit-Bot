# Created by Ricky (https://github.com/RickyBhatti/)
# This script is licensed under the GNU General Public License v3.0.
# Check the GitHub repository for more information. (https://github.com/RickyBhatti/Commit-Bot)

### Configuration
# Logging Options
LOG = True
LOG_FILE = "commit_bot.log"

# Commit Options
NO_COMMIT_CHANCE = 0.1 # 10% chance of NOT committing to GitHub.
MAX_COMMITS = 8 # Maximum number of commits that can be made.

# Cron job.
CRON_JOB_TIME = "0 12 * * *" # Every day at 12:00 pm.

# Output File
OUTPUT_FILE = "commit_bot.txt"

# Imports
from sys import argv
from pathlib import Path
from os import system # Executing the Git commands.
from random import random, randint # Generating a random float between 0 and 1.
from datetime import datetime # Date and time for our file.

# Check if a cronjob exists for this script, if not, create it using crontab.
system("crontab -l > cron.txt")
with open("cron.txt", "r") as f:
    if "commit_bot.py" not in f.read():
        with open("cron.txt", "a") as f:
            f.write(f"{CRON_JOB_TIME} cd {Path.cwd()} && python3 commit_bot.py\n")
            f.close()
            system("crontab cron.txt")
            system("rm -f cron.txt")
    else:
        f.close()
        system("rm -f cron.txt")

# Logging.
def log(message):
    if LOG:
        with open(LOG_FILE, "a") as f:
            f.write(f"{message}\n")
            f.close()

# Create our commit.
def create_commit():
    with open(OUTPUT_FILE, "w") as f:
        f.write(str(datetime.now()))
        f.close()
    system(f"git add {OUTPUT_FILE}")
    system(f"git commit -m \"Update {OUTPUT_FILE}\"")

# Execute the script.
if (random() > NO_COMMIT_CHANCE):
    commits = randint(0, MAX_COMMITS)
    for i in range(commits):
        create_commit()
    system("git push")
    log(f"[{datetime.now()}] Sucessfully committed {commits} time(s).")
else:
    log(f"[{datetime.now()}] No commits were made.")
