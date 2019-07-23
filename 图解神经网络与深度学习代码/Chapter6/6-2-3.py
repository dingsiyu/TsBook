# -*- coding: utf-8 -*-
import tensorflow as tf
#"����ȫ��������"
def net(tensor):
    #""����㡢�����㡢��������Ԫ����""
    I,H1,O=784,200,10
    #"��1���Ȩ�ؾ����ƫ��"
    w1=tf.random_normal([I,H1],0,1,tf.float32)
    b1=tf.random_normal([H1],0,1,tf.float32)
    #"������Ľ�������� sigmoid �����"
    l1=tf.matmul(tensor,w1)+b1
    sigma1=tf.nn.sigmoid(l1)
    #"��2���Ȩ�ؾ����ƫ��"
    w2=tf.random_normal([H1,O],0,1,tf.float32)
    b2=tf.random_normal([O],0,1,tf.float32)
    #"�����Ľ��"
    l2=tf.matmul(sigma1,w2)+b2
    return l2
#"��ȡͼƬ�ļ�"
image=tf.read_file("0.jpg",'r')
#"��ͼƬ�ļ�����ΪTensor"
image_tensor=tf.image.decode_jpeg(image)
#"ͼ����������״"
length=tf.size(image_tensor)#length=28*28
#"�ı���״������Ϊһ��һά���������д洢"
t=tf.reshape(image_tensor,[1,length])
#"��������ת����ת��Ϊfloat32����"
t=tf.cast(t,tf.float32)
#"��׼������"
t=t/255.0
#"�������붨���2��ȫ��������"
output=net(t)
session=tf.Session()
#��ӡ�����
print(session.run(output))