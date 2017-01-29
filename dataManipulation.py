import csv
import random
tags=[]
words=[]
wordReplaces=[\
    ["invadir","paso","peatonal"],\
    ["meterme","al","paso","peatonal"],\
    ["pase","alto"],\
    ["ignorar","luza","roja"],\
    ["dar","una","vuelta","prohibida"],\
    ["di","vuelta","prohibida"],\
    ["no","traigo","cinturon","de","seguridad"],\
    ["no","traer","cinturon","de","seguridad"],\
    ["estar","el","paso","peatonal"]\
    ]
tagReplaces=[
    ["*","a","a"],\
    ["*","*","a","a"],\
    ["*","b"],\
    ["*","b","b"],\
    ["*","*","c","c"],\
    ["*","c","c"],\
    ["*","*","d","*","d"],\
    ["*","*","d","*","d"],\
    ["*","*","a","a"]\
    ]
wordPenals=[\
    ["bajarme","del","auto"],\
    ["dar","mi","credencial"],\
    ["pagar","una","multa"],\
    ["remision","de","al","vehiculo","deposito"],\
    ["pagar","una","infraccion"],\
    ["mandar","mi","coche","al","deposito"],\
    ["salirme","del","coche"],\
    ["mandarme","al","corralon"],\
    ["llevarme","al","corralon"],\
    ["dar","mi","credencial"]\
    ]
tagPenals=[
    ["*","*","p"],\
    ["*","*","l"],\
    ["*","*","p"],\
    ["*","*","*","*","k"],\
    ["*","*","p"],\
    ["*","*","*","*","k"],\
    ["*","*","j"],\
    ["*","*","k"],\
    ["*","*","k"],\
    ["*","*","l"]\
    ]

def procesSentence(sentence,tagReplace,wordReplace,tagPenal,wordPenal):
    global tags,words
    tags=tags+['-','-']
    words=words+['-','-']
    for word in sentence[0].split(" "):
        if word =="#replace":
            words=words+wordReplace
            tags=tags+tagReplace
        elif word == "#penal":
            words=words+wordPenal
            tags=tags+tagPenal
        else:
            words.append(word)
            tags.append('*')
with open('data.csv') as csvfile:
     data = csv.reader(csvfile)
     for sentence in data:
         for index,wordReplace in enumerate(wordReplaces):
            ran=random.randint(0,8)
            procesSentence(sentence,tagReplaces[index],wordReplace,tagPenals[ran],wordPenals[ran])
     tags=tags+['-','-']
     words=words+['-','-']
     myfile = open("proces.csv", 'wb+')
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i,j in zip(tags,words):
         wr.writerow([i,j])
