# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import numpy as np

from front.common.partial_infer.utils import mo_array
from ops.transpose import Transpose
from front.extractor import FrontExtractorOp
from front.mxnet.extractors.utils import get_mxnet_layer_attrs


class TransposeFrontExtractor(FrontExtractorOp):
    op = 'transpose'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = get_mxnet_layer_attrs(node.symbol_dict)
        order = list(attrs.tuple("axes", int, None))
        Transpose.update_node_stat(node, {'order': mo_array(order, dtype=np.int32)})
        return cls.enabled
