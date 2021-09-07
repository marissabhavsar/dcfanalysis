import requests
from bs4 import BeautifulSoup
from csv import writer


def getTicker(): 
    ticker = input("Enter Ticker: ").upper()
    return ticker


#for each separate website link (3) have a function that collects necessary data and organizes it

#income statement: total revenue, net income (in drop down)
#cash flow: operating cash flow, free cash flow 

def scrape(ticker): 
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    incomeURL = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    page = requests.get(incomeURL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    cashflowURL = f'https://finance.yahoo.com/quote/{ticker}/cash-flow?p={ticker}'
    page2 = requests.get(cashflowURL, headers=headers)
    soup2 = BeautifulSoup(page2.content, 'html.parser') 
    analysisURL = f'https://finance.yahoo.com/quote/{ticker}/analysis?p={ticker}'
    page3 = requests.get(analysisURL, headers=headers)
    soup3 = BeautifulSoup(page3.content, 'html.parser') 
    statsURL = f'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'
    page4 = requests.get(statsURL, headers=headers)
    soup4 = BeautifulSoup(page4.content, 'html.parser')
    

    #revenue
    revenue = []
    table = soup.find("div", class_= 'W(100%) Whs(nw) Ovx(a) BdT Bdtc($seperatorColor)')

    for row in table.find("div", class_= "D(tbr) fi-row Bgc($hoverBgColor):h"): 
        for rev in row: 
             revenue.append(rev.get_text())

    
    #net income
    net = []
    
    for row in table.find_all("div", class_= "D(tbr) fi-row Bgc($hoverBgColor):h")[9]: 
        for num in row: 
            net.append(num.get_text())

    
    #free cash flow
    fcf = []

    table2 = soup2.find("div", class_= 'W(100%) Whs(nw) Ovx(a) BdT Bdtc($seperatorColor)')
 
    for row in table2.find_all("div", class_= "D(tbr) fi-row Bgc($hoverBgColor):h")[11]: 
        for num in row: 
            fcf.append(num.get_text())


    #operating cash flow 
    ocf = []
    for row in table2.find_all("div", class_= "D(tbr) fi-row Bgc($hoverBgColor):h")[0]: 
        for num in row: 
            ocf.append(num.get_text())
            

    ce = [] 
    for row in table2.find_all("div", class_= "D(tbr) fi-row Bgc($hoverBgColor):h")[6]: 
        for num in row: 
            ce.append(num.get_text())

    table3 = soup3.find("div", class_= 'W(100%) M(0) BdB Bdc($seperatorColor) Mb(25px)')

    predictedRev = []
    table3 = soup3.find_all("table", class_= 'W(100%) M(0) BdB Bdc($seperatorColor) Mb(25px)')[1]
    

    for row in table3.find_all("tr", class_= "BdT Bdc($seperatorColor)")[1]:
         for num in row: 
             #print(num.get_text())
             predictedRev.append(num.get_text())


    
    currentPrice = soup3.find("span", class_= "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text()  
    
    shares = soup4.find_all("td", class_= "Fw(500) Ta(end) Pstart(10px) Miw(60px)")[9].get_text()
    return revenue, net, ocf, fcf, ce, predictedRev, currentPrice, shares


