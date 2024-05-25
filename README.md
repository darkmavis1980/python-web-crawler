# Python Web Crawler

This is a simple web crawler. It is a Python script that crawls any given urls.

## Requirements

- Python 3.10 or higher
- Serverless Framework 3.x

## Installation

1. Clone the repository
2. Create a virtual environment and activate it

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

3. Install the dependencies

  ```bash
  pip install -r requirements.txt
  ```

4. Install the Node.js dependencies

  ```bash
  npm install
  ```

## Usage

Run it offline by using the following command:

```bash
npm run offline
```

## Endpoints

```bash
GET /crawl?url=<url>
```
