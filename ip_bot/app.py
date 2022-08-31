import os
import re

from dotenv import load_dotenv
from lookup import lookup_ip
from slack_bolt import App

load_dotenv()

# Initializes your app with your bot token and signing secret
# https://api.slack.com/start/building/bolt-python#initialize
app = App(token=os.getenv("SLACK_BOT_TOKEN"), signing_secret=os.getenv("SLACK_SIGNING_SECRET"))


# https://slack.dev/bolt-python/concepts
@app.message(re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"))
def say_hello_regex(say, context):
    # regular expression matches are inside of context.matches
    for ip in context["matches"]:
        # Look up IP
        say(lookup_ip(ip))


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
