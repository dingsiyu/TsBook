# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"һά��ndarray"
array=np.array([1,2,3],np.float32)
#"ndarrayת��Ϊtensor"
t=tf.convert_to_tensor(array,tf.float32,name='t')
#"��ӡ����"
print(t)