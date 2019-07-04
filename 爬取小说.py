from time import sleep
from selenium import webdriver
chrome=webdriver.Chrome()
def paqu(url):
    chrome.get(url)
    texts=chrome.find_elements_by_xpath("//div[@class='content']/p")
    i=""
    for t in texts:
        i+=t.text+"\n\n"
    with open("爬取.txt","a",encoding="utf-8") as f:
        f.write(i)
    next_url=chrome.find_elements_by_xpath("//a[@class='nextchapter']")
    if next_url:
        next_xinurl=next_url[0].get_attribute("href")
        paqu(next_xinurl)
    else:
        chrome.close()
        return
paqu("http://book.zongheng.com/chapter/36806/1006671.html")