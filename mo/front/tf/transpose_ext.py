# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.transpose import Transpose
from front.extractor import FrontExtractorOp


class TransposeFrontExtractorTF(FrontExtractorOp):
    op = 'Transpose'
    enabled = True

    @classmethod
    def extract(cls, node):
        Transpose.update_node_stat(node, {'order': None})
        return cls.enabled
