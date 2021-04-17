import os
import json
import requests

base_url = "https://app.orbit.love/api/v1/"

bearer_token = os.getenv('ORBIT_BEARER_TOKEN')

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer %s' % bearer_token
}

def get_workspaces(name=None):
    payload={}
    url = base_url + "workspaces"
    all_workspaces = json.loads(requests.request("GET", url, headers=headers, data=payload).text)['data']
    if(name is None):
        return all_workspaces
    else:
        for workspace in all_workspaces:
            if(workspace['attributes']['name'].lower() == name.lower()):
                return workspace
        return None

def get_workspace_id(name):
    if name == None:
        raise ValueError('Name of workspace cannot be None')

    workspace = get_workspaces(name)
    return int(workspace['id'])

def upsert_user_by_github(workspace_id, github):
    # "tags_to_add": "incididunt ullamco sint et",
    url = base_url + str(workspace_id) + "/members"

    payload = json.dumps({
    "member": {
        "teammate": False,
        "github": github
    }
    })

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.ok



