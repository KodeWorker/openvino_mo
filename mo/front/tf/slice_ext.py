# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from graph.graph import Node
from ops.slice import TFSlice


class SliceExtractor(FrontExtractorOp):
    op = 'Slice'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        TFSlice.update_node_stat(node)
        return cls.enabled
