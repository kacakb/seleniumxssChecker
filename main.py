import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def check_url(url, payload):
    driver = webdriver.Firefox()
    driver.get(url + payload)
    time.sleep(1)
    try:
        alert = driver.switch_to.alert
        print("Vulnerable: " + url + payload)
        alert.accept()
        driver.close()
    except:
        driver.close()
        pass

def main(rate, urls_file, payloads_file):
    with open(urls_file, 'r') as urls, open(payloads_file, 'r') as payloads:
        url_list = urls.readlines()
        payload_list = payloads.readlines()
        for url in url_list:
            for payload in payload_list:
                check_url(url.strip(), payload.strip())
                time.sleep(1/rate)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='XSS Checker')
    parser.add_argument('urls_file', help='File containing list of URLs to check for XSS')
    parser.add_argument('payloads_file', help='File containing list of payloads to use in XSS check')
    parser.add_argument('-r', '--rate', type=int, default=1, help='Number of requests to make per second (default: 1)')
    args = parser.parse_args()
    main(args.rate, args.urls_file, args.payloads_file)
