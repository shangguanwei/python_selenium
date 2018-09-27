Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
>>> b = webdriver.Chrome()
>>> b.get('http://baihu.680000cun.com/mobile')
>>> ele_name = b.find_element_by_id('UsernameOrPhoneNumber')
>>> ele.type('sgw')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ele.type('sgw')
AttributeError: 'WebElement' object has no attribute 'type'
>>> ele_name.type(sgw)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ele_name.type(sgw)
AttributeError: 'WebElement' object has no attribute 'type'
>>> type(sgw)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    type(sgw)
NameError: name 'sgw' is not defined
>>> ele_name.send_keys('sgw')
>>> ele_pwd = b.find_element_by_id('Password')
>>> ele_pwd.sendkeys('123456')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    ele_pwd.sendkeys('123456')
AttributeError: 'WebElement' object has no attribute 'sendkeys'
>>> ele_pwd.send_keys('123456')
>>> ele_login = b.find_element_by_css_selector('button[type="submit"]')
>>> ele.id
'0.5453088933115038-1'
>>> ele_login.click()
>>> b.get('http://hzsiyan.syzmt.com')
>>> from selenium.webdriver.common.action_chains import ActionChains
>>> ele = b.find_element_by_link_text('产品中心')
>>> ActionChains(b).move_to_element(ele).perform()
>>> sub_ele = b.find_element_by_link_text('百呼')
>>> sub_ele.click()
>>> b.maximize_window()
>>> 
