import tensorflow as tf
#"��ά����"
value2d=tf.constant(
        [
         [5,1,4,2],
         [3,9,5,7]
                ],tf.float32
        )
#"����1�����ϣ���ÿһ�е����ֵ��λ������"
result=tf.argmax(value2d,axis=1)
#result=tf.arg_max(value2d,1) �ú����Ѿ�������
session=tf.Session()
#"��ӡ���"
print(session.run(result))