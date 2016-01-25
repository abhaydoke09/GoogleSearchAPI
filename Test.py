__author__ = 'abhay'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import defaultdict
import random
import time


def getQueryTerms(concept):
    queryList=[]
    #queryList.append('what is '+concept+' -pdf -ppt -wiki')
    #queryList.append('example of '+concept+' -pdf -ppt -wiki')
    #queryList.append('How '+concept+' works -pdf -ppt -wiki')
    #queryList.append(concept+' analysis -pdf -ppt -wiki')
    #queryList.append('when to use '+concept+' -pdf -ppt -wiki')
    #queryList.append(concept+' program java -pdf -ppt -wiki')
    #queryList.append(concept+' program c/c++ -pdf -ppt -wiki')
    #queryList.append(concept+' program python -pdf -ppt -wiki')
    #queryList.append('visualization of '+concept+' -pdf -ppt -wiki')
    #queryList.append('explain '+concept+' with example -ppt -pdf -wiki')
    queryList.append('explain '+concept+' with example')
    #queryList.append('what is '+concept+' -ppt -pdf -wiki')
    queryList.append('what is '+concept)
    #queryList.append('How '+concept+' works -ppt -pdf -wiki')
    queryList.append('How '+concept+' works')
    #queryList.append(concept+' program -ppt -pdf -wiki')
    queryList.append(concept+' program')
    #queryList.append('when to use '+concept+' -ppt -pdf -wiki')
    queryList.append('when to use '+concept)
    #queryList.append('practical example of '+concept+' -ppt -pdf -wiki')
    queryList.append('practical example of '+concept)
    #queryList.append('Application of '+concept+' -ppt -pdf -wiki')
    queryList.append('Application of '+concept)
    #queryList.append('theory of '+concept+' -ppt -pdf -wiki')
    queryList.append('theory of '+concept)
    #queryList.append('visualization of '+concept+' -pdf -ppt -wiki')
    #queryList.append(concept+' program java -pdf -ppt -wiki')
    #queryList.append(concept+' program c/c++ -pdf -ppt -wiki')
    #queryList.append(concept+' program python -pdf -ppt -wiki')
    return queryList

def getLinks(searchQuery):
    urlDictionary= {}
    quesryList=getQueryTerms(searchQuery)
    for queryNumber,query in enumerate(quesryList):
        driver = webdriver.Firefox()
        driver.get("http://google.co.in")
        elem=driver.find_element_by_id("lst-ib")
        elem.send_keys(query)
        elem.send_keys(Keys.RETURN)
        for i in range(10):
            driver.implicitly_wait(random.randrange(20,30))
            time.sleep(random.randrange(15,20))
            results=driver.find_elements_by_class_name("r")
            for result in results:
                link=result.find_element_by_tag_name("a").get_attribute("href")
                if link in urlDictionary:
                    urlDictionary[link][queryNumber]=1
                else:
                    urlDictionary[link]=[0 for i in range(8)]
                    urlDictionary[link][queryNumber]=1
            driver.refresh()
            try:
                driver.find_element_by_id("pnnext").click()
            except:
                print 'blocked'
                testVar = raw_input("Ask user for something.")
                driver.find_element_by_id("pnnext").click()
        driver.close()
        time.sleep(random.randrange(30,40))
    return urlDictionary



topic='quicksort'
urlDictionary=getLinks(topic)
fw=open('/home/abhay/'+topic+'.csv','w')
#fw.write('link,example,algorithm,how it works,program,when to use,practical example,application,theory,visualization,java,c/c++,python,count\n')
fw.write('link,example,algorithm,how it works,program,when to use,practical example,application,theory,count\n')
#fw.write('link,algorithm,example,how it works,analysis,when to use,java,c/c++,python,visualization,count\n')

for url in urlDictionary:
    fw.write(url)
    #print urlDictionary[url]
    for i in range(8):
        fw.write(','+str(urlDictionary[url][i]))
    #print urlDictionary[url],sum(urlDictionary[url])
    fw.write(','+str(sum(urlDictionary[url]))+'\n')
fw.close()

