# EPReaper 🕸️

**EPReaper** (Endpoint Reaper) is a lightweight, async-powered web endpoint discovery tool that can crawl websites and extract URLs from both HTML and JavaScript content. It can also tap into the Wayback Machine to dig up historical endpoints. Built with FastAPI for speed and flexibility.

## 🚀 Features

- 🌐 Extract internal endpoints from HTML, JS, and forms
- 🕰️ Fetch historical links via Wayback Machine
- ⚡ Asynchronous and fast (thank you FastAPI)
- 🔎 Regex-based filtering support
- 🛠️ Built-in Swagger UI for testing
- 🐳 Docker & Compose support

---

## 🧠 Project Structure

```
.
├── app
│   ├── app.conf                 # Configuration file
│   ├── app.py                   # FastAPI app with endpoints
│   ├── crawl
│   │   ├── crawler.py           # Crawler class for extracting live links
│   │   ├── __init__.py
│   │   └── wayback.py           # Wayback Machine scraping logic
│   ├── Dockerfile               # Dockerfile for containerizing the app
│   ├── __init__.py
│   ├── requirements.txt         # Python dependencies
│   └── utils
│       ├── exception.py         # HTTP Exception wrapper
│       ├── fastappconf.py       # FastAPI config loader
│       ├── __init__.py
│       └── utility.py           # Timer, regex filter, config loader, etc.
├── compose.yaml                 # Docker Compose setup
├── Makefile                     # Build, run, clean shortcuts
├── README.md                    # You're reading it!
```

---

## 🧪 API Endpoints

### `/crawl`

Crawls a live site and extracts internal links.

**Query Parameters:**

- `url`: URL to crawl
- `timeout`: (optional) Request timeout (default: 60s)
- `regex`: (optional) Filter extracted links with regex

**Example:**

```
GET /crawl?url=https://example.com&regex=api
```

---

### `/wayback`

Fetches historical URLs from the Wayback Machine.

**Query Parameters:**

- `url`: Target URL
- `timeout`: (optional) Request timeout (default: 60s)
- `regex`: (optional) Regex pattern for filtering

**Example:**

```
GET /wayback?url=https://example.com&regex=\.php
```

---

## 🛠️ Run Locally

```bash
# Clone the repo
git clone https://github.com/devesmaeili/epreaper.git
cd epreaper

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r app/requirements.txt

# Run the app
cd app
uvicorn app:app --reload
```

---

## 🐳 Run with Docker

```bash
docker-compose up --build
```

---

## 📦 Makefile Goodies

```shell
# Services are built without using cache:
make init
```

```shell
# Services are built using cache:
make build
```

```shell
# Builds, (re)creates, starts, and attaches to containers for a service:
make start
```

```shell
# Stops containers and removes containers, networks,... created by up:
make stop
```

```shell
# All three commands 'make stop', 'make build' and 'make start'
make run
```

---

## ⚖️ License

MIT License

---
