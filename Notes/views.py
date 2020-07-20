import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index_json(request):
    print(request.user)
    queryset=[
        {"user":str(request.user),
         "笔记":{
             1:{"name":"追彭茵茵",
              "content":"尽快找到好工作,然后去追回她",
              "time":"24岁前",
              "is_done":False},
             2:{"name": "娶彭茵茵,陪她后半辈子",
              "content": "建立在追到她的前提下",
              "time": "她结婚之前",
              "is_done":False}
         }
         }
    ]
    return JsonResponse(queryset,safe=False)


def index(request):
    js_data=index_json(request)
    print(js_data.content)
    return render(request,"note/index.html",context={"json_data":js_data.content})