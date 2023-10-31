# Commit Bot
Automatically generate GitHub activity!  

We've all wanted to be the developer that commits every day, but that requires a lot of work. Let's automate it! This bot will automatically generate commit(s) every day, and push them to your GitHub account, allowing you to get that green contributions graph! (Check out the Disclaimers section below for more information.)  

Truthfully, I wouldn't use this. No one cares about your commits. I just got bored one day and decided to make it for fun.  

## Requirements
- [Python 3](https://www.python.org/downloads/)
- Linux OS or Windows WSL (Basically, anything that has crontab installed)

## Configuration
- `LOG`: If you'd like the script to log, set this to `True`. [Default: `True`]
- `LOG_FILE`: The file to log to. [Default: `commit_bot.log`]
- `NO_COMMIT_CHANCE`: The chance that the bot will not commit. (Value between 0 and 1.) [Default: `0.1`]
- `MAX_COMMITS`: The maximum number of commits to generate. [Default: `8`]
- `CRON_JOB_TIME`: The time to run the cron job. [Default: `"0 12 * * *"`]
- `OUTPUT_FILE`: The file to write the output to. (The file that is committed to GitHub) [Default: `commit_bot.txt`]

## Usage
- Create a private (or public, if you want everyone to see it for some reason) repository on GitHub. (Initialize the repository)
- Clone the newly created repository to your machine.
    - Ensure that you're able to execute `git` commands within the directory. As this is required for the script to work. (This may require you to log in to your GitHub account within the directory so that you are able to execute `git` commands.)
- Download this script and place it in the repository's directory.
- Run the script with `python3 commit_bot.py`.
    - The first time the script is run, it will create a cronjob that runs the script at the configured time. (This is done automatically. Once the cronjob has been created, the script will not edit it. If you'd like to change the time, you'd need to either delete the cronjob manually and edit the time in the script configuration, or edit the cronjob manually)

## Contributions
If you've found a bug, you can go ahead and create an [issue](https://github.com/RickyBhatti/Commit-Bot/issues).  
If you've improved the resource, feel free to make a [pull request](https://github.com/RickyBhatti/Commit-Bot/pulls)!  
  
## License
Copyright © 2023 [Ricky Bhatti](https://github.com/RickyBhatti).  
This project is [GNU GPL v3.0](https://github.com/RickyBhatti/Commit-Bot/blob/main/LICENSE) licensed.

## Disclaimers
- I'm not responsible for any damages that may occur. This includes, but is not limited to, any damages caused by the script, any damages caused by the script's configuration, or any damages caused by the script's usage. (Even though this is impossible, but, someone will find a way.)
- This script was designed purely out of my interest since I got bored during a week off. (I'm not using this script, for anyone curious, which is pretty obvious.)
