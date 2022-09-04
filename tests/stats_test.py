import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../ip_bot")  # noqa: E402


from stats import pretty_stats


def test_pretty_stats():
    stat = {"harmless": 86, "malicious": 0, "suspicious": 0, "undetected": 9, "timeout": 0}
    assert pretty_stats(stat) == "86 reports have found it harmless and 9 undetected"
