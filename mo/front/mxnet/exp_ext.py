# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.activation_ops import Exp
from front.extractor import FrontExtractorOp


class ExpExtractor(FrontExtractorOp):
    op = 'exp'
    enabled = True

    @classmethod
    def extract(cls, node):
        Exp.update_node_stat(node)
        return cls.enabled
