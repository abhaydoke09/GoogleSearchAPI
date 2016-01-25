__author__ = '755784'

import json
import urllib
import requests
from random import choice
from collections import defaultdict

gaurav_key = 'AIzaSyDqK4uv7W1_hTm6x0qWmmypGQFgYJ8_pWQ'
varun_key = 'AIzaSyCRKin5xw_EgHavOHRBytM62hml6NzXINs'
abhay_key = 'AIzaSyCh-qGotihDGzS-zZZk8_i8-dLo8R4Syr0'
megh_key = 'AIzaSyCbBS8BhSFBosGn5i2zNTrfTjTuVCty4nc'
tripathi_key = 'AIzaSyCYMn8vbz1SmQRmMdHX39sa35b3PdpI-Vk'
megh1_key = 'AIzaSyAGKrvmc0wsQcVqf43C2hIkJ6amPEjp_g4'
net1 = 'AIzaSyCgGuZie_Xo-hOECNXOTKp5Yk7deryqro8'

keys = [gaurav_key,abhay_key,megh1_key,tripathi_key,megh_key,net1]


def getQueryTerms(concept):
    queryList=[]
    queryList.append('explain '+concept+' with example')
    queryList.append('what is '+concept)
    queryList.append('How '+concept+' works')
    queryList.append(concept+' program')
    queryList.append('when to use '+concept)
    queryList.append('practical example of '+concept)
    queryList.append('Application of '+concept)
    queryList.append('theory of '+concept)
    return queryList

class dict2obj(object):
    def __init__(self, d):
        self.__dict__['d'] = d

    def __getattr__(self, key):
        value = self.__dict__['d'][key]
        if value == type({}):
            return dict2obj(value)

        return value

def get_custom_explanations(topic):
    quesryList=getQueryTerms(topic)

    urlDictionary= defaultdict(int)
    for query in quesryList:
        for start in range(1,42,10):
            search_term = urllib.quote_plus(query)
            cx = '001717158467697548207:dsvqgtk2tak'
            api_url = "https://www.googleapis.com/customsearch/v1?" \
                  "key="+choice(keys)+"&cx="+cx+"&fields=items&" \
                  "q="+search_term+'&start='+str(start)
            print api_url
            #response = requests.get(api_url).json()
            #results = json.load(response)
            results = requests.get(api_url).json()
            for link in results['items']:
                urlDictionary[link['link']]+=1
    return urlDictionary

topic='timsort'
urlList=get_custom_explanations(topic)

fw=open('/home/abhay/timsort.csv','w')
#urlDict=eval(f)
for url,count in urlList.items():
    fw.write(url+","+str(count)+'\n')

fw.close()


