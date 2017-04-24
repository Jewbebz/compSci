import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.constant(5.2)

sess = tf.Session()
print(sess.run([node1, node2, node3]))
