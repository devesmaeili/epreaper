import time
import re
import yaml


class Timer:
    def __init__(self) -> None:
        self.start_time = time.time()

    def elapsed(self) -> str:
        return round(time.time() - self.start_time, 3)


def filter_response(urls, reg: str):
    result = set()
    for url in urls:
        exists = re.search(reg, url)
        if exists:
            result.add(url)
    return result


def config() -> dict:
    with open("./app.conf", "r") as conf:
        return yaml.safe_load(conf)
