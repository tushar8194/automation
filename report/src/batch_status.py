import requests
import json
from common.constants import TOKEN_SERVICE, BATCH_SERVICE, PERIOD_WITHOUT_HYPHEN, FILE_NAME


def sort(lst):
    lst = [str(i) for i in lst]
    lst.sort()
    lst = [int(i) if i.isdigit() else i for i in lst]
    return lst


def getAuthToken():
    header = {'Accept' : 'application/type', 'Content-type' : 'application/json'}
    rd = requests.put(TOKEN_SERVICE, headers=header, verify=False)
    jsonToken = rd.json()
    parol = jsonToken["Bearer"]
    lp = " \"Bearer\": " + "\"" + parol + "\" "
    return lp


def getInfo():
    tokenUser = getAuthToken()
    header = {'Accept' : 'application/json', 'Content-Type' : 'application/json', 'Autherization' : '%s' % tokenUser}
    r = requests.get(BATCH_SERVICE, verify=False, headers=header, timeout=5000)
    return r.json()


def getSampleBatchAudit():
    header = {'Accept': 'text/*', 'Content-Type': 'text/*'}
    r = requests.get(BATCH_SERVICE, verify=False, headers=header)
    print(r)
    print(r.text)
    return r.text


def filterbatchAudit(rjson):
    srcBatchMap = dict()
    byqBatchMap = dict()
    byqlist = []
    for i in range(0, len(rjson)):
        list = [str(j) for j in rjson[i]["batchIds"]]
        for word in list[:]:
            if word.startswith(PERIOD_WITHOUT_HYPHEN):
                list.remove(word)
        list = sort(list)
        if len(list) !=0 and str(rjson[i]["source"]).startswith('BYQ') == False:
            srcBatchMap[rjson[i]["source"]] = list[-1]
        if str(rjson[i]["source"]).startswith('BYQ'):
            for entity in list[:]:
                entityParts = entity.split('-')
                if byqBatchMap.__contains__(entityParts[1]) and int(byqBatchMap[entityParts[1]]) < int(entityParts[0]):
                    byqBatchMap[entityParts[1]] = entityParts[0]
                else:
                    byqBatchMap[entityParts[1]] = entityParts[0]
            for item in byqBatchMap:
                byqlist.append(byqBatchMap[item] + "_" + item)
            srcBatchMap[rjson[i]["source"]] = byqlist
    return srcBatchMap


#FILTERED_BATCH = filterbatchAudit(getInfo())

print(json.dump(getSampleBatchAudit(), indent=4) + "\n")


# if FILE_NAME:
#     with open(FILE_NAME, 'a') as f:
#         print(json.dump(getSampleBatchAudit(), indent=4) + "\n")
#         #f.write(json.dump(FILTERED_BATCH,indent=4) + "\n")

