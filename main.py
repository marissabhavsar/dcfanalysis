from bs4 import BeautifulSoup
from collectData import *
from cleanData import *
from calculations import *

def main():
    ticker = getTicker()
    scrape(ticker)
    

    totalRevenue = scrape(ticker)[0]
    netIncome = scrape(ticker)[1]
    ocf = scrape(ticker)[2]
    fcf = scrape(ticker)[3]
    ce = scrape(ticker)[4]
    predictTR = scrape(ticker)[5]
    
    currentPrice = scrape(ticker)[6]
    shares = scrape(ticker)[7]

    totalRevenue = clean(totalRevenue, netIncome, ocf, fcf, ce, predictTR)[0]
    netIncome = clean(totalRevenue, netIncome, ocf, fcf, ce, predictTR)[1]
    ocf = clean(totalRevenue, netIncome, ocf, fcf, ce, predictTR)[2]
    fcf = clean(totalRevenue, netIncome, ocf, fcf, ce, predictTR)[3]
    ce = clean(totalRevenue, netIncome, ocf, fcf, ce, predictTR)[4]

    fcfByincome = averageFcf(fcf, netIncome)
    revGrowth = revGrowthRate(totalRevenue)
    avgNiMargin = incomeMargin(totalRevenue, netIncome)
    totalRevenue = predictRev(totalRevenue)
    netIncome = predictNI(netIncome, avgNiMargin, totalRevenue)

    reqReturn = getReqReturn()

    fcf = predictFCF(fcfByincome, netIncome, fcf, reqReturn)
    presentVal = presentValFCF(reqReturn, fcf)
    
    fairVal = fairValue(presentVal, shares)
    marginSafety = getMarginSafety()

    target = targetPrice(fairVal, marginSafety)
    
    print("The Current Price of ", ticker, " is ", currentPrice)
    print("The Fair Value of ", ticker, " is: ", fairVal)
    print("The Target Price of ", ticker, " is ", target)



    
    
        


    

    




main()