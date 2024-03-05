# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.instance_normalization import InstanceNormalization
from front.extractor import FrontExtractorOp
from front.mxnet.extractors.utils import get_mxnet_layer_attrs
from graph.graph import Node


class InstanceNormFrontExtractor(FrontExtractorOp):
    op = 'InstanceNorm'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        attr = get_mxnet_layer_attrs(node.symbol_dict)
        node_attrs = {
            'epsilon': attr.float('eps', 0.001)
        }

        InstanceNormalization.update_node_stat(node, node_attrs)
        return cls.enabled
