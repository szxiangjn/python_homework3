# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:20:42 2019

@author: 70437
"""
import tensorflow as tf
import numpy as np

class fast_style_transfer():
    
    def __init__(self):
        
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())
        self.saver = tf.train.import_meta_graph('fast_style_transfer.meta')
        
        graph = tf.get_default_graph()
        self.X = graph.get_tensor_by_name('X:0')
        self.g = graph.get_tensor_by_name('transformer/g:0')
        
    def transfer(self, im, style):
        
        model = 'samples_%s' % style
        self.saver.restore(self.sess, tf.train.latest_checkpoint(model))
        gen_img = self.sess.run(self.g, feed_dict={self.X: [im]})[0]
        gen_img = np.clip(gen_img, 0, 255) / 255.
        
        return gen_img