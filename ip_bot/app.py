import os
import re

from dotenv import load_dotenv

from lookup import virus_total_api_call, make_ip_info_sting, is_private_range, validate_ip_address
from slack_bolt import App

load_dotenv()

# Initializes your app with your bot token and signing secret
# https://api.slack.com/start/building/bolt-python#initialize
app = App(token=os.getenv("SLACK_BOT_TOKEN"), signing_secret=os.getenv("SLACK_SIGNING_SECRET"))


# https://slack.dev/bolt-python/concepts
@app.message(re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"))
def say_hello_regex(say, context):
    # regular expression matches are inside of context.matches
    for ip_string in context["matches"]:
        # Look up IP
        if not validate_ip_address(ip_string):
            continue
        if is_private_range(ip_string):
            say(f"{ip_string} is reserved for private networks.")
        say(make_ip_info_sting(virus_total_api_call(ip_string)))


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
