import json
import sys
import re

def convert(datastore):
    arr = []
    for i in range(len(datastore)):
        data = datastore[i]
        if data['speaker'] == 'user':
            arr.append(0)
        else:
            arr.append(1)
    return arr

def split(arr):
    isOne = False
    isZero = False
    cur = None
    res = [-1]
    for i in range(len(arr)):
        if cur is None:
            if arr[i]==0:
                isZero = True
                cur = 0
            else:
                isOne = True
                cur = 1
        else:
            if arr[i]==cur:
                continue
            else:
                if arr[i]==0 and isZero or arr[i]==1 and isOne:
                    res.append(i-1)
                    if arr[i]==0:
                        isZero = True
                    if arr[i]==1:
                        isOne = True
                cur = arr[i]
    res.append(len(arr)-1)
    return res

def getCorpus(datastore, res):
    corpus = []
    for i in range(1,len(res),1):
        diag={'user': None, 'system': None}
        for j in range(res[i-1]+1, res[i]+1, 1):
            if diag[datastore[j]['speaker']] is None:
                diag[datastore[j]['speaker']] = datastore[j]['utterance']['nlg']
            else:
                if datastore[j]['utterance']['nlg'] is not None:
                    diag[datastore[j]['speaker']] += ' '
                    diag[datastore[j]['speaker']] += datastore[j]['utterance']['nlg']
        corpus.append(diag)
    return corpus

def writeFile(corpus):
    From = open("From.txt","w")
    To = open("To.txt","w")
    print("writing file ...")
    for i in range(len(corpus)):
        user_input = corpus[i]['user']
        sys_input = corpus[i]['system']
        if user_input == None:
            user_input = 'emmmm'
        if sys_input == None:
            sys_input = 'emmmm'
        user_input = re.sub(r'[^\x00-\x7F]+', ' ', user_input)
        sys_input = re.sub(r'[^\x00-\x7F]+', ' ', sys_input)
        From.writelines(user_input+'\n')
        To.writelines(sys_input+'\n')
    From.close()
    To.close()
    print("finished!")

def main():
    filename = sys.argv[1]
    if filename:
        with open(filename, 'r') as f:
            datastore = json.load(f)
    arr = convert(datastore)
    res = split(arr)
    corpus = getCorpus(datastore, res)
    print(corpus)
    writeFile(corpus)

if __name__ == '__main__':
    main()

