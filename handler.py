import json
from bs4 import BeautifulSoup
import requests

def crawl(event, context):
    url = event['queryStringParameters']['url']

    # # fetch the content from the url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

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

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """