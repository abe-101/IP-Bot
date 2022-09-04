import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../ip_bot")


from lookup import is_private_range, make_ip_info_sting, validate_ip_address  # noqa: E402


def test_is_private_range():
    assert is_private_range("192.168.1.1") is True
    assert is_private_range("23.43.12.1") is False


def test_validate_ip_address():
    assert validate_ip_address("23.43.12.1") is True
    assert validate_ip_address("this is not an ip") is False


def test_make_ip_info_sting():
    decodedResponse = {
        "data": {
            "attributes": {
                "country": "US",
                "last_analysis_stats": {
                    "harmless": 93,
                    "malicious": 0,
                    "suspicious": 0,
                    "undetected": 0,
                    "timeout": 0,
                },
            },
            "id": "23.43.12.1",
        }
    }
    formated_stat = (
        "23.43.12.1 originates from 🇺🇸 United States, 93 reports have found it harmless."
    )
    assert make_ip_info_sting(decodedResponse) == formated_stat
