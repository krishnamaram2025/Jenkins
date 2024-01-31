import requests
import json
import os




# Jenkins URL and job name
jenkins_url = os.environ['JENKINS_SERVER']
job_name = 'CSF'

# Jenkins credentials (username and API token)
USERNAM = os.environ['JENKINS_USR']
API_TOKEN = os.environ['JENKINS_TOKEN']

# Build URL with parameters
build_url = f'{jenkins_url}/job/{job_name}/buildWithParameters'

# Jenkins authentication
auth = (USERNAM, API_TOKEN)

# Build parameters
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


# params = {'param1': 'value1', 'param2': 'value2'}

# Trigger build with parameters
response = requests.post(build_url, auth=auth, params=params)

# Check the response
if response.status_code == 201:
    print(f"Build triggered successfully for job: {job_name}")
else:
    print(f"Failed to trigger build. Status code: {response.status_code}")
    print(f"Response content: {response.text}")
