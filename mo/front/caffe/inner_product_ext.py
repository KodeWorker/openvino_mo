# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.MatMul import FullyConnected
from front.caffe.extractors.utils import weights_biases
from front.extractor import FrontExtractorOp


class InnerProductFrontExtractor(FrontExtractorOp):
    op = 'innerproduct'
    enabled = True

    @classmethod
    def extract(cls, node):
        param = node.pb.inner_product_param
        pb_model = node.model_pb
        attrs = {
            'out-size': param.num_output,
            'transpose_weights': not param.transpose,
        }
        attrs.update(weights_biases(param.bias_term, pb_model))
        FullyConnected.update_node_stat(node, attrs)
        return cls.enabled


class AnotherInnerProductFrontExtractor(FrontExtractorOp):
    op = 'inner_product'
    enabled = True

    @classmethod
    def extract(cls, node):
        param = node.pb.inner_product_param
        pb_model = node.model_pb
        attrs = {
            'out-size': param.num_output,
            'transpose_weights': not param.transpose,
        }
        attrs.update(weights_biases(param.bias_term, pb_model))
        FullyConnected.update_node_stat(node, attrs)
        return cls.enabled
