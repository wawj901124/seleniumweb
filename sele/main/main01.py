import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dict_MerchanInfo_Individu = {"act.cpInfo.brandName":"Mrs Lee","act.cpInfo.email":"MrsLee@iapppay.com","act.cpInfo.contactNo":"62801099876625",
                        "act.cpInfo.siup":"MrsLee_SIUP","act.cpInfo.district":"MrsLee_district","act.cpInfo.village":"MrsLee_village",
                        "act.cpInfo.postcode":"MrsLee_postcode","act.cpInfo.address":"MrsLee_address","act.cpInfo.level":"Individu",
                        "act.cpInfo.category":"GAS STATION","act.cpInfo.criteria":"Medium","province":"BALI","city":"Kab. Buleleng"}
dict_MerchanInfo_Company = {"act.cpInfo.brandName":"Mrs Lee","act.cpInfo.email":"MrsLee@iapppay.com","act.cpInfo.contactNo":"62801099876625",
                        "act.cpInfo.siup":"MrsLee_SIUP","act.cpInfo.district":"MrsLee_district","act.cpInfo.village":"MrsLee_village",
                        "act.cpInfo.postcode":"MrsLee_postcode","act.cpInfo.address":"MrsLee_address","act.cpInfo.companyName":"MrsLee_companyName",
                        "act.cpInfo.officialWebsite":"MrsLee_officialWebsite","act.cpInfo.npwp":"MrsLee_npwp","act.cpInfo.level":"Individu",
                        "act.cpInfo.category":"GAS STATION","act.cpInfo.criteria":"Medium","province":"JAWA TENGAH","city":"Kab. Brebes"}
dict_Owner_Individu = {"act.chargerInfo.name":"Mrs Lee","act.chargerInfo.typeID":"KITAS/KITAP","act.chargerInfo.nationality":"Indonesian",
                        "act.chargerInfo.idNo":"7652938","act.chargerInfo.npwp":"Mrs Lee","act.chargerInfo.addr":"MrsLee Address ok",
                        "act.chargerInfo.phone":"1542839","act.chargerInfo.email":"MrsLee@Individu.com"}
dict_Owner_Company = {"act.chargerInfo.name":"Mrs Lee","act.chargerInfo.addr":"","act.chargerInfo.phone":"628666663333","act.chargerInfo.email":"MrsLeePMian@Individu.com"}
dict_Bankaccount = {"act.bankAccountInfo.bankCode":"DANAMON","act.bankAccountInfo.accountName":"LeeCong","act.bankAccountInfo.accountNumber":"86251222"}
def logout(driver):
    #登出操作
    js = "window.scrollTo(0,0);"
    driver.execute_script(js)
    sleep(2)
    # driver.find_element(By.XPATH,"//div[@class='pullOut']/p[@class='p1 ng-binding']").click()
    # sleep(1)
    # driver.find_element(By.XPATH,"//ul/li[@class='ng-scope']").click()
    # sleep(2)
    driver.find_element(By.XPATH,"//div[@class='pullOut']/p[@class='p1 ng-binding']").click()
    sleep(1)
    driver.find_element(By.XPATH,"//a[@ng-click='logOut();']").click()
def inputAll(driver,inputlist,sleeptime=1,Bytype=By.NAME):
    for (k,v) in inputlist.items():
        element = driver.find_element(By.NAME,k)
        if element.tag_name == "input":
            element.send_keys(v)
        if element.tag_name == "select":
            Select(element).select_by_visible_text(v)
        sleep(sleeptime)



class TestAddMerchant(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        self.driver.get("https://bjw.halodigit.com:9090/nereus/agent/index")
        self.driver.maximize_window()
        #登录
        self.driver.find_element(By.CSS_SELECTOR,'#loginName').send_keys("6285558888")
        self.driver.find_element(By.CSS_SELECTOR,'#loginPwd').send_keys("a111111")
        self.driver.find_element(By.XPATH,"//*[@id=\"login-holder\"]/div[2]/form/div/div[2]/a/span").click()
        # driver.find_element(By.CSS_SELECTOR,'span').click()
        sleep(4)

    def setUp(self):
        #添加商户
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Add merchant')]").click()

    def test_demo(self):
        # try:
        #     wait = WebDriverWait(self.driver,10,0.2)
        #     wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@uploader='StoreFrontUploader']")))
        # except TimeoutException as e:
        #     print(traceback.print_exc())
        # except NoSuchElementException as e:
        #     print(traceback.print_exc())
        # except Exception as e:
        #     print(traceback.print_exc())
        # else:
        # filebox = self.driver.find_element(By.XPATH,"//input[@type='file'  and @uploader='FullFaceBustUploader']")   
        filebox = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/ui-view/div[2]/div/form/div[2]/div[2]/div[1]/p/span[1]/input")     
        filebox.send_keys('E:\\00北京爱贝\\0测试项目\\6.海外项目\\2018-05-01印尼钱包WEB后台\\图片测试\\灯塔（小）_JPG.jpg')
        sleep(4)

        # file_siup = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/ui-view/div[2]/div/form/div[2]/div[2]/div[1]/p/span[1]/input")     
        # file_siup.send_keys('E:\\00北京爱贝\\0测试项目\\6.海外项目\\2018-05-01印尼钱包WEB后台\\图片测试\\灯塔（小）_JPG.jpg')
        # file_FullfaceBust = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/ui-view/div[2]/div/form/div[4]/div[2]/div/p/span[1]/input")     
        # file_FullfaceBust.send_keys('E:\\00北京爱贝\\0测试项目\\6.海外项目\\2018-05-01印尼钱包WEB后台\\图片测试\\灯塔（小）_JPG.jpg')
        # file_LocationPhoto = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/ui-view/div[2]/div/form/div[6]/div/div[1]/p/span[1]/input")     
        # file_LocationPhoto.send_keys('E:\\00北京爱贝\\0测试项目\\6.海外项目\\2018-05-01印尼钱包WEB后台\\图片测试\\灯塔（小）_JPG.jpg')        
        # sleep(4)
        # if dict_MerchanInfo_Individu["act.cpInfo.level"] == "Individu":
        #     if len(dict_MerchanInfo_Individu) == 16:
        #         print('Merchant Individu need 13 items to input,not %s,will EXIT()!!!'%(size(dict_MerchanInfo_Individu)))
        #         quit()
        #     if len(dict_MerchanInfo_Individu) == 13:                
        #         inputAll(self.driver,dict_MerchanInfo_Individu)                     #添加商户_Merchant info区域                
        #         inputAll(self.driver,dict_Owner_Individu,1,By.NAME)                 #添加商户_Owner/Person in Charge info区域                
        #         inputAll(self.driver,dict_Bankaccount,sleeptime=1,Bytype=By.NAME)   #添加商户_Bank account区域
        # elif dict_MerchanInfo_Company["act.cpInfo.level"] == "Company":
        #     if len(dict_MerchanInfo_Company) != 16:
        #         print('Merchant Company need 16 items to input,not %s,will EXIT()!!!'%(size(dict_MerchanInfo_Company)))
        #         quit()
        #     else:
        #         inputAll(dict_MerchanInfo_Company)
        #         inputAll(dict_Owner_Company,1,By.NAME)
        #         inputAll(dict_Bankaccount,sleeptime=1,Bytype=By.NAME)

    # def test_merList(self):
    #     pass
        #商户列表
        # driver.find_element(By.XPATH,"//a[contains(text(),'Merchant list')]").click()


        
    def tearDown(self):
        #登出操作
        sleep(5)
        # logout(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()




"""
//*[@id="contentdetail"]/div[2]/ui-view/div[2]/div/form/div[1]/p[4]/span[2]


"""