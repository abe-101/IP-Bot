# ip-bot

https://user-images.githubusercontent.com/82916197/187593496-2d626495-82f1-4451-bf6c-1411f9cb9120.mp4

## Description

ip-bot is a Slack bot that will provide contextual information about an ip address mentioned in a slack message.


## Set up

Clone this repo
```
git clone git@github.com:abe-101/ip-bot.git
```

## Install Dependency's :
```
pip install -r requirements.txt
```

## Configure slack app
Follow Slack's step-by-step guide to [Building an app with Bolt for Python](https://api.slack.com/start/building/bolt-python)

For this project we need to ad more scope
Bot Token Scopes:
1. channels:history
2. channels:read
3. chat:write

User Token Scopes:
1. channels:history


## Environment Variables
To avoid having to export your variables create a file `ip_bot/.env` with your api keys and ip-bot will handle the rest 😀

ip-bot uses [Virus Total's](https://www.virustotal.com/gui/home/upload) public API.
Create an account to get your Token at https://developers.virustotal.com/reference/overview
```
SLACK_BOT_TOKEN=<Your Slack bot Token>
SLACK_SIGNING_SECRET=<Slack signing key>
VIRUS_TOTAL_API_KEY=<Your Virus Total api token>
```


## Credits
* [Abe](https:github.com/abe-101)
* [b-fullam](https://github.com/b-fullam/Automating-VirusTotal-APIv3-for-IPs-and-URLs)
