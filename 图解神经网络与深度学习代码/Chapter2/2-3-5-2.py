import tensorflow as tf
#"��ά����"
value2d=tf.constant(
        [
        [5,1,4,2],
        [3,9,5,7]
                ],tf.float32
        )
#"�����Ự"
session=tf.Session()
#"������0�᷽���ϵĺ�"
sum0=tf.reduce_sum(value2d,axis=0)
print("�� 0 �᷽���ϵĺ�:")
print(session.run(sum0))
#"������1�᷽���ϵĺ�"
sum1=tf.reduce_sum(value2d,axis=1)
print("�� 1 �᷽���ϵĺ�:")
print(session.run(sum1))
#"������(0,1)ƽ���ϵĺ�"
sum01=tf.reduce_sum(value2d,axis=(0,1))
print("�� (0,1) ƽ���ϵĺ�:")
print(session.run(sum01))