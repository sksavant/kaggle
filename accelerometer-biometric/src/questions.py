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

ans = open("ans_2_0.csv","a")
ans.write("QuestionId,IsTrue\n")
qfile = open("../data/questions.csv")
qfile.readline()
varf = 2.0
while True:
    l = qfile.readline()
    if l=="":
        break
    qid,sid,qd = l.split(",")
    sid = int(sid)
    qd= int(qd)
    sm=seq[sid]
    dm=dev[qd]
    if (abs((sm[0]-dm[0])/math.sqrt(dm[3]))<=varf and abs((sm[1]-dm[1])/math.sqrt(dm[4]))<=varf and abs((sm[2]-dm[2])/math.sqrt(dm[5]))<=varf):
        ans.write(str(qid)+","+"1\n")
    else:
        ans.write(str(qid)+","+"0\n")
