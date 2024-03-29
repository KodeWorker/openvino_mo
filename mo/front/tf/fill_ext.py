# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from ops.fill import Fill


class FillExtractor(FrontExtractorOp):
    op = 'Fill'
    enabled = True

    @classmethod
    def extract(cls, node):
        Fill.update_node_stat(node, {})
        return cls.enabled
