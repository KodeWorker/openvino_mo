# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from graph.graph import Graph
from ops.op import Op


class CopyOp(Op):
    """
    Empty Op for Copy layer. It will be replaced by FrontReplacer
    """
    op = 'copy'
    enabled = True

    def __init__(self, graph: Graph, attrs: dict):
        super().__init__(graph, {
            'type': None,
            'op': __class__.op,
            'infer': None
        }, attrs)
