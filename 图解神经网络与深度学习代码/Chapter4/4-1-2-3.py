# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.python import pywrap_tensorflow
#ckpt=tf.train.get_checkpoint_state('./')
#"��ȡ�ڵ�ǰ�ļ�����(./)��ckpt�ļ����������ckpt�����λ������"
ckpt=tf.train.latest_checkpoint('./')
#"��ӡ��ȡ��ckpt�ļ�"
print('��ȡ��ckpt�ļ�:'+ckpt)
#"����NewCheckpointReader��,��ȡckpt�ļ��еı������Ƽ����Ӧ��ֵ"
reader=pywrap_tensorflow.NewCheckpointReader(ckpt)
var_to_shape_map=reader.get_variable_to_shape_map()
for key in var_to_shape_map:
    print('tensor_name:',key)
    print(reader.get_tensor(key))