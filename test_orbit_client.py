import orbit_client

def test_get_workspace():
    workspaces = orbit_client.get_workspaces()
    assert type(workspaces) == type([])

def test_get_specific_workspace():
    name = "MyWorkspace"
    workspace = orbit_client.get_workspaces(name)
    assert type(workspace) == type({})
    assert workspace['attributes']['name'] == name

def test_get_specific_workspace_case_insensitive():
    name = "MYWORKspace"
    workspace = orbit_client.get_workspaces(name)
    assert type(workspace) == type({})
    assert workspace['attributes']['name'].lower() == name.lower()

def test_get_specific_workspace_spaces():
    name = "Example Workspace"
    workspace = orbit_client.get_workspaces(name)
    assert type(workspace) == type({})
    assert workspace['attributes']['name'].lower() == name.lower()

def test_get_workspace_id():
    name = "Example Workspace"
    workspace_id = orbit_client.get_workspace_id(name)
    assert type(workspace_id) == type(1)

def test_upsert_okay():
    name = "Example Workspace"
    workspace_id = orbit_client.get_workspace_id(name)
    response = orbit_client.upsert_user_by_github(workspace_id, "ililic")
    assert response

def test_upsert_fail():
    name = "Example Workspace"
    workspace_id = orbit_client.get_workspace_id(name)
    response = orbit_client.upsert_user_by_github(workspace_id, "")
    assert response == False