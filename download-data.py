#!/usr/bin/python
import sys
import getpass
import requests

class Authentication:
    def __init__(self, filename=".auth"):
        self.username=""
        self.password=""
        self.gotauth=False
        self.fn = filename
        self.get_from_file()
        if not self.gotauth:
            self.get_from_input()
        if self.gotauth:
            pass
        else:
            print "Looped once but not got any auth"
            self.__init__()

    def get_from_file(self):
        try:
            if not self.gotauth:
                f=open(self.fn,"r")
                self.username,self.password=f.read().split()
                self.gotauth=True
                f.close()
        except:
            self.gotauth=False

    def get_from_input(self):
        self.username=raw_input("Username for "+self.fn+" :")
        self.password=getpass.getpass() #To mask password
        self.gotauth=True
        f=open(self.fn,"w")
        f.write(self.username+" "+self.password)
        f.close()

proxy_auth = Authentication(".proxyauth")
kaggle_auth = Authentication(".kaggleauth")

proxies= {
    "http": "http://"+proxy_auth.username+":"+proxy_auth.password+"@netmon.iitb.ac.in:80/",
}

# The direct link to the Kaggle data set
data_url = 'https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/download/Train.zip'
if (len(sys.argv) > 1):
    data_url = sys.argv[1];
print data_url

# The local path where the data set is saved.
local_filename = "Train.zip"
if (len(sys.argv) > 2):
    local_filename = sys.argv[2];

# Kaggle Username and Password
kaggle_info = {'UserName': kaggle_auth.username, 'Password': kaggle_auth.password}

# Attempts to download the CSV file. Gets rejected because we are not logged in.
r = requests.get(data_url, proxies=proxies)

# Login to Kaggle and retrieve the data.
r = requests.post(r.url, data = kaggle_info, prefetch = False)

# Writes the data to a local file one chunk at a time.
f = open(local_filename, 'w')
for chunk in r.iter_content(chunk_size = 512 * 1024): # Reads 512KB at a time into memory
    if chunk: # filter out keep-alive new chunks
        f.write(chunk)
f.close()
