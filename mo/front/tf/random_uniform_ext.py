# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.random_uniform import AttributedRandomUniform
from front.extractor import FrontExtractorOp
from front.tf.extractors.utils import tf_dtype_extractor


class RandomUniformExtractor(FrontExtractorOp):
    op = 'RandomUniform'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = {
            'output_type': tf_dtype_extractor(node.pb.attr["dtype"].type),
            'global_seed': node.pb.attr['seed'].i,
            'op_seed': node.pb.attr['seed2'].i
        }
        AttributedRandomUniform.update_node_stat(node, attrs)
        return cls.enabled
