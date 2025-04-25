import uvicorn
from datetime import datetime
from utils import FastAppConf, HTTPExceptions, APIResponse, utility
from crawl import Crawler, WayBack


app_conf = utility.config()
app = FastAppConf(
    title=app_conf.get("title"),
    version=app_conf.get("version"),
    openapi_prefix=app_conf.get("openapi_prefix"),
    openapi_url=app_conf.get("openapi_url"),
    assets_url=app_conf.get("assets_url"),
    docs_url=app_conf.get("docs_url"),
    swagger_css_url=app_conf.get("swagger_css_url"),
    swagger_js_url=app_conf.get("swagger_js_url"),
    swagger_favicon_url=app_conf.get("swagger_favicon_url"),
    origins=app_conf.get("origins"),
).setup()


@app.get("/crawl")
@HTTPExceptions()
async def crawl(url: str, timeout: int = 60, regex: str = None):
    resp = APIResponse
    timer = utility.Timer()
    crawler = Crawler(url=url, timeout=timeout)
    result: set = await crawler.crawl()
    if regex:
        result = utility.filter_response(result, regex)
    resp.status = 200
    resp.log = "GET /crawl"
    resp.detail = {
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": {"crawl_time": timer.elapsed(), "links": result},
    }
    return resp


@app.get("/wayback")
@HTTPExceptions()
async def wayback(url: str, timeout: int = 60, regex: str = None):
    resp = APIResponse
    timer = utility.Timer()
    wayback = WayBack(url=url, timeout=timeout)
    result: list = await wayback.fetch()
    if regex:
        result = utility.filter_response(result, regex)
    resp.status = 200
    resp.log = "GET /wayback"
    resp.detail = {
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": {
            "response_time": timer.elapsed(),
            "request_url": result[1],
            "links": result[0],
        },
    }
    return resp


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=app_conf.get("port"), reload=True)
