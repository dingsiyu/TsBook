# -*- coding: utf-8 -*-
import tensorflow as tf
#"����1�� Variable ����"
v=tf.Variable(tf.constant([2,3],tf.float32))
#"�����Ự"
session=tf.Session()
#"Variable �����ʼ��"
session.run(tf.global_variables_initializer())
#"��ӡֵ"
print('v��ʼ����ֵ')
print(session.run(v))
#"���ó�Ա���� assign\_add �ı䱾���ֵ"
session.run(v.assign_add([10,20]))
print('v �ĵ�ǰֵ')
print(session.run(v))