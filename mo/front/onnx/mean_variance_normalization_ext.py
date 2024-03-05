# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.mvn import MVNOnnx
from front.common.partial_infer.utils import int64_array
from front.extractor import FrontExtractorOp
from front.onnx.extractors.utils import onnx_attr


class MeanVarianceNormalizationExtractor(FrontExtractorOp):
    op = 'MeanVarianceNormalization'
    enabled = True

    @classmethod
    def extract(cls, node):
        axes = onnx_attr(node, 'axes', 'ints',
                         default=int64_array([0, 2, 3]),
                         dst_type=lambda x: int64_array(x))

        attrs = {
            'eps': 1e-9,
            'normalize_variance': 1,
            'axes': axes,
            'eps_mode': 'outside_sqrt',
        }

        MVNOnnx.update_node_stat(node, attrs)
        return cls.enabled
