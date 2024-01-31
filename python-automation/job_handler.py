"""
This module is to perform jenkins operation using jenkins API
"""

import requests
import os
# from custom_logger.logging import CustomLogger

# logger = CustomLogger()
JENKINS_SERVER = 'http://52.91.25.79:8080'


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
