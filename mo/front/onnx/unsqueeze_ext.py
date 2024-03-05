# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.common.partial_infer.utils import int64_array
from front.extractor import FrontExtractorOp
from front.onnx.extractors.utils import onnx_attr
from ops.expand_dims import ExpandDims


class UnsqueezeFrontExtractor(FrontExtractorOp):
    """
    Convert Unsqueeze layer to ExpandDims because the ExpandDims layer has fixed attribute with dimensions to unsqueeze.
    """
    op = 'Unsqueeze'
    enabled = True

    @classmethod
    def extract(cls, node):
        axis = int64_array(onnx_attr(node, 'axes', 'ints', default=[]))

        ExpandDims.update_node_stat(node, {'expand_axis': axis})
        return cls.enabled
