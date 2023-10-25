
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from getResources import getResources


import warnings
warnings.filterwarnings("ignore")
import pandas as pd

vm_df = pd.DataFrame(columns=['Resource ID'])

query = """Resources | 
project tags.CreatedDate,tags.CreatedBy, type | where type =~ 'Microsoft.Compute/virtualMachines'" |ft
"""

token = ''
while token != None:
    if token == '':
        output = getResources(query, None)
    else:
        output = getResources(query, token)
    token = output.skip_token
    data = output.data
    print(data)
    