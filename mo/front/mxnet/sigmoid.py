# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.activation_ops import Sigmoid
from front.extractor import FrontExtractorOp


class SigmoidFrontExtractor(FrontExtractorOp):
    op = 'sigmoid'
    enabled = True

    @classmethod
    def extract(cls, node):
        Sigmoid.update_node_stat(node)
        return cls.enabled
