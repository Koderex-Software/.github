import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape_page():
    url = 'https://example.com'  # Replace with the URL you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Remove common elements like scripts and styles
    for script in soup(['script', 'style']):
        script.decompose()
    
    # Get the text of the page
    page_text = soup.get_text()
    
    return jsonify({'page_text': page_text})

if __name__ == '__main__':
    app.run()