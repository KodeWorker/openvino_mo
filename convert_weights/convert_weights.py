# -*- coding: utf-8 -*-

import tf2onnx
import numpy as np
import tensorflow as tf
import od_model
import fast_od_model

from utils import load_weights, detections_boxes, freeze_graph
import json

FLAGS = tf.compat.v1.app.flags.FLAGS
# for anchors and classes
tf.compat.v1.app.flags.DEFINE_string(
    'json_file', 'model.json', 'model JSON file')
tf.compat.v1.app.flags.DEFINE_string(
    'weights_file', 'model.weights', 'Binary file with detector weights')
tf.compat.v1.app.flags.DEFINE_string(
    'data_format', 'NCHW', 'Data format: NCHW (gpu only) / NHWC')
tf.compat.v1.app.flags.DEFINE_string(
    'output_graph', 'frozen_model.pb', 'Frozen tensorflow protobuf model output path')
tf.compat.v1.app.flags.DEFINE_bool(
    'fast', False, 'Use fast model version of model')
tf.compat.v1.app.flags.DEFINE_integer(
    'size', 416, 'Image size')

# tf2onnx
tf.compat.v1.app.flags.DEFINE_bool(
    'tf2onnx', False, 'convert from pb to onnx')
tf.compat.v1.app.flags.DEFINE_integer(
    'opset', 13, 'convert from pb to onnx')

tf.compat.v1.app.flags.DEFINE_string(
    'input_graph', 'frozen_model.pb', 'Frozen tensorflow protobuf model input path')
tf.compat.v1.app.flags.DEFINE_string(
    'output_onnx', 'frozen_model.onnx', 'ONNX model output path')
tf.compat.v1.app.flags.DEFINE_list(
    'inputs', 'input:0', 'list of input names')
tf.compat.v1.app.flags.DEFINE_list(
    'outputs', 'output:0', 'list of output names')
    
def main(argv=None):
    
    if FLAGS.tf2onnx:
        
        graph_def, inputs, outputs = tf2onnx.tf_loader.from_graphdef(FLAGS.input_graph, FLAGS.inputs, FLAGS.outputs)
        
        model_proto, external_tensor_storage = tf2onnx.convert.from_graph_def(graph_def,
        name=None, input_names=FLAGS.inputs, output_names=FLAGS.outputs, opset=FLAGS.opset,
        custom_ops=None, custom_op_handlers=None, custom_rewriter=None, 
        inputs_as_nchw=None, extra_opset=None,
        shape_override=None, target=None, large_model=False,
        output_path=FLAGS.output_onnx)
        
    else:
        tf.compat.v1.disable_eager_execution()
        
        with open(FLAGS.json_file, "r") as read_file:
            info = json.load(read_file)
                
        if FLAGS.fast:
            model = fast_od_model.fast_od_model
        else:
            
            anchors = info[0]["custom_attributes"]["anchors"]
            it = iter(anchors)
            od_model._ANCHORS = [*zip(it, it)]
            model = od_model.od_model

        classes = info[0]["custom_attributes"]["classes"]

        # placeholder for detector inputs
        inputs = tf.compat.v1.placeholder(tf.float32, [None, FLAGS.size, FLAGS.size, 3], "inputs")

        with tf.compat.v1.variable_scope('detector'):
            detections = model(inputs, classes, data_format=FLAGS.data_format)
            load_ops = load_weights(tf.compat.v1.global_variables(scope='detector'), FLAGS.weights_file)

        # Sets the output nodes in the current session
        boxes = detections_boxes(detections)

        with tf.compat.v1.Session() as sess:
            sess.run(load_ops)
            freeze_graph(sess, FLAGS.output_graph)

if __name__ == '__main__':
    tf.compat.v1.app.run()
