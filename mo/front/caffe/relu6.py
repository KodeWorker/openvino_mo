# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.activation_ops import ReLU6
from front.extractor import FrontExtractorOp


class ReLU6FrontExtractor(FrontExtractorOp):
    op = 'ReLU6'
    enabled = True

    @classmethod
    def extract(cls, node):
        ReLU6.update_node_stat(node)
        return True
