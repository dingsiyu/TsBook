# -*- coding: utf-8 -*-
import tensorflow as tf
#"����Ϊ5����������"
I=tf.constant([3,4,1,5,6],tf.complex64)
#"����Ϊ4�ľ����"
K=tf.constant([1,2,-2,-1],tf.complex64)
#"��0����"
I_padded=tf.pad(I,[[0,3]])
#"������˷�ת180��"
K_rotate180=tf.reverse(K,axis=[0])
#"��ת����в�0����"
K_roate180_padded=tf.pad(K_rotate180,[[0,4]])
#"����Ҷ�任"
I_padded_fft=tf.fft(I_padded)
#"����Ҷ�任"
K_roate180_padded_fft=tf.fft(K_roate180_padded)
#"��������������Ҷ�任��˲���"
Ik_fft=tf.multiply(I_padded_fft,K_roate180_padded_fft)
#"����Ҷ��任"
Ik=tf.ifft(Ik_fft)
#"��Ϊ����������;���˶���ʵ���������ϸ���Ҷ��任����ȡʵ���Ĳ���"
Ik_real=tf.real(Ik)
session=tf.Session()
#"��ӡ���"
print(session.run(Ik_real))