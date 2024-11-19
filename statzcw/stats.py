
from typing import List
import math

def zcount(data: List[float]) -> float :
    return len(data)

def zmean(data: List[float]) -> float :
    return sum(data)/len(List)

def zmode(data: List[float]) -> float :
    items = {}
    for i in data:
        if i not in items:
            items[i] = data.count(i)

    max_value = max(items.values())
    return data.get(max_value)


def zmedian(data: List[float]) -> float :
    index_value = int((len(data)-1)/2)
    return data[index_value]

def zvariance(data: List[float]) -> float :
    data_mean = sum(data) / len(data)

    deviations = []
    for i in data:
        deviations.append(abs(data_mean - i)**2)
        
    return sum(deviations)/ (len(data)-1)
	
def zstddev(data: List[float]) -> float :
    # sqrt of variance
    return math.sqrt(zvariance(data))

def zstderr(data: List[float]) -> float :
    return zstddev(data) / math.sqrt(len(data))

def cov(a, b):
    pass

def zcorr(datax: List[float], datay: List[float]) -> float :
    pass


def readDataFile(file):
    x,y = [], []
    with open(file) as f:
        first_line = f.readline() # consume headers
        for l in f:
            row = l.split(',')
            #print(row, type(row))
            x.append(float(row[0]))
            y.append(float(row[1]))

    return (x,y) #we have two lists containing values

def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data

