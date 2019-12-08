# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf   # 引入 Tensorflow 库
gjm = tf.constant("Hello World ! I love TensorFlow ! ")   #创建一个常量 Operation （操作）
sess = tf.Session()   #启动一个 TensorFlow 的 Session（会话）
print (sess.run(gjm))   #运行 Graph (计算图)  python3.x 专用语法
sess.close()   #关闭 Session （会话）