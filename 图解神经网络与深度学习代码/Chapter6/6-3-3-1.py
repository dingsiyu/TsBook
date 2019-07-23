# -*- coding: utf-8 -*-
import tensorflow as tf
import os
#"ռλ��"
x=tf.placeholder(tf.float32,[None,28*28])
labels=tf.placeholder(tf.float32,[None,10])
#"------��һ������������------"
nums=33#"����ѵ�������ĸ���"
#"�õ��ļ���./data/�µ�����tfRecord�ļ�"
files=tf.train.match_filenames_once(os.path.curdir+
                                       "/data/"+
                                       "data*.tfrecord")
#"����TFRecordReader����"
num_epochs=1000
reader=tf.TFRecordReader()
records_queue=tf.train.string_input_producer(files,num_epochs=num_epochs)
_,serialized_example=reader.read(records_queue)
#"�����ļ��е�ͼ�����Ӧ�ı�ǩ"
features=tf.parse_single_example(
        serialized_example,
        features={
                'img_raw':tf.FixedLenFeature([],tf.string),
                'label':tf.FixedLenFeature([],tf.int64),
                }
                                 )

#"�������������"
img_raw=features['img_raw']
img_raw=tf.decode_raw(img_raw,tf.uint8)
img=tf.reshape(img_raw,[28*28])
img=tf.cast(img,tf.float32)
img=img/255.0
#"��ǩ"
label=features['label']
label=tf.cast(label,tf.int64)
label_onehot=tf.one_hot(label,10,dtype=tf.float32)
#"ÿ�δ��ļ��ж�ȡ3��ͼƬ"
BatchSize =3
imgs,labels_onehot=tf.train.shuffle_batch([img,label_onehot],
                        BatchSize,1000+3*BatchSize,1000)
#"------��2���֣�����ȫ��������------"
#""����㡢�����㡢��������Ԫ����""
I,H1,O=784,200,10
#"����㵽�������Ȩ�ؾ����ƫ��"
w1=tf.Variable(tf.random_normal([I,H1],0,1,tf.float32),
                dtype=tf.float32,name='w1')
b1=tf.Variable(tf.random_normal([H1],0,1,tf.float32),
                dtype=tf.float32,name='b1')
#"������Ľ�������� sigmoid �����"
l1=tf.matmul(x,w1)+b1
sigma1=tf.nn.sigmoid(l1)
#"��2�������㵽�����ĵ�Ȩ�ؾ����ƫ��"
w2=tf.Variable(tf.random_normal([H1,O],0,1,tf.float32),
                dtype=tf.float32,name='w2')
b2=tf.Variable(tf.random_normal([O],0,1,tf.float32),
                dtype=tf.float32,name='b2')
#"�����Ľ��"
logits=tf.matmul(sigma1,w2)+b2
#"------��3���֣�������ʧ����------"
loss=tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits_v2(
                        labels=labels_onehot,logits=logits))
#"------��4���֣��ݶ��½�------"
opti=tf.train.AdamOptimizer(0.001,0.9,0.999,1e-8).minimize(loss)
#"�����Ự"
session=tf.Session()
session.run(tf.global_variables_initializer())
session.run(tf.local_variables_initializer())
coord=tf.train.Coordinator()
threads=tf.train.start_queue_runners(sess=session,coord=coord)
for i in range(num_epochs):
    for n in range(int(nums/BatchSize)):
        imgs_arr,lables_onehot_arr=session.run([imgs,labels_onehot])
        session.run(opti,feed_dict={x:imgs_arr,labels:lables_onehot_arr})
coord.request_stop()
coord.join(threads)
session.close()