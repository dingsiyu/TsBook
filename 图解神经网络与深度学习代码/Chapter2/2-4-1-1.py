# -*- coding: utf-8 -*-
import tensorflow as tf
#"2��3�еĶ�ά����"
value1=tf.constant(
        [
         [1,2,3],
         [4,5,6]
        ],tf.float32)
#"2��1�еĶ�ά����"
value2=tf.constant([
        [10],
        [20]
        ],tf.float32)
#"�ӷ�����"
result=tf.add(value1,value2)
#"�����Ự"
session=tf.Session()
#""��ӡ���""
print(session.run(result))