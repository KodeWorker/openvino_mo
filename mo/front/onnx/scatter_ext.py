# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.scatter import ScatterElementsUpdate
from ops.scatternd import ScatterNDUpdate
from front.extractor import FrontExtractorOp
from front.onnx.extractors.utils import onnx_attr


class ScatterExtractor(FrontExtractorOp):
    # deprecated ONNX operation
    op = 'Scatter'
    enabled = True

    @classmethod
    def extract(cls, node):
        axis = onnx_attr(node, 'axis', 'i', default=0)
        ScatterElementsUpdate.update_node_stat(node, {'axis': axis})
        return cls.enabled


class ScatterElementsExtractor(FrontExtractorOp):
    op = 'ScatterElements'
    enabled = True

    @classmethod
    def extract(cls, node):
        axis = onnx_attr(node, 'axis', 'i', default=0)
        ScatterElementsUpdate.update_node_stat(node, {'axis': axis})
        return cls.enabled


class ScatterNDExtractor(FrontExtractorOp):
    op = 'ScatterND'
    enabled = True

    @classmethod
    def extract(cls, node):
        ScatterNDUpdate.update_node_stat(node, {})
        return cls.enabled
