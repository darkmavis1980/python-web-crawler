import json
from bs4 import BeautifulSoup
import requests

"""
Crawl the given URL and return the raw content, paragraphs and links
"""
def crawl(event, context):

    query_string_params = event.get('queryStringParameters')
    url = query_string_params.get('url') if query_string_params else None

    if url is None:
        return { "statusCode": 400, "body": json.dumps({"message": "Missing url parameter"})}
    
    # Try to fetch the content from the URL and catch any errors.
    try:
         
        with requests.Session() as session:
            page = session.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')

    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return {"statusCode": 400, "body": json.dumps({"error": str(e)})}

    raw_content = soup.get_text()
    paragraphs = soup.find_all('p')

    hrefs = soup.find_all('a')

    paragraphs_list = []
    for i in paragraphs:
        if (i.get_text().strip() != ''):
            paragraphs_list.append(i.get_text().strip())

    data = {
        'url': url,
        'links': [],
        'raw_content': raw_content,
        'paragraphs': paragraphs_list
    }

    for i in hrefs:
        link = i.get('href')
        text = i.get_text()
        if text.strip() != '':
            data['links'].append({
                'text': text.strip(),
                'link': link
            })

    response = {"statusCode": 200, "body": json.dumps(data)}

    return response
