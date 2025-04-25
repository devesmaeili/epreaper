import re
import requests
from urllib.parse import urljoin, urlparse
from jsbeautifier import beautify
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self, url: str, timeout: int = 60) -> None:
        self.url = url
        self.timeout = timeout

    async def crawl(self) -> set:
        try:
            response = requests.get(url=self.url, timeout=self.timeout)
            content_type = response.headers.get("Content-Type", "")
            if "text/html" in content_type:
                return Crawler.__parse_html(self.url, response.text)
            if "javascript" in content_type or self.url.endswith(".js"):
                return Crawler.__parse_js(response.text)
        except Exception as e:
            return e.__str__()

    @staticmethod
    def __parse_html(base_url: str, html: str) -> set:
        visited_urls = set()
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.find_all(["a", "script", "form"]):
            if href := tag.get("href") or tag.get("src") or tag.get("action"):
                full_url = urljoin(base_url, href)
                parsed = urlparse(full_url)
                if parsed.netloc == urlparse(base_url).netloc:
                    visited_urls.add(full_url.split("?")[0])
        return visited_urls

    @staticmethod
    def __parse_js(js_text: str) -> set:
        endpoint_regex = re.compile(r"""(?:"|')(\/[a-zA-Z0-9_\-\/\.]+)(?:"|')""", re.VERBOSE)
        return {match for match in endpoint_regex.findall(beautify(js_text))}
