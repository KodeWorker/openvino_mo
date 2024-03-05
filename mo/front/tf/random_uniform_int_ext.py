# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.random_uniform import RandomUniform
from front.extractor import FrontExtractorOp
from front.tf.extractors.utils import tf_dtype_extractor


class RandomUniformIntExtractor(FrontExtractorOp):
    op = 'RandomUniformInt'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = {
            'output_type': tf_dtype_extractor(node.pb.attr["Tout"].type),
            'global_seed': node.pb.attr['seed'].i,
            'op_seed': node.pb.attr['seed2'].i
        }
        RandomUniform.update_node_stat(node, attrs)
        return cls.enabled
