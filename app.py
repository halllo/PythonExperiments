import requests;
import json;
from types import SimpleNamespace;
import uuid;


# Get access_token
authResponse = requests.post(
    url = "https://demo.duendesoftware.com/connect/token", 
    data = { 
        'grant_type': 'client_credentials',
        'client_id': 'm2m',
        'client_secret': 'secret',
        'scopes': ''
    });

js = json.loads(authResponse.text, object_hook=lambda d: SimpleNamespace(**d));
at = js.access_token;


# Make an authorized JSON post
class Upload:
  def __init__(self, name):
    self.id = str(uuid.uuid4());
    self.name = name;

class UploadEncoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__;

ups = [
    Upload("u1"),
    Upload("u2"),
    Upload("u3"),
    Upload("u4"),
    Upload("u5"),
];
upsJson = json.loads(json.dumps(ups, cls=UploadEncoder));

apiResonse = requests.post(
    url = "https://enbt01sex4vv7.x.pipedream.net",
    headers = { 'Authorization': f'Bearer {at}' },
    json = upsJson
);


# Make an authorized file upload
# requests.post(
#     url = "https://enbt01sex4vv7.x.pipedream.net",
#     headers = { 'Authorization': f'Bearer {at}' },
#     files = dict() #TODO: https://stackoverflow.com/a/12385661