# IP-Bot


https://user-images.githubusercontent.com/82916197/187593974-ca406ab0-8813-4396-bb16-5d06fbee0bf8.mp4


## Description

a Slack bot that will tell you about an IP address mentioned in a slack message.

# Getting Started

## Creating a Slack app
First you'll need to [create a Slack app](https://api.slack.com/apps?new_app=1&ref=bolt_start_hub)

## Requesting Scopes
Navigate over to the **OAuth & Permissions** sidebar, Scroll down to the **Bot Token Scopes** section and click **Add an OAuth Scope**

Search for:
1. channels:history
2. chat:write

Scroll down to the **User Token Scopes** section and click **Add an OAuth Scope**:
Search for:
1. channels:history

## Fork and Clone this repo
```
git clone git@github.com:<USERNAME>/ip-bot.git
```

## Install Dependency's :
```
pip install -r requirements.txt
```
## Installing Your App

Install your own app by selecting the **Install App** button at the top of the **OAuth & Permissions** page
5.


## Environment Variables

Create a file `ip_bot/.env` Containing you API tokens.
for this project we need:
1. The Bot User OAuth Access Token under the **OAuth & Permissions** sidebar
2. The Slack signing secret. Navigate to the **Basic Information** page from your app management page. Under **App Credentials**, copy the value for Signing Secret.
3. [Virus Total's](https://www.virustotal.com/gui/home/upload) public API. Create an account to get your Token at https://developers.virustotal.com/reference/overview

```
SLACK_BOT_TOKEN=<Your Slack bot Token>
SLACK_SIGNING_SECRET=<Slack signing key>
VIRUS_TOTAL_API_KEY=<Your Virus Total api token>
```

## Using ngrok as a local proxy 

To tr out locally we'll be using ngrok, which allows you to expose a public endpoint that Slack can use to send your app events. If you haven't already, [install ngrok from their website](https://ngrok.com/download).  
Tell ngrok to use port 3000 which Bolt for python uses by default:
```
ngrok http 3000
```

## Subscribing to events

First get the Bolt app running:
```
python ip_bot/app.py
```

On your app configuration page, select the **Event Subscriptions** sidebar. You'll be presented with an input box to enter a Request URL, which is where Slack sends the events your app is subscribed to. For local development, we'll use your ngrok URL from above.

    For example: https://1234abcde.ngrok.io

By default Bolt for Python listens for all incoming requests at the /slack/events route, so for the Request URL you can enter your ngrok URL appended with `/slack/events`.

    For example: https://1234abcde.ngrok.io/slack/events

After you've saved your Request URL, click on **Subscribe to events on behalf of users**, then **Add Workspace Event** and search for `message.channels`. Then **Save Changes** using the button on the bottom right.

## Try It Out

You bot is now ready in action
Open slack messanger and add your bot to any channel and mention an ip address in a message and see what happens

## Credits
* [Abe](https:github.com/abe-101)
<!-- * [b-fullam](https://github.com/b-fullam/Automating-VirusTotal-APIv3-for-IPs-and-URLs)-->
