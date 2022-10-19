import json
import urllib.request
import os

def lambda_handler(event, context):
    params = {
        "name": "SAMPLE_PARAMETER",
        "withDecryption": "true"
    }
    p = urllib.parse.urlencode(params)
    url = 'http://localhost:2773/systemsmanager/parameters/get/?' + p
    print(url)
    req = urllib.request.Request(url)
    req.add_header('X-Aws-Parameters-Secrets-Token', os.environ['AWS_SESSION_TOKEN'])
    with urllib.request.urlopen(req) as res:
        body = res.read()
    return {
        "statusCode": 200,
        "body": json.loads(body.decode("utf-8"))['Parameter']['Value']
    }
