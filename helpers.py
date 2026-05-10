import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def is_url_reachable(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False


def retrieve_phone_code(driver):
    """Retrieve phone confirmation code from browser logs"""
    import json
    import re

    logs = [log["message"] for log in driver.get_log('performance')
            if log.get("message") and 'api/v1/number?number' in log.get("message")]

    for log in logs:
        message = json.loads(log)["message"]
        if message["method"] == "Network.responseReceived":
            body = driver.execute_cdp_cmd('Network.getResponseBody',
                                          {'requestId': message["params"]["requestId"]})
            code = ''.join(re.findall(r'\d', body['body']))
    return code