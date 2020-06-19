from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html',{'hithere':'Type in words below'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
    introduction = 'This is a word count tool I made for stupid baobao!'
    return render(request, 'about.html', {'introduction':introduction})
