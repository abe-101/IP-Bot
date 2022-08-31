import json
import os
import re

import pycountry
import requests
from dotenv import load_dotenv

from stats import pretty_stats


def is_private_ip(ip: str) -> bool:
    pattern = re.compile(
        r"(^0\.)|(^10\.)|(^100\.6[4-9]\.)|(^100\.[7-9]\d\.)|(^100\.1[0-1]\d\.)|(^100\.12[0-7]\.)|(^127\.)|(^169\.254\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.0\.0\.)|(^192\.0\.2\.)|(^192\.88\.99\.)|(^192\.168\.)|(^198\.1[8-9]\.)|(^198\.51\.100\.)|(^203.0\.113\.)|(^22[4-9]\.)|(^23[0-9]\.)|(^24[0-9]\.)|(^25[0-5]\.)"  # noqa: E501
    )
    if pattern.search(ip):
        return True
    else:
        return False


def lookup_ip(ip: str) -> str:
    # Load Virus Total api key
    load_dotenv()
    API_KEY = os.getenv("VIRUS_TOTAL_API_KEY")

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"Accept": "application/json", "x-apikey": API_KEY}

    response = requests.get(url, headers=headers)
    decodedResponse = json.loads(response.text)

    if is_private_ip(ip):
        return f"{ip} is used for private networks."

    try:

        # Reteive country name from country code
        country_code = decodedResponse["data"]["attributes"]["country"]
        country = pycountry.countries.get(alpha_2=country_code)

        # stats
        stats = decodedResponse["data"]["attributes"]["last_analysis_stats"]
        stat_str = pretty_stats(stats)

        return f"{ip} originates from {country.flag} {country.name}, {stat_str}."
    except KeyError:
        return decodedResponse["error"]["message"]
