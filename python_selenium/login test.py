import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#打开浏览器
def openBrowser():
	webdriver_handle = webdriver.Chrome()
	return webdriver_handle

#打开网址
def openUrl(handle,url):
	handle.get(url)
	handle.maximize_window

def findElement(handle,arg):
	ele_name = handle.find_element_by_id(arg['userid'])
	ele_pwd = handle.find_element_by_id(arg['pwdid'])
	ele_logbtn = handle.find_element_by_id(arg['logbtnid'])
	return ele_name,ele_pwd,ele_logbtn

def sendVals(eletuple,arg):
	listkey = ['uname','pwd']
	i = 0
	for key in listkey:
		eletuple[i].send_keys('')
		eletuple[i].clear()
		eletuple[i].send_keys(arg[key])
		i+=1
	print (eletuple[2].text)
	eletuple[2].click()

def checkResult(handle):
	try:
		alert = handle.switch_to_alert()
		alert.accept()
		print('Accont or pwd error!')
	except:
		print('login success!')
	
def login_test(ele_dict,user_list):
	d = openBrowser()
	openUrl(d,ele_dict['url'])
	time.sleep(5)

	ele_tuple = findElement(d,ele_dict)
	for arg in user_list:
		sendVals(ele_tuple,arg)
		checkResult(d)
		time.sleep(5)

if __name__ == '__main__':

	url = 'http://baihu.680000cun.com/'
	accont = 'sgw'
	pwd = '1234567'
	ele_dict = {'url':url,'userid':'UsernameOrPhoneNumber','pwdid':'Password','logbtnid':'submit_button','uname':accont,'pwd':pwd}
	user_list = [{'uname':accont,'pwd':pwd}]
	login_test(ele_dict,user_list)