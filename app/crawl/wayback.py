import requests


class WayBack:
    def __init__(self, url: str, timeout: int = 60) -> None:
        self.url = f"http://web.archive.org/cdx/search/cdx?url={url}/*&output=text&fl=original&collapse=urlkey"
        self.timeout = timeout

    async def fetch(self) -> tuple[list[str], str] | tuple[str, str] | None:
        try:
            response = requests.get(url=self.url, timeout=self.timeout)
            if response.status_code == 200:
                return [link.strip() for link in response.text.split("\n") if link], self.url
            else:
                return response.reason, self.url
        except Exception as e:
            print(f"[!] wayback error! [{e}]")
