# -*- coding: utf-8 -*-
import tensorflow as tf
#"3��3��2��ȵ���ά����"
t3d=tf.constant(
        [
        [[2,5],[3,3],[8,2]],
        [[6,1],[1,2],[5,4]],
        [[7,9],[2,-3],[-1,3]]
        ],tf.float32
        )
#"��[1,0,1]λ�ô�,ȡ��2��2���1������"
t=tf.slice(t3d,[1,0,1],[2,2,1])
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(t))