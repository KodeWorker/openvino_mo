# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.activation_ops import Swish
from front.extractor import FrontExtractorOp
from graph.graph import Node


class SwishExtractor(FrontExtractorOp):
    op = 'swish_f32'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        Swish.update_node_stat(node, {})
        return cls.enabled

