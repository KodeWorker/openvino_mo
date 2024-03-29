# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from front.mxnet.extractors.utils import get_mxnet_layer_attrs
from ops.expand_dims import ExpandDims


class ExpandDimsExtractor(FrontExtractorOp):
    op = 'expand_dims'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = get_mxnet_layer_attrs(node.symbol_dict)
        expand_axis = attrs.int('axis', None)
        ExpandDims.update_node_stat(node, {'expand_axis': expand_axis})
        return cls.enabled
