#-*- coding: utf-8 -*-
from django.shortcuts import render
import json
import os
from django.http import JsonResponse

# Create your views here.


# /num을 넣어주면 sort+num.json 파일을 불러오도록 처리 
# json 파일을 받아서 links에 내 부모단계가 몇단계인지 내 직계 자식이 몇명인지 체크 
def todo(request):
    module_dir = os.path.dirname(__file__)  # get current directory

    file_path = os.path.join(module_dir, 'static/json/sort.json')
    file = open(file_path)
    data = json.load(file)
    nodes = data["nodes"]
    links = data["links"]

    print "nodes!"
    print nodes 


    # name = nodes[0]['name']
    # source = links[0]['source']
    # target = links[0]['target']
    
    # names = []
    sources = []
    targets = []

    # for i in xrange(0,len(nodes)):
         
    #     names.append(nodes[i]["name"]) 
    #     names.sort()


    for i in xrange(0,len(links)):
        sources.append(links[i]["source"])
        # sources = list(set(sources))
        sources.sort()
    
    # print "source" 
    # print source          

    for i in xrange(0,len(links)):
        targets.append(links[i]["target"])
        # targets = list(set(targets)) 
        targets.sort() 
         

    allIds = []
    allIds.extend(sources)
    allIds.extend(targets)
    # allIds = list(set(allIds))
    allIds.sort()

    #현재 사용되는 모든 퀴즈 id 정렬 완료
    #이제 새로운 {i: "number"} 의 리스트를 만들어야 됨 
    ids = []
    for i in xrange(0,len(allIds)):
        item = {}
        item[i] = allIds[i] 

        # "{"+i+": allIds[i]}"
        # item = "{"+i+": allIds[i]}"
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

    print "1st Data:"
    print nodes

        #노드도, 부모 노드와 일반 노드를 id 기준으로 정렬해야하는데, 이는 JSON에서 처리해야 할 것 같다.

    # for i in xrange(0,len(allIds)):
    for i in xrange(0,len(allIds)):
        #JSON 내의 값이 value위치에 있는 숫자면  변경 
        print ids[i]
        key = ids[i].keys()[0]
        print ids[i].keys()
        print ids[i][key]

        # for j in xrange(0,len(nodes)):
        #     print "nodes"
        #     print "nodes[j][referer]:",nodes[j]['referer'] 
            

        #     if nodes[j]['referer'] > len(nodes):
        #         nodes[j]['referer'] = -1 

        #     elif nodes[j]['referer'] != -10: 
        #         nodes[j]['level'] = getParentLevel(nodes,len(nodes),j,0) 

        #     else :
        #         nodes[j]['level'] = -1



    # # level소팅 
    # for i in xrange(0,len(nodes)):
    #     for j in xrange(1,len(nodes)):
    #         # 만약 node J 가 0보다 크고 J-1도 0보다 크다면, j와 j-1중에 더 작은값을 j-1로 이동 
    #         # 만약 node j 가 0보다 크고, j-1은 0보다 작다면 j-1과 j를 바꿈 
    #         # 만약 node j 가 0보다 작다면 아무것도 안함 
            
    #         if nodes[j]['level']>=1  and  nodes[j-1]['level']>=1   :
    #             if nodes[j]['level'] < nodes[j-1]['level']: 
    #                 temp = nodes[j]['level'] 
    #                 nodes[j]['level'] = nodes[j-1]['level']
    #                 nodes[j-1]['level'] = temp   
    #         elif nodes[j]['level']>=1  and  nodes[j-1]['level']<0   :
    #             temp = nodes[j]['level'] 
    #             nodes[j]['level'] = nodes[j-1]['level']
    #             nodes[j-1]['level'] = temp   
             
                    


                    
                  
                     
            
             
                
                 
        

            

    # return JsonResponse(nodes , safe=False) 
    
    # 
          

    return JsonResponse(nodes , safe=False) 


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



















































