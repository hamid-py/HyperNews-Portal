from django.db import models

# Create your models here.
import json
with open('C:\h-project\Hypernews_portal\\news.json','r') as f:
    my_file = json.load(f)
    # my_file.append({
    #     "created": '2020, 1, 5, 7, 18, 20',
    #     "text": "Sancho agrees with united offer",
    #     "title": "Best football player in England",
    #     "link": 9234592
    # })
# with open('C:\h-project\Hypernews_portal\\news.json','w') as f:
#     json.dump(my_file, f)
print(my_file)
