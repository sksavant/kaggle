#!/usr/bin/python

trainfile = open("../data/train.csv","r")
#trainfile = open("../data/test.csv","r")
trainfile.readline()
#meanfile = open("meanvartest.txt","a")
meanfile = open("meanvartrain.txt","a")
devicemeanvar = {}
#(meanx,meany,meanz, varx, vary, varz,n)
l =trainfile.readline()
t,x,y,z,dev = map(float,l.split(","))
dev = int(dev)
cur_dev = dev
xyz = [[x],[y],[z]]
while True:
    l = trainfile.readline()
    if l=="":
        mean = (sum(xyz[0])/len(xyz[0]),sum(xyz[1])/len(xyz[1]),sum(xyz[2])/len(xyz[2]))
        var = []
        for i in range(3):
            vsum = 0
            for xval in xyz[0]:
                vsum = vsum+ (xval-mean[i])**2
            var.append(vsum/len(xyz[0]))
        devicemeanvar[cur_dev]  = (mean[0],mean[1],mean[2],var[0],var[1],var[2]) 
        print devicemeanvar[cur_dev]
        pr = str(devicemeanvar[cur_dev])
        pr = pr[1:len(pr)-1]
        meanfile.write(str(cur_dev)+", "+pr+"\n")
        break
    t,x,y,z,dev = map(float,l.split(","))
    dev = int(dev)
    if dev==cur_dev:
        xyz[0].append(x)
        xyz[1].append(y)
        xyz[2].append(z)
    else:
        mean = (sum(xyz[0])/len(xyz[0]),sum(xyz[1])/len(xyz[1]),sum(xyz[2])/len(xyz[2]))
        var = []
        for i in range(3):
            vsum = 0
            for xval in xyz[0]:
                vsum = vsum+ (xval-mean[i])**2
            var.append(vsum/len(xyz[0]))
        devicemeanvar[cur_dev]  = (mean[0],mean[1],mean[2],var[0],var[1],var[2]) 
        print devicemeanvar[cur_dev]
        pr = str(devicemeanvar[cur_dev])
        pr = pr[1:len(pr)-1]
        meanfile.write(str(cur_dev)+", "+pr+"\n")
        cur_dev = dev
        xyz = [[x],[y],[z]]
    '''
    try:
        v = devicemeanvar[dev]
        devicemeanvar[dev] = ((v[0]*n+x)/(n+1),(v[1]*n+x)/(n+1),(v[2]*n+x)/(n+1),
    except KeyError:
    '''
meanfile.close()
trainfile.close()
