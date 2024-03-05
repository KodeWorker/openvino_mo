# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.instance_normalization import InstanceNormalization
from front.extractor import FrontExtractorOp
from front.onnx.extractors.utils import onnx_attr


class InstanceNormalizationExtractor(FrontExtractorOp):
    op = 'InstanceNormalization'
    enabled = True

    @classmethod
    def extract(cls, node):
        epsilon = onnx_attr(node, 'epsilon', 'f', default=float(1e-5))
        InstanceNormalization.update_node_stat(node, {'epsilon': epsilon})
        return cls.enabled
