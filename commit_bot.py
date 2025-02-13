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
from datetime import datetime, date, timedelta # Date and time for our file.

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
    print(message)
    if LOG:
        with open(LOG_FILE, "a") as f:
            f.write(f"{message}\n")
            f.close()

# Create our commit.
def create_commit(commit_date):
    with open(OUTPUT_FILE, "w") as f:
        f.write(str(datetime.now()))
        f.close()
    system(f"git add {OUTPUT_FILE}")
    if commit_date:
        system(f"git commit --date \"{commit_date}\" -m \"Update {OUTPUT_FILE}\"")
    else:
        system(f"git commit -m \"Update {OUTPUT_FILE}\"")

# Parse the arguments.
def parse_args():
    if len(argv) == 1:
        return None, None
    
    try: 
        if len(argv) == 2:
            return datetime.strptime(argv[1], "%m-%d-%Y"), date.today().strftime("%m-%d-%Y")
    
        return datetime.strptime(argv[1], "%m-%d-%Y"), datetime.strptime(argv[2], "%m-%d-%Y")
    except ValueError:
        print("Invalid date format. Please use the following format: MM-DD-YYYY.")
        exit(1)

    return None, None # Should never reach this point.

if __name__ == "__main__":
    start_date, end_date = parse_args()
    
    if start_date and end_date:
        log(f"Dates provided: {start_date} - {end_date}, running in manual mode.")
        current_date = start_date
        while current_date <= end_date:
            commits = randint(0, MAX_COMMITS)
            for i in range(commits):
                # create_commit(current_date.strftime("%Y-%m-%d %H:%M:%S"))
                pass
            # system("git push")
            log(f"[{datetime.now()}] Sucessfully committed {commits} time(s).")
            current_date += timedelta(days=1)
    else:
        log(f"No dates were provided. Running in cron mode.")
        # Execute the script.
        if (random() > NO_COMMIT_CHANCE):
            commits = randint(0, MAX_COMMITS)
            for i in range(commits): # TODO: Re-enable this later.
                # create_commit()
                pass
            # system("git push")
            log(f"[{datetime.now()}] Sucessfully committed {commits} time(s).")
        else:
            log(f"[{datetime.now()}] No commits were made.")
