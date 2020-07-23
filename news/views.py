from django.shortcuts import render, redirect
import datetime
import random
from django.views import View
from django.http import Http404, HttpResponse
import json

json_news1 = {'news': [
    {
        "created": datetime.datetime(2020, 2, 22, 16, 40, 00),
        "text": "A new star appeared in the sky.",
        "title": "The birth of the star",
        "link": 9234732
    },
    {
        "created": datetime.datetime(2020, 3, 25, 17, 10, 50),
        "text": "A good win for red devil's.",
        "title": "Another Victory",
        "link": 9234799
    },
    {
        "created": datetime.datetime(2020, 1, 5, 7, 18, 20),
        "text": "Sancho agrees with united offer",
        "title": "Best football player in England",
        "link": 9234592
    }

]
}


class StarterView(View):
    def get(self, *args, **kwargs):
        # save_json(json_news1)
        return redirect('/news/')


def load_json(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)


def save_json(path, file):
    with open(path, 'w') as jason_paht:
        json.dump(file, jason_paht)



class ViewsNewsLink(View):
    def get(self, request, link_number, *args, **kwrgs):
        json_news = load_json('C:\h-project\Hypernews_portal\\news.json')
        return render(request, 'news/news.html', {'json_news': json_news, 'link_number': link_number})


def myFunc(e):
    return e['created']


class AdressView(View):
    def get(self, request, *args, **kwargs):
        json_news = load_json('C:\h-project\Hypernews_portal\\news.json')
        for i in json_news:
            i["created"] = i["created"].split()[0]
        json_news.sort(reverse=True, key=myFunc)
        search_word = request.GET.get('q')
        if search_word:
            search_list = list()
            for j in json_news:
                if search_word.lower() in j['title'].lower().split():
                    search_list.append(j)
            return render(request, 'news/index.html', {'json_news': search_list})
        return render(request, 'news/address.html', {'json_news': json_news})


class CreateVew(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/create.html', {})

    def post(self, request, *args, **kwargs):
        create_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        random.seed(create_time)
        link_news = random.randint(1,99999)
        title_news = request.POST.get("title")
        text_news = request.POST.get("text")
        news_dict = {"created": create_time, "text": text_news, "title": title_news, "link": link_news}
        json_news = load_json('C:\h-project\Hypernews_portal\\news.json')
        json_news.append(news_dict)
        save_json('C:\h-project\Hypernews_portal\\news.json', json_news)
        return redirect("/news/")



