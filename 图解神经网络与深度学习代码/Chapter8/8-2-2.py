# -*- coding: utf-8 -*-
import tensorflow as tf
#" �������� 5x5 "
I=tf.constant(
        [
        [
        [[2],[9],[11],[4],[8]],
        [[6],[12],[20],[16],[5]],
        [[1],[32],[13],[14],[10]],
        [[11],[20],[27],[40],[17]],
        [[9],[8],[11],[4],[1]]
        ]
        ],tf.float32
        )
# "����� 3x3"
Kernel=tf.constant(
        [
        [[[4]],[[8]],[[12]]],
        [[[5]],[[10]],[[15]]],
        [[[6]],[[12]],[[18]]]
        ],tf.float32
        )
#" �����Ự"
session=tf.Session()
# "��������������ֱ�Ӿ��"
result=tf.nn.conv2d(I,Kernel,[1,1,1,1],'SAME')
print('ֱ�Ӿ���Ľ��')
print(session.run(result))
#"����˿��Է���Ϊ 3x1�Ĵ�ֱ����� �� 1x3 ˮƽ�����"
kernel1=tf.constant(
        [
        [[[4]]],
        [[[5]]],
        [[[6]]]
        ],tf.float32
        )
kernel2=tf.constant(
        [
        [[[3]],[[2]],[[1]]]
        ],tf.float32
        )
#"��kernel2��ת180��"
rotate180_kernel2=tf.reverse(kernel2,axis=[1])
#"�������������ľ���˵ľ��"
result1=tf.nn.conv2d(I,kernel1,[1,1,1,1],'SAME')
result12=tf.nn.conv2d(result1,rotate180_kernel2,[1,1,1,1],'SAME')
print('���þ���˵ķ����Եľ�����')
print(session.run(result12))