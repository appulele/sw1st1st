#-*- coding: utf-8 -*-
from django.shortcuts import render
import json
import os
from django.http import JsonResponse

def index(request): 
     
    return render(request, "index.html")  

def analy(request): 
     
    return render(request, "duedue.html")  



 
# /num을 넣어주면 sort+num.json 파일을 불러오도록 처리 
# json 파일을 받아서 links에 내 부모단계가 몇단계인지 내 직계 자식이 몇명인지 체크 
def getData(request):
    module_dir = os.path.dirname(__file__)  # get current directory

    file_path = os.path.join(module_dir, 'static/json/sort.json')
    file = open(file_path)
    data = json.load(file)
    nodes = data["nodes"]
    links = data["links"]
    sources = []
    targets = []

    for i in xrange(0,len(links)):
        sources.append(links[i]["source"])
        # sources = list(set(sources))
        sources.sort()

    for i in xrange(0,len(links)):
        targets.append(links[i]["target"])
        # targets = list(set(targets)) 
        targets.sort() 

    allIds = []
    allIds.extend(sources)
    allIds.extend(targets)
    allIds.sort()
    
    #현재 사용되는 모든 퀴즈 id 정렬 완료
    #이제 새로운 {i: "number"} 의 리스트를 만들어야 됨 
    ids = []
    for i in xrange(0,len(allIds)):
        item = {}
        item[i] = allIds[i] 
        ids.append(item)

    print "-------allIds:"
    print allIds
    for i in xrange(0,len(allIds)):
        #JSON 내의 값이 value위치에 있는 숫자면  변경 
        print ids[i]
        key = ids[i].keys()[0]
        print ids[i].keys()
        print ids[i][key]
        
        for j in xrange(0,len(links)):
            print "keys"
            print "keys-------"
            print links[j]['source']
            print links[j]['target']
            if ids[i][key] ==  links[j]['source']  :
                links[j]['source'] = key
            if ids[i][key] ==  links[j]['target']  :
                links[j]['target'] = key

        for j in xrange(0,len(nodes)):
            nodes[j]['node_num'] = j
            if ids[i][key] ==  nodes[j]['referer']  :
                nodes[j]['referer'] = key

    for i in xrange(0,len(allIds)):
        #JSON 내의 값이 value위치에 있는 숫자면  변경 
        print ids[i]
        key = ids[i].keys()[0]
        print ids[i].keys()
        print ids[i][key]

    jData = {}
    jData['nodes'] = nodes
    jData['links'] = links


    return JsonResponse(jData , safe=False) 


def getParentLevel(nodes,maxLength,index,level):
    level = level + 1
    # 가끔 parent가 다른 퀴즈인 경우같은게 있는 거같으넫, 그럼 그런 퀴즈결과는 안가져오니까 오버id인 경우 level -1로 
    if index >  maxLength:
        return level
    else:
        referer = nodes[index]['referer']
            
        print "referer:"
        print referer
        
        if referer == -1:
            return level;
        elif referer > 1:
            return getParentLevel(nodes,maxLength,referer ,level)
        else:
            # return -10
            return level
    





def data(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'static/json/con.json')
    file = open(file_path)
    data = json.load(file)
    return JsonResponse(data , safe=False) 

def fish(request):
    return render(request, "toDo/fish.html")  



















































