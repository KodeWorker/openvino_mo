# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.onnx.extractors.utils import onnx_attr
from front.extractor import FrontExtractorOp
from ops.concat import Concat
    
class ConcatFrontExtractor(FrontExtractorOp):
    op = 'Concat'
    enabled = True

    @classmethod
    def extract(cls, node):
        mapping_rule = {
           'axis': onnx_attr(node, 'axis', 'i', default=0)
        }
        Concat.update_node_stat(node, mapping_rule)
        return cls.enabled
