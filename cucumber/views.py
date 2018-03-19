from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def kenta(request):
    return HttpResponse("Kenta Oke-Bode Route Description")

def count(request):
    
    return render(request,'counter.html')
    

def jump(request):
    tray= request.GET['phrase']
    wordblender =tray.split()
    worddictionary = {}
    
    for word in wordblender:
        if word in worddictionary:
            #increase
            worddictionary[word] +=1
            
        else:
            worddictionary[word]=1
            
    s= sorted(worddictionary.items(),key=operator.itemgetter(1), reverse=True)
    
    return render(request,'jumper.html', {'Words': tray, 'number':len(wordblender), 'dictionary':s})