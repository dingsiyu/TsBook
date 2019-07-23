# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"��ȡ tfrecord �ļ��б�����ֻ��һ�� tfrecord"
records_queue=tf.train.string_input_producer(['data.tfrecord'],num_epochs=2)
#"����һ�� TFRecordReader ����"
reader=tf.TFRecordReader()
_,serialized_example=reader.read(records_queue)
#"���� tfrecord �е�����,ÿ��ֻ����һ��"
features=tf.parse_single_example(
        serialized_example,
        features={
                'array_raw':tf.FixedLenFeature([],tf.string),
                'height':tf.FixedLenFeature([],tf.int64),
                'width':tf.FixedLenFeature([],tf.int64),
                'depth':tf.FixedLenFeature([],tf.int64)
                }
                                 )
#"��������Ӧ��ֵ"
array_raw=features['array_raw']
array = tf.decode_raw(array_raw,tf.float32)#"����"
height= features['height']
width = features['width']
depth = features['depth']
#"�����Ự"
session=tf.Session()
session.run(tf.global_variables_initializer())
session.run(tf.local_variables_initializer())
coord=tf.train.Coordinator()
threads=tf.train.start_queue_runners(sess=session,coord=coord)
#"ѭ��5�ν����ļ����е�����"
for i in range(5):
     ndarray,h,w,d=session.run([array,height,width,depth])
     print('---��%(num)d �ν�������ndarray---'%{'num':i+1})
     print(ndarray)
coord.request_stop()
coord.join(threads)
session.close()