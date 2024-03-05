# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.BatchNormInference import BatchNormInference
from front.extractor import FrontExtractorOp
from front.onnx.extractors.utils import onnx_attr


class BatchNormalizationExtractor(FrontExtractorOp):
    op = 'BatchNormalization'
    enabled = True

    @classmethod
    def extract(cls, node):
        attr_dict = {
           'data_format': 'NCHW',
           'eps': onnx_attr(node, 'epsilon', 'f', 1e-5),
        }
        BatchNormInference.update_node_stat(node, attr_dict)
        return cls.enabled
