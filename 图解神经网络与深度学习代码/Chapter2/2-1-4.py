# -*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
#"��ȡͼƬ�ļ�"
image=tf.read_file("test.jpg",'r')
#"��ͼƬ�ļ�����ΪTensor"
image_tensor=tf.image.decode_jpeg(image)
#"ͼ����������״"
shape=tf.shape(image_tensor)
session=tf.Session()
print('ͼ�����״:')
print(session.run(shape))
#"Tensor ת��Ϊ ndarray"
image_ndarray=image_tensor.eval(session=session)
#"��ʾͼƬ"
plt.imshow(image_ndarray)
plt.show()