

def averageFcf(fcf, income): 
    year1 = fcf[0] / income[0]
    year2 = fcf[1] / income[1]
    year3 = fcf[2] / income[2]

    avg = (year1 + year2 + year3) / 3
    
    return avg 

#gets growth rate for rev then averages it
def revGrowthRate(tr):
    growthRate = []

    for i in range(0, len(tr)-1): 
        val = tr[i] + tr[i+1]
        val = val / tr[i+1]
        growthRate.append(val)
    
    sum = 0.0 
    
    for i in range(0, len(growthRate)): 
        sum+= growthRate[i]
        
    avgGrowthRate = sum / len(growthRate)
    return avgGrowthRate
    

#divides net income / totalRev for last 4 years
#take into account that tr starts at 2021
def incomeMargin(tr, ni):
    val = 0
    for i in range(0, len(ni)): 
        val += (ni[i] / tr[i+2])
    
    avg = val / len(ni)
    print(avg)
    return avg




def predictRev(tr, avgRev): 
    tr.insert(0, (tr[0] * (1 + avgRev)))
    tr.insert(0, (tr[0] * (1 + avgRev)))

    return tr

#takes in current ni, niMargin, and uses 2 tr
def predictNI(ni, niMargin, tr): 
    ni.insert(0, tr[3] * niMargin)
    ni.insert(0, tr[2] * niMargin)
    ni.insert(0, tr[1] * niMargin)
    ni.insert(0, tr[0] * niMargin)

    return ni

def getReqReturn(): 
    reqReturn = input("Enter Required Return %: ")

    return reqReturn

#predicted fcf and terminal value included
def predictFCF(avgfcf, ni, fcf, reqReturn): 
    fcf.insert(0, avgfcf * ni[3])
    fcf.insert(0, avgfcf * ni[2])
    fcf.insert(0, avgfcf * ni[1])
    fcf.insert(0, avgfcf * ni[0])
    fcf.insert(0, (ni[0] * 1.025) / (reqReturn - 2.5))

    return fcf


#make sure fcf has terminal val included 
def presentValFCF(reqReturn, fcf): 
    dF = [] 
    for i in range(1, 5): 
        dF.insert(0, pow(1+reqReturn, i))
    
    pv = []
    for i in range(4, -1, -1):
        pv.insert(0, fcf[i] / dF[i])

    return pv
    
def fairValue(pv, shares): 
    sum = 0
    for i in range(0, len(pv)): 
        sum+= pv[i]
    
    fairVal = sum / shares
    return fairVal 

def getMarginSafety(): 
    safety = input("Enter Margin of Safety % (decimal): ")

def targetPrice(fairValue, marginSafety): 
    targetPrice = fairValue - (fairValue * marginSafety)
    return targetPrice
    