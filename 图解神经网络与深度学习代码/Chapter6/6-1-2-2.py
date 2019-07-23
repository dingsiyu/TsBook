# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"�����ļ�"
record=tf.python_io.TFRecordWriter('dataTest.tfrecord')
#"��1��2���3����άndarray"
array1=np.array(
        [
        [[1,2,3],[4,5,6]],
        ],np.float32
        )
#"��1��2���3����άndarray"
array2=np.array(
        [
        [[11,12,13],[14,15,16]],
        ],np.float32
        )
#"��1��2���3����άndarray"
array3=np.array(
        [
        [[21,23,21],[23,24,22]],
        ],np.float32
        )
#"��������3��ndarray����һ���б�"
arrays=[array1,array2,array3]
#"ѭ�����������б��е�ÿһ��ndarray"
for array in arrays:
    #"��ndarray�е�ֵתΪΪ�ֽ�����"
    array_raw=array.tostring()
    #"ndarray��ֵ"
    feature={
         'array_raw':
             tf.train.Feature(bytes_list=tf.train.
                   BytesList(value=[array_raw])),
         }
    features=tf.train.Features(feature=feature)
    example=tf.train.Example(features=features)
    #"�ַ������л���д���ļ�"
    record.write(example.SerializeToString())
record.close()