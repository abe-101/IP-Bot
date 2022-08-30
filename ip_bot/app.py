import os
import re

# Use the package we installed
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"), signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.message(
    re.compile(
        r"(?<![-\.\d])(?:0{0,2}?[0-9]\.|1\d?\d?\.|2[0-5]?[0-5]?\.){3}(?:0{0,2}?[0-9]|1\d?\d?|2[0-5]?[0-5]?)(?![\.\d])"
    )
)
def say_hello_regex(say, context):
    # regular expression matches are inside of context.matches
    for ip in context["matches"]:
        # Look up IP
        say(f"{ip} is good")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
