# Copyright (C) 2018-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import numpy as np

from front.extractor import FrontExtractorOp
from front.mxnet.extractors.utils import get_mxnet_layer_attrs
from graph.graph import Node
from ops.arange_like import ArangeLikeOp


class ArangeLikeExt(FrontExtractorOp):
    op = '_contrib_arange_like'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        attrs = get_mxnet_layer_attrs(node.symbol_dict)
        ArangeLikeOp.update_node_stat(node, {
            'start': attrs.float('start', 0),
            'repeat': attrs.int('repeat', 1),
            'step': attrs.float('step', 1),
            'axis': attrs.int('axis', None),
        })
        return cls.enabled
