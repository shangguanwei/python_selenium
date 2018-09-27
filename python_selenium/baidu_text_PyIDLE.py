Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
>>> b = webdriver.Chrome()
>>> b.get('http://www.baidu.com')
>>> b.current_url
'https://www.baidu.com/'
>>> b.title
'百度一下，你就知道'
>>> ele = b.find_element_by_id('kw')
>>> id(ele)
54229392
>>> type(ele)
<class 'selenium.webdriver.remote.webelement.WebElement'>
>>> ele.send_keys('LOL')
>>> ele.clear()
>>> ele.send_keys('lol')
>>> ele.back()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ele.back()
AttributeError: 'WebElement' object has no attribute 'back'
>>> b.back
<bound method WebDriver.back of <selenium.webdriver.chrome.webdriver.WebDriver (session="94ee5ba206b67878b9854a0f13340628")>>
>>> b.back()
>>> 
