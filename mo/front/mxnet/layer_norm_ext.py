# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
from front.extractor import FrontExtractorOp
from front.mxnet.extractors.utils import get_mxnet_layer_attrs
from graph.graph import Node
from ops.layer_norm import LayerNorm


class LayerNormFrontExtractor(FrontExtractorOp):
    op = 'LayerNorm'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        attr = get_mxnet_layer_attrs(node.symbol_dict)

        node_attrs = {
            'epsilon': attr.float('eps', 9.99999975e-06),
            'axis': attr.int('axis', -1),
            'output_mean_var': attr.bool('output_mean_var', False)
        }
        LayerNorm.update_node_stat(node, node_attrs)
        return cls.enabled
