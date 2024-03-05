# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.cumsum import CumSum
from front.extractor import FrontExtractorOp
from front.onnx.extractors.utils import onnx_attr


class CumSumFrontExtractor(FrontExtractorOp):
    op = 'CumSum'
    enabled = True

    @classmethod
    def extract(cls, node):
        exclusive = onnx_attr(node, 'exclusive', 'i', 0)
        reverse = onnx_attr(node, 'reverse', 'i', 0)
        CumSum.update_node_stat(node, {'exclusive': exclusive, 'reverse': reverse})
        return cls.enabled
