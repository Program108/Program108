import requests
import random
import threading
#token = ""                                                                                                                                  url ="https://8ef6-2405-201-a408-7192-6d60-6f8f-c5d9-5166.in.ngrok.io/api/addStudent?token="+token
#url = "https://google.com"
adm = random.randint(1200,1800)
i = randon.randint(0,2737)
# url="https://8ef6-2405-201-a408-7192-6d60-6f8f-c5d9-5166.in.ngrok.io/api/addStudent?token="+token+"&&admNo="+str(adm)
# url="https://b77b-2401-4900-1c36-4c7d-7543-3fc6-7b6c-8cd3.in.ngrok.io/api/addStudent?token="+token+"&&admNo="+str(adm)+"&&sName="+names[i]


names = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan", "Aazaan", "Abaan", "Abbas", "Abd>

# url="https://8ef6-2405-201-a408-7192-6d60-6f8f-c5d9-5166.in.ngrok.io/api/addStudent?token="+token+"&&admNo="+str(adm)
# url="https://8ef6-2405-201-a408-7192-6d60-6f8f-c5d9-5166.in.ngrok.io/api/addStudent?token="+token+"&&admNo="+str(adm)+"&&sName="+names[i]

def s():
    for i in range(10000):
        r = requests.get(url)
        print(r.text)
                                                                                                                                             t1 = threading.Thread(target=s)
t2 = threading.Thread(target=s)
t3 = threading.Thread(target=s)
t4 = threading.Thread(target=s)
t5 = threading.Thread(target=s)
t6 = threading.Thread(target=s)
t7 = threading.Thread(target=s)
t8 = threading.Thread(target=s)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
