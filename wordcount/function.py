#coding=utf-8
_date_ = '2019/3/12 10:50'

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def count(request):
    text=request.GET['text']
    total_count = len(text)
    d={}
    for word in text:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    d=sorted(d.items(),key=lambda w:w[1],reverse=False)
    return render(request,'count.html',{'count':total_count,'text':text,'wordcount':d})


def about(request):
    return render(request,'about.html')