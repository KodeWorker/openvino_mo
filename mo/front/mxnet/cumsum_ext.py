# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from ops.cumsum import MXNetCumSum
from front.extractor import FrontExtractorOp
from front.mxnet.extractors.utils import get_mxnet_layer_attrs, mxnet_str_dtype_to_np


class CumSumExtractor(FrontExtractorOp):
    op = '_np_cumsum'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = get_mxnet_layer_attrs(node.symbol_dict)

        update_attrs = {
            'axis': attrs.int('axis', 0),
            'mx_out_type': attrs.dtype('dtype', None)
        }

        MXNetCumSum.update_node_stat(node, update_attrs)
        return cls.enabled
