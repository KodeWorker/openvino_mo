# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.mxrepeat import MXRepeat
from front.extractor import FrontExtractorOp
from front.mxnet.extractors.utils import get_mxnet_layer_attrs
from graph.graph import Node


class RepeatExt(FrontExtractorOp):
    op = 'repeat'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        attrs = get_mxnet_layer_attrs(node.symbol_dict)
        axis = attrs.int('axis', 0)
        repeats = attrs.int('repeats', None)
        assert repeats is not None and repeats > 0, \
            '`repeat` op requires positive `repeats` attribute, but it is {} for node {}'.format(repeats, node.name)

        MXRepeat.update_node_stat(node, {
            'axis': axis,
            'repeats': repeats,
        })
        return cls.enabled
