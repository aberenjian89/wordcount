from django.shortcuts import render
from operator import itemgetter


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext'].replace(',', '').replace('.', '').split(' ')
    dic = {}
    for word in fulltext:
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1
    dic = sorted(dic.items(), key = itemgetter(1), reverse = True)
    return render(request, 'count.html', {'dictionary': dic, 'wordscount': len(dic), 'fulltext': request.GET['fulltext']})


def aboutpage(request):
    return render(request, 'about.html')
