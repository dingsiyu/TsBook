# -*- coding: utf-8 -*-
import tensorflow as tf
#"��ά����"
f=tf.constant([
           [10,2,8],
           [5,12,3]
           ],tf.complex64)
#"�����Ự"
session=tf.Session()
#"f�Ķ�ά��ɢ����Ҷ�任"
F=tf.fft2d(f)
#"��ӡf�ĸ���Ҷ�任��ֵ"
print("f�Ķ�ά��ɢ����Ҷ�任:")
print(session.run(F))
#"����F�ĸ���Ҷ��任(��Ȼ�������f����ȵ�)"
F_ifft2d=tf.ifft2d(F)
#"��ӡF�ĸ���Ҷ��任��ֵ"
print("F�ĸ���Ҷ��任:")
print(session.run(F_ifft2d))