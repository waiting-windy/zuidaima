import requests
import re
from bs4 import BeautifulSoup

url='http://wufazhuce.com/'#每一期的链接共同的部分
def getInstance():
    try:
        res=requests.get(url)
        res.raise_for_status()
    except requests.RequestException as e:#处理异常
        print(e)
    else:
        html=res.text#页面内容
        soup = BeautifulSoup(html,'html.parser')
        bs = soup.find('div',class_='fp-one-cita')
        index = bs.a['href'].rsplit('/',1)[1]
        
        s=str(index)#数字类型转为字符串类型
        currenturl=url+'one/'+s#当前期的链接
        try:
            res=requests.get(currenturl)
            res.raise_for_status()
        except requests.RequestException as e:#处理异常
            print(e)
        else:
            html=res.text   #页面内容
            soup = BeautifulSoup(html,'html.parser')
            b=soup.select('.one-cita')#查找“每日一句”所在的标签
            print(b[0].text.strip())
        return b[0].text
        
    
        

if __name__=="__main__":
    getInstance()