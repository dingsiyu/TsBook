import tensorflow as tf
#"��������"
t=tf.constant([2,5,3],tf.float32)
x=tf.log(t)
#"softmax����"
s=tf.nn.softmax(x,0)
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(s))