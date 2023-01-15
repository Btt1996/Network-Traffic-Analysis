import requests
from bs4 import BeautifulSoup

def scan_unsecured(url):
    try:
        # send GET request to url
        response = requests.get(url)

        # parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # check for login form
        form = soup.find('form', {'method': 'post'})
        if form:
            # check for unsecured connection (http)
            if not response.url.startswith('https'):
                print("[WARNING] Unsecured connection:", response.url)

                # check for login inputs
                inputs = form.find_all('input')
                for input_tag in inputs:
                    if input_tag.get('type') == 'password':
                        print("[INFO] Login form found at:", response.url)
                        break
    except:
        pass

if __name__ == "__main__":
    # list of URLs to scan
    urls = ['http://example1.com', 'https://example2.com', 'http://example3.com']

    # scan each URL
    for url in urls:
        scan_unsecured(url)
