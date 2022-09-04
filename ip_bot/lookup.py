import ipaddress
import os

import pycountry
import requests
from dotenv import load_dotenv
from stats import pretty_stats


def validate_ip_address(ip_string: str) -> bool:
    try:
        ipaddress.ip_address(ip_string)
        return True
    except ValueError:
        return False


def is_private_range(ip_string: str) -> bool:
    return ipaddress.ip_address(ip_string).is_private


def virus_total_api_call(ip: str):
    # Load Virus Total api key
    load_dotenv()
    API_KEY = os.getenv("VIRUS_TOTAL_API_KEY")

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"Accept": "application/json", "x-apikey": API_KEY}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def make_ip_info_sting(decodedResponse) -> str:
    ip_string = decodedResponse["data"]["id"]

    # Reteive country name from country code
    country_code = decodedResponse["data"]["attributes"]["country"]
    country = pycountry.countries.get(alpha_2=country_code)

    # stats
    stats = decodedResponse["data"]["attributes"]["last_analysis_stats"]
    stat_str = pretty_stats(stats)

    return f"{ip_string} originates from {country.flag} {country.name}, {stat_str}."
