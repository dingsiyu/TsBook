# -*- coding: utf-8 -*-
import tensorflow as tf
#"������ֵ"
logits=tf.constant([[ -8.286214,0.64386976,9.21543,-0.07865417,5.6011457,
                     6.145635,-10.207598,7.5121603,7.7261553,9.431863]],
                     tf.float32)
#"�˹�����ı�ǩ"
labels=tf.constant([[1,0,0,0,0,0,0,0,0,0]],tf.float32)
#"sigmod������"
entroy=tf.nn.sigmoid_cross_entropy_with_logits(logits=logits,labels=labels)
#"��ʧֵ"
loss=tf.reduce_sum(entroy)
#"��ӡ��ʧֵ"
session=tf.Session()
print(session.run(loss))