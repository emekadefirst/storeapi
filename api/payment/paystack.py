import os
import requests
from dotenv import load_dotenv

load_dotenv()

sk = os.environ.get('PAYSTACK')

class Paystack:
    def __init__(self, email, amount, secret_key):
        self.email = email
        self.amount = amount
        self.secret_key = sk

    def pay(self):
        url = "/transaction/initialize"
        data = {
            "email": self.email,
            "amount": self.amount * 100
        }
        headers = {
            "Authorization": "Bearer " + self.secret_key,
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            data = response.json()
            ref = data['data']['reference']
            auth_link = data['data']['authorization_url']
            result = {
                'reference_id': ref,
                'auth_url': auth_link
                }
            return result
        return "404"
        

import requests

class Verify:
    def __init__(self, reference, secret_key):
        self.reference = reference
        self.secret_key = secret_key
        
    def status(self):
        url = f"https://api.paystack.co/transaction/verify/{self.reference}"
        headers = {
            "Authorization": "Bearer " + self.secret_key
        }
        timeout_counter = 0
        max_timeout = 20  # Maximum number of retries
        while timeout_counter < max_timeout:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                gateway_response = data.get('data', {}).get('gateway_response')
                if gateway_response == "Successful":
                    return "successful"
                elif gateway_response == "The transaction was not completed":
                    return "pending"
                else:
                    return "failed"
            else:
                # Retry if the status code is not 200
                timeout_counter += 1
        return "timeout"
