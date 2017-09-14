'''
kNN for python3
'''
import numpy as np

def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

# Python3 버전
def classify0(inX, dataSet, labels, k):
    diffMat = inX - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount, key=classCount.get, reverse=True)
    # classCount.get 이부분을 통해서 튜플이 아닌 key 값만 나온다고 한다!! 
    return sortedClassCount[0]

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = np.zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

# 수정본
#   - 파일을 한 번만 연다
#   - 즉, open(), readlines()를 한 번만 호출
def file2matrix_drop(filename):
    fr = open(filename)
    index = 0                     # 반환할 행렬의 로우 인덱스
    classLabelVec = []            # 클래스 레이블 변수 준비
    for line in fr.readlines():
        # 문자열 양 옆 공백 제거 후 탭('\t')을 기준으로 단어로 분리한 리스트
        lineList = line.strip().split('\t')
        
        # lineList의 마지막 컬럼값(레이블)을 클래스 레이블 변수에 추가
        classLabelVec.append(lineList[-1])
        
        # List Comprehension in Python
        feature = [float(value) for value in lineList[0:3]]
        
        # 처음 읽은 라인이면 returnMat 변수 초기화, 아니면 returnMat 변수에 행 추가
        # 아래 if else 문을 한 문장으로 표현
        returnMat = np.vstack((returnMat, feature)) if index != 0 else np.array(feature)
        # 메모리 측면에서는 조금 손해다.. 
        #if (index == 0):
        #    returnMat = np.array(feature)
        #else:
        #    returnMat = np.vstack((returnMat, feature))
        
        index += 1
    return returnMat, classLabelVec

def autoNorm(dataSet):
    # 각 특징별 최솟값, 최댓값, 범위를 구함
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    
    # 정규화된 배열을 구함
    normDataSet = (dataSet - minVals) / ranges
    
    # ranges와 minVals은 테스트 값에 대해 정규화할 필요가 있으므로 반환해야 함
    return normDataSet, ranges, minVals


def datingClassTest(file='datingTestSet.txt',k=3):
    hoRatio = 0.10     #hold out 10%
    datingDataMat,datingLabels = file2matrix(file)       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],
                           datingLabels[numTestVecs:m],k)
        print("the classifier came back with: %s, the real answer is: %s" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): 
            errorCount += 1.0
            print("**-----error-----**")
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))
    print(errorCount)
    
    
    
def classifyPerson():
    resultList = ['not at all','in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = np.array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print("You will probably like this person: ",\
          resultList[classifierResult - 1])