# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.activation_ops import Sign
from front.extractor import FrontExtractorOp


class SignExtractor(FrontExtractorOp):
    op = 'Sign'
    enabled = True

    @classmethod
    def extract(cls, node):
        Sign.update_node_stat(node)
        return cls.enabled
