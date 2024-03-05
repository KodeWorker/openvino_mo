# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import numpy as np

from front.common.partial_infer.utils import mo_array, int64_array
from front.extractor import FrontExtractorOp
from front.onnx.extractors.utils import onnx_attr
from ops.group_norm import GroupNorm


class ExperimentalDetectronGroupNorm(FrontExtractorOp):
    op = 'ExperimentalDetectronGroupNorm'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = {
            'eps': mo_array(onnx_attr(node, 'eps', 'f', default=1e-6), dtype=float),
            'num_groups': int64_array(onnx_attr(node, 'num_groups', 'i', default=1)),
        }
        GroupNorm.update_node_stat(node, attrs)
        return cls.enabled


class GroupNormExtractor(FrontExtractorOp):
    op = 'GroupNorm'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = {
            'eps': mo_array(onnx_attr(node, 'eps', 'f', default=1e-6), dtype=float),
            'num_groups': int64_array(onnx_attr(node, 'num_groups', 'i', default=1)),
        }
        GroupNorm.update_node_stat(node, attrs)
        return cls.enabled
