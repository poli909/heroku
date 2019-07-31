from django.shortcuts import render, HttpResponse
import os
import sys
import urllib.request
import json

client_id = "DHCcYGN3qRFxdpMiUg_y"
client_secret = "1_tg1zV7IE"



def search(request) :
    return render(request, 'search.html')

def result(request) :
    keyword = request.POST['keyword']
    encText = urllib.parse.quote("양림동")
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    rq = urllib.request.Request(url)
    rq.add_header("X-Naver-Client-Id",client_id)
    rq.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(rq)
    rescode = response.getcode()
    if(rescode==200): #200코드는 정상으로 입력 받았을 때
        # data = response.read().decode('utf-8')
        # result = json.loads(data) # json 타입의 형식을 Dict로 변경 
        # for post in result['items']:
        #     print(post['title'])
        #     print(post['link'])
        #     print(post['description'])
        data = response.read().decode('utf-8')
        result = json.loads(data)
        return render(request, 'result.html', {'posts' : result['items']})
    else:
        return HttpResponse('API 접근불가')
