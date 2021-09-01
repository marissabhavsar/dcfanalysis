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
    
    
    print(clean(totalRevenue, netIncome, ocf, fcf, ce, predictTR))
    
    totalRevenue = clean(totalRevenue, netIncome, ocf, fcf, ce, predictTR)[0]
    netIncome = clean(totalRevenue, netIncome, ocf, fcf, ce, predictTR)[1]
    ocf = clean(totalRevenue, netIncome, ocf, fcf, ce, predictTR)[2]
    fcf = clean(totalRevenue, netIncome, ocf, fcf, ce, predictTR)[3]
    ce = clean(totalRevenue, netIncome, ocf, fcf, ce, predictTR)[4]

    
    
        


    

    




main()