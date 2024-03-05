# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from middle.LeakyReluPattern import LeakyReLUFusion
from middle.pass_separator import PostMiddleStart
from graph.graph import Graph
from middle.replacement import MiddleReplacementPattern
from utils.error import Error
from utils.find_inputs import find_inputs
from utils.utils import refer_to_faq_msg


class CaffeMeanFileProcessing(MiddleReplacementPattern):
    enabled = True
    force_clean_up = True
    graph_condition = [lambda graph: graph.graph['fw'] == 'caffe']

    def run_after(self):
        return [LeakyReLUFusion]

    def run_before(self):
        return [PostMiddleStart]

    def find_and_replace_pattern(self, graph: Graph):
        from front.caffe import loader
        argv = graph.graph['cmd_params']
        original_shapes = graph.graph['original_shapes']
        caffe_pb2 = graph.graph['caffe_pb2']
        del graph.graph['caffe_pb2']
        input_names = find_inputs(graph)
        graph.graph['input_names'] = input_names
