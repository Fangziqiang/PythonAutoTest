#coding=utf-8
import os

# os.path.getmtime()
# getmtime()���� �ļ��б��������ļ���ʱ�䣨�����ļ���ʱ������������ǻ�õ�һ�����ʱ�䣩
# ����жϵ�Ŀ¼���滹������Ŀ¼�ļ���������Ҫ���и����ӵ��жϣ�
lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn)
           if not os.path.isdir(result_dir+"\\"+fn) else 0)
# if not .. ���÷��պ��� fi �෴�� ��ʾ�������������Ϊ�棬��ִ�� if �������䡣��
# os.path.isdir():isdir()�����ж�ĳһ·���Ƿ�ΪĿ¼��