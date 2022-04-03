import requests, json
from rich import print
from rich.pretty import pprint
def get_iamToken(token:str):
    q = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens',
        json={'yandexPassportOauthToken':token})
    #print(json.loads(q.content))
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

def get_Cloud(iamToken, cloudId):

    q = requests.get(f'https://resource-manager.api.cloud.yandex.net/resource-manager/v1/clouds/{cloudId}',
        headers={'Authorization': 'Bearer '+iamToken})
    return json.loads(q.content)

def get_Folder(iamToken, folderId):

    q = requests.get(f'https://resource-manager.api.cloud.yandex.net/resource-manager/v1/folders/{folderId}',
        headers={'Authorization': 'Bearer '+iamToken})
    return json.loads(q.content)

def get_Func(iamToken, functionId):

    q = requests.get(f'https://serverless-functions.api.cloud.yandex.net/functions/v1/functions/{functionId}',
        headers={'Authorization': 'Bearer '+iamToken})
    return json.loads(q.content)


def get_lastFunction(iamToken, id):
    Folder={}
    Folder['functionId']=id
    Folder['tag']='$latest'
    q = requests.get(f'https://serverless-functions.api.cloud.yandex.net/functions/v1/versions:byTag',
        headers={'Authorization': 'Bearer '+iamToken}, params=Folder)
    return json.loads(q.content)

def get_verFunction(iamToken, functionVersionId):
    Folder={}
    Folder['functionVersionId']=functionVersionId
    q = requests.get(f'https://serverless-functions.api.cloud.yandex.net/functions/v1/versions/{functionVersionId}',
        headers={'Authorization': 'Bearer '+iamToken}, params=Folder)
    return json.loads(q.content)



def get_createFunction_postVer(iamToken, functionId, package):
    inf=get_lastFunction(iamToken, functionId)
    Folder={
  "functionId": inf['functionId'],
  "runtime": inf['runtime'],
  "entrypoint": inf['entrypoint'],
  "resources": inf['resources'],
  "package": package
}
    print(inf)
    print(Folder)

    jk={}
    for i in inf:
        if i != 'functionId' and  i != 'createdAt' and i != 'imageSize' and i != 'status' and i != 'logGroupId' and i != 'tags ':
            jk[i]=inf[i]
    print(jk)

    for i in Folder:
        jk[i]=Folder[i]
    print(jk)

    q = requests.post(f'https://serverless-functions.api.cloud.yandex.net/functions/v1/versions',
        headers={'Authorization': 'Bearer '+iamToken}, json=jk)
    return json.loads(q.content)
