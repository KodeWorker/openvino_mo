# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.Complex import Complex
from front.extractor import FrontExtractorOp


class ComplexOpFrontExtractor(FrontExtractorOp):
    op = 'Complex'
    enabled = True

    @classmethod
    def extract(cls, node):
        Complex.update_node_stat(node, {})
        return cls.enabled
