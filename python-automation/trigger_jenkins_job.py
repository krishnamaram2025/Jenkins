"""
This module is to perform jenkins operation using jenkins API
"""

import requests
import os
import json
# from custom_logger.logging import CustomLogger

# logger = CustomLogger()


class JenkinsTrigger:
    def _init_(self):
        pass

    @staticmethod
    def trigger_build(url, method='GET', params=''):
        """
        Triggers a build for the specified Jenkins job.

        Parameters:
        - parameters (dict): Optional parameters for the Jenkins job.

        Returns:
        - response (requests.Response): The response object from the API call.
        """
        print("started triggering job")
        if method.upper() == 'GET':
            response = requests.get(url, auth=(os.environ['JENKINS_USR'].lower(), os.environ['JENKINS_PWD']))
        elif method.upper() == 'POST':
            response = requests.get(
                f"{JENKINS_SERVER}/crumbIssuer/api/json",
                auth=(os.environ['JENKINS_USR'].lower(), os.environ['JENKINS_PWD'])
            ).json()
            crumb = response['crumb']   
            crumb_issuer = response['crumbRequestField']                     
            headers = {
                "accept": "application/json",
                "content-type": "multipart/form-data",
                crumb_issuer: crumb
            }
            response = requests.post(
                url=url,
                auth=(os.environ['JENKINS_USR'].lower(), os.environ['JENKINS_PWD']),
                headers=headers,
                params=params
            )
            if response.status_code in [200, 201]:
                print("Job triggered successfully!")
                # Extract build number from the response headers till we have request_id changes
                build_number = response.headers['Location'].split('/')[-2]
                print(f"Build Number: {build_number}")
                return build_number
            else:
                print(f"jenkins build failed for {url}")
                print(response.text)
                raise
        else:
            print(f"Unsuporrted Method {method} for URL {url}")
            raise
        return response

if __name__ == '__main__':
    JENKINS_SERVER = os.environ['JENKINS_SERVER']
    # url = 
    # params = ""
    # JenkinsTrigger.trigger_build(url, method='POST', params=params)   
    #  print(f"Started provisioning cluster and payload {input_payload}")
    BUILD_URL = f'{JENKINS_SERVER}/job/CSF/job/buildWithParameters'
    input_payload = { 
    "cloud_provider": "aws",
    "myregion" : "us-east-1",
    "mycidr" : "10.0.0.0/16",
    "myami" : "ami-002070d43b0a4f171", 
    "mypublickey" : "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDkMw6K8asfk1eAWDse2FykRZobqtBHZ+XEKI5L4N42CqbzFVlgW8pzR60yAqzsXZLlc8zDVXpZr2fX1ft/aF6RWDod/EvTGC+9fnvZyZVdVOCje0NK6C8ABgiIY1srQtX9R0oT2OqXySbt/POGRihSGMmmCuxWMQjZCqZmS5J66Vm3D0+hihkqThDOa07izrHCLMHERo+dIKbX8hmFvlPq5j1HFGXuWzkkWJaD3+xHT8Ao56lEPrB7NNyvlnlvGH1JO8qWfEk/CuEN10v5K1wjf8W3dLu6vtEgG2BcGDm37KYoF+Y0+l9z0g5OsKAhBG7KM21nMTcEGEUd6nCQMHo3QHN2zlzq6NMy6XSK06trNaJovuuDST44iM9XAX3A+HkyiNqgNIzazVae5XtRdBAPFB/KMZkBclx8Nm8JPUXKwWIGwmmFfWxilhdC2rr1BKChIEdzGNrw6KydLItDz+DW/ajeI5JT2/x6NKj2Epz3NEsQ4a37EIWXzmY6HCrHJrs= Krishna@krish"
}

    params = {
        "CLUSTER_DATA": '"' + json.dumps(input_payload).replace('"', '\\"') + '"'
    }
    print("params", params)
    request = JenkinsTrigger.trigger_build(url= BUILD_URL, method='POST', params=params)