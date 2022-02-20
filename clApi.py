def get_iamToken(token:str):
    q = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens',
        json={'yandexPassportOauthToken':token})

    iamToken=json.loads(q.content)['iamToken']
    return iamToken

def get_yaInfo(token):
    q = requests.post('https://login.yandex.ru/info?oauth_token='+token)

    return json.loads(q.content)


def get_listOrganization(iamToken):
    q = requests.get(f'https://organization-manager.api.cloud.yandex.net/organization-manager/v1/organizations',
        headers={'Authorization': 'Bearer '+iamToken})
    return json.loads(q.content)

def get_listCloud(iamToken, Organization=0):
    if Organization:
        Org=Organization
        Organization={}
        Organization['organizationId']=Org
    q = requests.get(f'https://resource-manager.api.cloud.yandex.net/resource-manager/v1/clouds',
        headers={'Authorization': 'Bearer '+iamToken}, params=Organization)
    return json.loads(q.content)

def get_listFolders(iamToken, Cloud=0):
    if Cloud:
        Cl=Cloud
        Cloud={}
        Cloud['cloudId']=Cl
    q = requests.get(f'https://resource-manager.api.cloud.yandex.net/resource-manager/v1/folders',
        headers={'Authorization': 'Bearer '+iamToken}, params=Cloud)
    return json.loads(q.content)

def get_listFunction(iamToken, Foldr):
    Folder={}
    Folder['folderId']=Foldr
    q = requests.get(f'https://serverless-functions.api.cloud.yandex.net/functions/v1/functions',
        headers={'Authorization': 'Bearer '+iamToken}, params=Folder)
    return json.loads(q.content)
