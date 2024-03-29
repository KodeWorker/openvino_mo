# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.activation_ops import ReLU
from front.extractor import FrontExtractorOp


class ReLUFrontExtractor(FrontExtractorOp):
    op = 'relu'
    enabled = True

    @classmethod
    def extract(cls, node):
        ReLU.update_node_stat(node)
        return ReLUFrontExtractor.enabled
