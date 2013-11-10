#!/usr/bin/python
import math

dev = {}
seq = {}
dmean = open("meanvartrain.txt")
for l in dmean.readlines():
    did,xm,ym,zm,xv,yv,zv = map(float, l.split(","))
    did = int(did)
    dev[did] = (xm,ym,zm,xv,yv,zv)

smean = open("meanvartest.txt")
for l in smean.readlines():
    did,xm,ym,zm,xv,yv,zv = map(float, l.split(","))
    did = int(did)
    seq[did] = (xm,ym,zm)

ans = open("ans.txt","a")
qfile = open("../data/questions.csv")
qfile.readline()
while True:
    l = qfile.readline()
    if l=="":
        break
    qid,sid,qd = l.split(",")
    sid = int(sid)
    qd= int(qd)
    sm=seq[sid]
    dm=dev[qd]
    if (abs((sm[0]-dm[0])/math.sqrt(dm[3]))<=1.5 and abs((sm[1]-dm[1])/math.sqrt(dm[4]))<=1.5 and abs((sm[2]-dm[2])/math.sqrt(dm[5]))<=1.5):
        ans.write(str(qid)+","+"1\n")
    else:
        ans.write(str(qid)+","+"0\n")
