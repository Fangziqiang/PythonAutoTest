#识别验证码:保存验证码所在页面截图
		driver.get_screenshot_as_file('F:\\a.png')
		#识别验证码:获取验证码图片的坐标,设置验证码截取的范围
		img_vcode = driver.find_element_by_id('validatecodeimg')
		location = img_vcode.location
		range = [int(location['x']),int(location['y']),int(location['x']+57),int(location['y']+40)]
		#识别验证码:调用自定义函数，识别并填入验证码
		vcode = dis_vcode('F:\\a.png',range,'F:\\b.png')
		driver.find_element_by_id('vadidatecode').send_keys(vcode)
		driver.find_element_by_id('imageField').click()
		wait.until(lambda ele : ele.find_element_by_id('menu_030000')).click()
		all_handles_0 = driver.window_handles