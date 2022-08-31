import ipaddress
import json
import os

import pycountry
import requests
from dotenv import load_dotenv
from stats import pretty_stats


def lookup_ip(ip: str) -> str:
    # Load Virus Total api key
    load_dotenv()
    API_KEY = os.getenv("VIRUS_TOTAL_API_KEY")

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"Accept": "application/json", "x-apikey": API_KEY}

    response = requests.get(url, headers=headers)
    decodedResponse = json.loads(response.text)

    if ipaddress.ip_address(ip).is_private:
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
