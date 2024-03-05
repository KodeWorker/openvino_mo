# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from graph.graph import Node
from ops.broadcast import Broadcast


class BroadcastExtractor(FrontExtractorOp):
    op = 'BroadcastTo'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        Broadcast.update_node_stat(node, attrs={'mode': 'numpy'})
        return cls.enabled
