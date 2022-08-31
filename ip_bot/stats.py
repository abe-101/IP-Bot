import inflect

p = inflect.engine()


def pretty_stats(stats):
    sorted_stats = dict(sorted(stats.items(), key=lambda item: item[1], reverse=True))
    sorted_stats = {key: value for key, value in sorted_stats.items() if value != 0}

    stat_list = []
    first_item = True
    for k, v in sorted_stats.items():
        if first_item:
            stat_list.append(f"{v} reports have found it {k}")
            first_item = False
        else:
            stat_list.append(f"{v} {k}")

    return p.join((stat_list))
