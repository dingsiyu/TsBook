# -*- coding: utf-8 -*-
import numpy as np
f=np.array([
           [10,2,8],
           [5,12,3]
           ],np.complex64)
#"��һ������ÿһ�н��и���Ҷ�任"
f_0_fft=np.fft.fft(f,axis=0)
print(f_0_fft)
#"�ڶ�������Ե�һ���õ��Ľ�����ֱ��ÿһ�н��и���Ҷ�任"
f_0_1_fft=np.fft.fft(f_0_fft,axis=1)
print(f_0_1_fft)