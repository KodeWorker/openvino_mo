# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
from front.common.partial_infer.utils import int64_array
from front.extractor import FrontExtractorOp
from front.onnx.extractors.utils import onnx_attr
from ops.reshape import Reshape

class ReshapeFrontExtractor(FrontExtractorOp):
    op = 'Reshape'
    enabled = True

    @classmethod
    def extract(cls, node):
        dim = onnx_attr(node, 'shape', 'ints', None)
        if dim is not None:
            dim = int64_array(dim)
            Reshape.update_node_stat(node, {'dim': dim})
        else:
            Reshape.update_node_stat(node)
        return cls.enabled
