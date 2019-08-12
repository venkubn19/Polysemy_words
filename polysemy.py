import  requests
import json
from nltk.corpus import stopwords 
import os
from nltk.stem import PorterStemmer
import random


app_id = ''
app_key = ''
language = 'en'
text=input()
filt_sent=[]
stop_words=set(stopwords.words("english"))

ps = PorterStemmer()
poly=['record','bank','book','park','flat','right','race','match','face','board','sharp']
dic={ 
      "bank":["fish","river","trout"]  ,
      "park":["vehicle","car","cycle","bike"],
      "book":["flight","ticket","plane","show","movie"],
      "match":["cricket","football","tomorrow"],
      "record":["guinness","top","best"],
      "face":["pretty","sad","happy","fair","bright"],
      "sharp":["edge","knives"]
     }


#identify polysemy and removing stop words
for word in text.split():
 if ps.stem(word) in poly:
  polysemy=ps.stem(word)  
 if word.lower() not in stop_words:
  filt_sent.append(word)

print(filt_sent)

word_id = polysemy

print(word_id)
url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()
r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
t={}
t=json.dumps(r.json())
d=json.loads(t)



meanings=[]
#print("json \n" + json.dumps(r.json()))
try:
 meanings.append(d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][1]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][2]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][0]["entries"][1]["senses"][0]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][0]["entries"][1]["senses"][1]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][0]["entries"][1]["senses"][2]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][0]["entries"][2]["senses"][0]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][0]["entries"][2]["senses"][1]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][0]["entries"][2]["senses"][2]["definitions"])
except:
 print("")

try:
 meanings.append(d["results"][0]["lexicalEntries"][1]["entries"][0]["senses"][0]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][1]["entries"][0]["senses"][1]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][1]["entries"][0]["senses"][2]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][1]["entries"][1]["senses"][0]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][1]["entries"][1]["senses"][1]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][1]["entries"][1]["senses"][2]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][1]["entries"][2]["senses"][0]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][1]["entries"][2]["senses"][1]["definitions"])
except:
 print("")
try:
 meanings.append(d["results"][0]["lexicalEntries"][1]["entries"][2]["senses"][2]["definitions"])
except:
 print("")




def found(polysemy):
 if polysemy=="bank":
  flag=0
  for word in filt_sent:
   if ps.stem(word) in dic[polysemy]:
    print(d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"])
    flag=1
   else:
    continue
  if flag==0:
   print(random.choice(meanings))

 if polysemy=="book":
  flag=0
  for word in filt_sent:
   if ps.stem(word) in dic[polysemy]:
    print(d["results"][0]["lexicalEntries"][1]["entries"][0]["senses"][0]["definitions"])
    flag=1
   else:
    continue
  if flag==0:
   print(random.choice(meanings))


 if polysemy=="park":
  flag=0
  for word in filt_sent:
   if ps.stem(word) in dic[polysemy]:
    print(d["results"][0]["lexicalEntries"][1]["entries"][0]["senses"][0]["definitions"])
    flag=1
   else:
    continue
  if flag==0:
   print(random.choice(meanings))

 if polysemy=="match":
  flag=0
  for word in filt_sent:
   if ps.stem(word) in dic[polysemy]:
    print(d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"])
    flag=1
   else:
    continue
  if flag==0:
   print(random.choice(meanings))

 if polysemy=="record":
  flag=0
  for word in filt_sent:
   if ps.stem(word) in dic[polysemy]:
    print(d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][2]["definitions"])
    flag=1
   else:
    continue
  if flag==0:
   print(random.choice(meanings))


 if polysemy=="face":
  flag=0
  for word in filt_sent:
   if ps.stem(word) in dic[polysemy]:
    print(d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"])
    flag=1
   else:
    continue
  if flag==0:
   print(random.choice(meanings))


 if polysemy=="sharp":
  flag=0
  for word in filt_sent:
   if ps.stem(word) in dic[polysemy]:
    print(d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"])
    flag=1
   else:
    continue
  if flag==0:
   print(random.choice(meanings))

 if polysemy=="board":
  flag=0
  for word in filt_sent:
   if ps.stem(word) in dic[polysemy]:
    print(d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"])
    flag=1
   else:
    continue
  if flag==0:
   print(random.choice(meanings))




found(word_id)
