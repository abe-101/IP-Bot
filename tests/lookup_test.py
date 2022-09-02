import sys
import os
import json

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../ip_bot")


from lookup import is_private_range, validate_ip_address, make_ip_info_sting


def test_is_private_range():
    assert is_private_range("192.168.1.1") == True
    assert is_private_range("23.43.12.1") == False


def test_validate_ip_address():
    assert validate_ip_address("23.43.12.1") == True
    assert validate_ip_address("this is not an ip") == False


def test_make_ip_info_sting():
    with open("file.json") as f:
        decodedResponse = json.load(f)
    formated_stat = (
        "23.43.12.1 originates from 🇺🇸 United States, 93 reports have found it harmless."
    )
    assert make_ip_info_sting(decodedResponse) == formated_stat
