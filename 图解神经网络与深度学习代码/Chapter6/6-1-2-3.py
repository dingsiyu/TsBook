# -*- coding: utf-8 -*-
import tensorflow as tf
#"����TFRecordReader����"
epochs=2
reader=tf.TFRecordReader()
records_queue=tf.train.string_input_producer(['dataTest.tfrecord'],
                                              num_epochs=epochs)
_,serialized_example=reader.read(records_queue)
#"�����ļ��е�ͼ�����Ӧ�ı�ǩ"
features=tf.parse_single_example(
        serialized_example,
        features={
                'array_raw':tf.FixedLenFeature([],tf.string)
                }
                                 )
#"�������������"
array_raw=features['array_raw']
array_raw=tf.decode_raw(array_raw,tf.float32)
array=tf.reshape(array_raw,[1,2,3])
#"ÿ�δ��ļ��ж�ȡ2������"
BatchSize =2#"���ܴ����ļ������ݵĸ���"
arrays=tf.train.shuffle_batch([array],BatchSize,1000+3*BatchSize,1000)
#"�����Ự"
session=tf.Session()
session.run(tf.global_variables_initializer())
session.run(tf.local_variables_initializer())
coord=tf.train.Coordinator()
threads=tf.train.start_queue_runners(sess=session,coord=coord)
#"ѭ��2�Σ����ļ��������ȡ"
for e in range(2):
    arrs=session.run([arrays])
    print('---��%(num)d��array---'%{'num':e+1})
    print(arrs)
coord.request_stop()
coord.join(threads)
session.close()