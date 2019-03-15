# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/27 16:57'
import unittest

from PIL import Image   #导入Image
from PIL import ImageEnhance  #导入ImageEnhance
import pytesseract   #导入pytesseract

from project.manager.loginpage import LoginPage


class GetImageCode:
    # def __init__(self):
    #     self.loginpage  = LoginPage()  #实例化

    def getCode(self):

        caicode = '../imagefile/code1.png'
        graycode = '../imagefile/codegary1.png'

        img = Image.open(caicode)  #打开验证码
        pixtongji = []
        for x in range(img.size[1]):
            for y in range(img.size[0]):
                # 遍历图片的xy坐标像素点颜色
                pix = img.getpixel((y, x))
                pixtongji.append(pix)
                # print(pix)

        print(pixtongji)
        nonepixtongji = []
        nonepixtongjidic = {}
        for i in range(len(pixtongji)):
            if pixtongji[i] not in nonepixtongji:
                nonepixtongji.append(pixtongji[i])

        for item in pixtongji:
            if item in nonepixtongjidic.keys():
                nonepixtongjidic[item] += 1
            else:
                nonepixtongjidic[item] = 1
        print(nonepixtongjidic)
        nonepixtongjilist = sorted(nonepixtongjidic.values(),reverse=True)   #按照键值对的值对字典进行倒序排序
        numvalue = []

        numvalue.append(nonepixtongjilist[1])
        # numvalue.append(nonepixtongjilist[3])
        # numvalue.append(nonepixtongjilist[4])
        print(numvalue)
        print(nonepixtongjidic)
        print(nonepixtongjilist)
        print(type(nonepixtongjilist))
        print(numvalue)
        print(type(numvalue))
        print(nonepixtongjidic.values())


        getkey = []
        for key,value in nonepixtongjidic.items():
            for i  in range(len(numvalue)):
                if value == numvalue[i]:
                    getkey.append(key)
                # print(key)
        print(getkey)

        # 新建一张图片(大小和原图大小相同，背景颜色为255白色)
        img_new = Image.new('P', img.size, 255)
        for x in range(img.size[1]):
            for y in range(img.size[0]):
                # 遍历图片的xy坐标像素点颜色
                pix = img.getpixel((y, x))
                # print(pix)

                # 自己调色，r=0，g=0，b>0为蓝色
                for i in range(len(getkey)):
                    if (pix[0] == getkey[i][0] and pix[1] == getkey[i][1] and pix[2] == getkey[i][2]):
                        # 把遍历的结果放到新图片上，0为透明度，不透明
                        img_new.putpixel((y, x), 0)

        # print(nonepixtongji)
        img_new.save(graycode, format='png')
        imagecode = Image.open(graycode)   #打开验证码图片
        imgry = imagecode.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        sharpness = ImageEnhance.Contrast(imgry)   #对比度增强
        imagecodegary = sharpness.enhance(3.0)#3.0为图像的饱和度
        imagecodegary.save(graycode)   #保存灰度值验证码

        imagecode = Image.open(graycode)   #打开验证码图片
        imgry = imagecode.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        sharpness = ImageEnhance.Contrast(imgry)   #对比度增强
        imagecodegary = sharpness.enhance(3.0)#3.0为图像的饱和度
        imagecodegary.save(graycode)   #保存灰度值验证码

        endcode = Image.open(graycode)    #打开灰度值验证码
        codetext = pytesseract.image_to_string(endcode)
        # codetext = pytesseract.image_to_string(endcode)
        # codetext = pytesseract.image_to_string(endcode)  # 使用image_to_string识别验证码
        print("验证码：",codetext)

        # image = self.loginpage.activebase.findElementByXpath(self.loginpage.code)
        # location = image.location   #获取验证码x,y轴坐标
        # size = image.size   #获取验证码的长宽
        # coderange = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
        # # print(image)
        # print(location)
        # print(size)
        # pageScreenshotStr = self.loginpage.activebase.getScreenshot()
        # pageScreenshot = Image.open("../imagefile/%s.png"% pageScreenshotStr)   #打开截图
        # imageScreen = pageScreenshot.crop(coderange)   #使用Image的crop函数，从截图中再次截取我们需要的区域,即验证码区域
        # imageScreen.save("../imagefile/code.png")   #保存验证码图片
        # imagecode = Image.open("../imagefile/code.png")   #打开验证码图片
        # imgry = imagecode.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        # sharpness = ImageEnhance.Contrast(imgry)   #对比度增强
        # imagecodegary = sharpness.enhance(3.0)#3.0为图像的饱和度
        # imagecodegary.save("../imagefile/codegary.png")   #保存灰度值验证码

        # endcode = Image.open("../imagefile/codegary.png")   #打开灰度值验证码
        # codetext = pytesseract.image_to_string(endcode).strip()   #使用image_to_string识别验证码
        # print(codetext)





        #
        # code = self.loginpage.activebase. .findElementByXpathAndReturn (self.loginpage.)
        # print('实际结果：',code)
        # prevercodetip = "Incorrect validation code"
        # self.assertEqual(vercodetip,prevercodetip)

    def getUrlCode(self):
        self.loginpage.activebase.getUrl("https://bjw.halodigit.com:9090/nereus/manager/index#/biz/application/application/list")  # 启动web
        self.loginpage.activebase.delayTime(10)
        self.loginpage.activebase.findElementByXpathAndInput(self.loginpage.account,"1@1")
        self.loginpage.activebase.findElementByXpathAndInput(self.loginpage.password, "123456")
        self.loginpage.activebase.findElementByXpathAndClick(self.loginpage.loginbutton)
        self.loginpage.activebase.delayTime(5)
        codetext = self.loginpage.activebase.getcodetext(self.loginpage.code)
        print("验证码1：",codetext)
        self.loginpage.activebase.findElementByXpathAndClick(self.loginpage.code)
        self.loginpage.activebase.delayTime(3)
        codetext2 = self.loginpage.activebase.getcodetext(self.loginpage.code)
        print("验证码2：",codetext2)
        if codetext == codetext2:
            print("点击前后验证码相同")
        else:
            print("点击前后验证码不同")






if __name__ == "__main__":
    getcode = GetImageCode()   #实例化
    getcode.getCode()
    # getcode.getUrlCode()
