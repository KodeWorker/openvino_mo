# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.common.partial_infer.utils import int64_array
from front.extractor import FrontExtractorOp
from front.onnx.extractors.utils import onnx_attr
from ops.squeeze import Squeeze


class SqueezeFrontExtractor(FrontExtractorOp):
    op = 'Squeeze'
    enabled = True

    @classmethod
    def extract(cls, node):
        axis = int64_array(onnx_attr(node, 'axes', 'ints', default=[]))

        attrs = {
            'squeeze_dims': axis if len(axis) != 0 else None
        }

        # update the attributes of the node
        Squeeze.update_node_stat(node, attrs)
        return cls.enabled
