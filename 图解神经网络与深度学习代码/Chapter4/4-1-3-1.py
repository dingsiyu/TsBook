# -*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
#"xyz�����ڵĵ�"
xy=tf.placeholder(tf.float32,[None,2])
z=tf.placeholder(tf.float32,[None,1])
#"��ʼ��z=w1*x+w2*y+b�е�w1��w2��b"
w=tf.Variable(tf.constant([[1],[1]],tf.float32),dtype=tf.float32)
b=tf.Variable(1.0,dtype=tf.float32)
#"��ʧ����"
loss=tf.reduce_sum(tf.square(z-(tf.matmul(xy,w)+b)))
#"�����Ự"
session=tf.Session()
session.run(tf.global_variables_initializer())
#"�ݶ��½���"
opti=tf.train.GradientDescentOptimizer(0.005).minimize(loss)
#"��¼ÿһ�ε������ƽ��ƽ�����(Mean Squared Error)"
MSE=[]
#"ѵ������"
xy_train=np.array([
                [1,1],
                [2,1],
                [3,2],
                [1,2],
                [4,5],
                [5,8]
                ],np.float32)
z_train=np.array([
                [8],
                [12],
                [10],
                [14],
                [28],
                [10]
                ],np.float32)
#"����һ��tf.train.Saver��"
saver=tf.train.Saver()
#"ѵ��ģ��,ѭ��500��"
for i in range(500):
    #"�ݶ��½�"
    session.run(opti,feed_dict={xy:xy_train,z:z_train})
    #"����ÿһ�ε�������ʧֵ����׷�ӵ��б��н��б���"
    MSE.append(session.run(loss,feed_dict={xy:xy_train,z:z_train}))
    #"ÿ��100�δ�ӡ w��b��ֵ"
    if i%100==0:
        #"����ģ��"
        saver.save(session,
                './regression/regressionModel.ckpt',global_step=i)
        print('------"��"'+str(i)+'"�εĵ���ֵ"-------')
        print(session.run([w,b]))
#"��ӡ��500�Σ����)�ĵ���ֵ"
print('------"��" '+str(500)+'"�εĵ���ֵ"-------')
print(session.run([w,b]))
saver.save(session,'./regression/regressionModel.ckpt',global_step=i)
#"������ʧ������ֵ"
plt.figure(1)
plt.plot(MSE)
plt.show()