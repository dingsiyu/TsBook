# -*- coding: utf-8 -*-
import tensorflow as tf
#"�������� I"
I=tf.constant(
        [
        [2,3,8],
        [6,1,5],
        [7,2,-1]
        ],tf.complex64
        )
#"�����"
k=tf.constant(
        [
        [4,1],
        [2,3]
        ],tf.complex64
        )
#"�������������²���Ҳಹ0"
I_padded=tf.pad(I,[[0,1],[0,1]])
#""��ת�����180��""
k_rotate180=tf.reverse(k,[0,1])
#""�Է�ת��ľ�����²���Ҳಹ0""
k_rotate180_padded=tf.pad(k_rotate180,[[0,2],[0,2]])
#"��ά��ɢ����Ҷ�任"
I_padded_fft2=tf.fft2d(I_padded)
k_rotate180_padded_fft2=tf.fft2d(k_rotate180_padded)
#"������ά����Ҷ�任��Ӧλ�����"
xk_fft2=tf.multiply(I_padded_fft2,k_rotate180_padded_fft2)
#"��������˵Ľ�����и���Ҷ��任"
xk=tf.ifft2d(xk_fft2)
#"�����Ự"
session=tf.Session()
#"���þ����������full����Ľ��"
print(session.run(xk))