# -*- coding: utf-8 -*-
import os
import matplotlib.image as mp_image
import tensorflow  as tf
N = 10
for label in range(N):
    record=tf.python_io.TFRecordWriter(os.path.curdir+'/data/'+
                        'data%(label)d.tfrecord'%{'label':label})
    curDir = os.path.curdir+'/data/'+str(label)+'/'
    fileList = os.listdir(curDir)
    for name in fileList:
        #"ͼƬ��·��������"
        imagePath = curDir+name
        #"��ȡͼƬ�����ֻ�Ϊndarray"
        image=mp_image.imread(imagePath)
        #"��ndarray�����ƻ�"
        img_raw=image.tostring()
        feature={
         'img_raw':
             tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])),
         'label':
             tf.train.Feature(int64_list=tf.train.Int64List(value=[label]))
         }
        features=tf.train.Features(feature=feature)
        example=tf.train.Example(features=features)
        #"�ַ������л���д���ļ�"
        record.write(example.SerializeToString())
    #"�ر��ļ���"
    record.close()