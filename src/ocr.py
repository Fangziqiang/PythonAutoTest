#ʶ����֤��:������֤������ҳ���ͼ
		driver.get_screenshot_as_file('F:\\a.png')
		#ʶ����֤��:��ȡ��֤��ͼƬ������,������֤���ȡ�ķ�Χ
		img_vcode = driver.find_element_by_id('validatecodeimg')
		location = img_vcode.location
		range = [int(location['x']),int(location['y']),int(location['x']+57),int(location['y']+40)]
		#ʶ����֤��:�����Զ��庯����ʶ��������֤��
		vcode = dis_vcode('F:\\a.png',range,'F:\\b.png')
		driver.find_element_by_id('vadidatecode').send_keys(vcode)
		driver.find_element_by_id('imageField').click()
		wait.until(lambda ele : ele.find_element_by_id('menu_030000')).click()
		all_handles_0 = driver.window_handles