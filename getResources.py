import azure.mgmt.resourcegraph as arg
from azure.identity import AzureCliCredential
import pandas as pd

credential = AzureCliCredential()

all_subs = pd.read_csv('list_of_all_subscriptions.csv')
all_subs = dict(zip(all_subs['sub_id'], all_subs['sub_name']))
all_subs = list(all_subs.keys())

def getResources( strQuery, token ):
    argClient = arg.ResourceGraphClient(credential)
    argQueryOptions = arg.models.QueryRequestOptions(skip_token=token, result_format="objectArray")

    argQuery = arg.models.QueryRequest(subscriptions=all_subs, query=strQuery, options=argQueryOptions)

    argResults = argClient.resources(argQuery)

    return argResults
