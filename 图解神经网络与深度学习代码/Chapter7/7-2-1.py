# -*- coding: utf-8 -*-
import tensorflow as tf
#"���볤��Ϊ3��һά����"
f=tf.constant([4,5,6],tf.complex64)
#"�����Ự"
session=tf.Session()
#"һά����Ҷ�任"
F=tf.fft(f)
#"��ӡ����Ҷ�任F��ֵ"
print("����Ҷ�任F��ֵ:")
print(session.run(F))
#"����F�ĸ���Ҷ��任(��Ȼ�������f����ȵ�)"
F_ifft=tf.ifft(F)
#"��ӡF����Ҷ��任��ֵ"
print("��ӡF�ĸ���Ҷ��任��ֵ:")
print(session.run(F_ifft))