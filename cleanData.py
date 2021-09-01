
#will return values as floats and in lists with necessary nums
def clean(tr, ni, ocf, fcf, ce, predictTR):
    newTR = []
    newNI = []
    newOcf = []
    newFcf = []
    newCe = []
    
    for i in range(3, 7): 
        newTR.append(float(tr[i].replace(',', '')))
        newNI.append(float(ni[i].replace(',', '')))
        newOcf.append(float(ocf[i].replace(',', '')))
        newFcf.append(float(fcf[i].replace(',', '')))
        newCe.append(float(ce[i].replace(',', '')))
        
    val1 = float(predictTR[3].replace('B', ''))
    val2 = float(predictTR[4].replace('B', ''))
    newTR.insert(0, val1 * 1e8)
    newTR.insert(0, val2 * 1e8)

    return newTR, newNI, newOcf, newFcf, newCe

    
    

 
