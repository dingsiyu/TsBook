# -*- coding: utf-8 -*-
import os
import tensorflow as tf
import matplotlib.pyplot as plt
H,W=28,28
#"�õ��ļ���./data/�µ�����tfRecord�ļ�"
files=tf.train.match_filenames_once(os.path.curdir+
                                       "/data/"+
                                       "data*.tfrecord")
#"����TFRecordReader����"
reader=tf.TFRecordReader()
records_queue=tf.train.string_input_producer(files,num_epochs=2)
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
#"ת����ͼƬ"
img=tf.reshape(img_raw,[H,W])
#"��ǩ"
label=features['label']
label=tf.cast(label,tf.int64)
#"ÿ�δ��ļ��ж�ȡ3��ͼƬ"
BatchSize =3
img,label=tf.train.shuffle_batch([img,label],
            BatchSize,1000+3*BatchSize,1000)
session=tf.Session()
session.run(tf.global_variables_initializer())
session.run(tf.local_variables_initializer())
coord=tf.train.Coordinator()
threads=tf.train.start_queue_runners(sess=session,coord=coord)
print(session.run(files))
#"ѭ��2�ν����ļ����е�����"
for i in range(2):
    print('---��%(num)d��ͼ��---'%{'num':i+1})
    imgs,labels = session.run([img,label])
    for j in range(BatchSize):
        print('-��%(num)d��ͼ���еĵ�%(index)d��:��ǩΪ%(l)d-'
                 %{'num':i+1,'index':j+1,'l':labels[j]})
        plt.imshow(imgs[j,:,:])
        plt.show()
coord.request_stop()
coord.join(threads)
session.close()