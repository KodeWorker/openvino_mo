# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.range import Range
from front.extractor import FrontExtractorOp
from graph.graph import Node


class RangeFrontExtractor(FrontExtractorOp):
    op = 'Range'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        # output_type attribute will be deduced during shape infer
        Range.update_node_stat(node, {})
        return cls.enabled

