# I have created this file -- Piyush
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def Analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('Remove Punctuation','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    if fullcaps=='on':
        Analyzed=''
        for char in djtext:
            Analyzed=Analyzed + char.upper()
        param={'purpose':'changed to UpperCase','analyzed_text':Analyzed}
        djtext=Analyzed
        
    
    if removepunc=='on':    
        Analyzed=''
        Punctuation='''"!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"'''
        for ch in djtext:
            if ch not in Punctuation:
                 Analyzed+=ch
        param={'purpose':'Removed Punctuations','analyzed_text':Analyzed}
        djtext=Analyzed
        
    if  newlineremover=='on':
        Analyzed=''
        for ch in djtext:
            if ch != '\n':
                 Analyzed+=ch
        param = {'purpose':'NewLine Removed','analyzed_text':Analyzed}
        djtext=Analyzed
    if removepunc=='off' and fullcaps=='off' and newlineremover=='off':
        return HttpResponse('Please Click on the checkbox and try agains')    
    return render(request,'Analyze.html',param)    
def About(request):
    return render(request,'about_us.html')
def Contact(request):
    return render(request,'Contact.html')    
