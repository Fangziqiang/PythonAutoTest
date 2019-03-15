#encoding=UTF-8
from PIL import Image
from PIL import ImageEnhance
from selenium import webdriver
from  pytesseract import image_to_string

def tag_window(sho_win,len_win):
	'''
	描述：页面有多个窗口的情况下，窗口句柄保存的列表是无序的，此函数
		  返回最近打开的窗口在窗口句柄列表中的索引，从而实现正确切换

	'''
	for i in len_win:
		if i not in sho_win:
			return len_win.index(i)

def dis_vcode(img_screen_sqve_path,range,img_vcode_save_path):
	#打开保存的含验证码的页面
	img=Image.open(img_screen_sqve_path)
	#截取验证码区域并保存
	yzm_img = img.crop(range)
	yzm_img.save(img_vcode_save_path)
	#打开验证码图片、处理、保存、识别
	yzm_img=Image.open(img_vcode_save_path)
	#图像加强，二值化
	img_bin = yzm_img.convert('L')
	#对比度增强
	sharpness =ImageEnhance.Contrast(img_bin)
	sharp_img = sharpness.enhance(5.0)
	sharp_img.save(img_vcode_save_path)
	return image_to_string(img_bin)