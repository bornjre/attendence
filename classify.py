
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

import numpy as np
import tensorflow as tf
import time

def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.GraphDef()

  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph


def read_tensor_from_image_file(file_name,
                                input_height=299,
                                input_width=299,
                                input_mean=0,
                                input_std=255):
  input_name = "file_reader"
  output_name = "normalized"
  file_reader = tf.read_file(file_name, input_name)
  if file_name.endswith(".png"):
    image_reader = tf.image.decode_png(
        file_reader, channels=3, name="png_reader")
  elif file_name.endswith(".gif"):
    image_reader = tf.squeeze(
        tf.image.decode_gif(file_reader, name="gif_reader"))
  elif file_name.endswith(".bmp"):
    image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
  else:
    image_reader = tf.image.decode_jpeg(
        file_reader, channels=3, name="jpeg_reader")
  float_caster = tf.cast(image_reader, tf.float32)
  dims_expander = tf.expand_dims(float_caster, 0)
  resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
  normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
  sess = tf.compat.v1.Session()
  result = sess.run(normalized)

  return result

def load_labels(label_file):
  label = []
  proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
  for l in proto_as_ascii_lines:
    label.append(l.rstrip())
  return label

class Classifier:
    def __init__(self, path):
        input_name = "import/" + "Placeholder"
        output_name = "import/" + "final_result"

        self.labelfile = "{}/mylabels.txt".format(path)
        self.graph = load_graph("{}/trained_graph.pb".format(path))
        self.input_operation = self.graph.get_operation_by_name(input_name)
        self.output_operation = self.graph.get_operation_by_name(output_name)

    def run(self, image):
        with tf.compat.v1.Session(graph=self.graph) as sess:
            results = sess.run(self.output_operation.outputs[0], {
                self.input_operation.outputs[0]: image
            })
        results = np.squeeze(results)

        top_k = results.argsort()[-5:][::-1]
        labels = load_labels(self.labelfile)

        label = labels[0]
        result = results[0]

        for i in top_k:
            print(labels[i], results[i])
            if results[i] > result:
                result = results[i]
                label = labels[i]
        return label, result

    def run_loop(self, inchannel:list, outchannel:list):
      
      lastkey = -1
      while True:

        job = None
        while True:
          try:
            job = inchannel.pop()
            if job is bool:
              return
            else:
              break
          except IndexError:
            time.sleep(.5)
        
        image = job[1]
        key = job[0]
        if key < lastkey:
          continue
        else:
          lastkey = key
        label, result =  self.run(image)
        outchannel.append((label, result))
# TODO add a seperate class as unregistered_people with random people as input images 