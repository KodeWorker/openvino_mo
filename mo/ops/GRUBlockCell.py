# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from graph.graph import Graph
from ops.op import Op


class GRUBlockCell(Op):
    op = 'GRUBlockCell'
    enabled = False

    def __init__(self, graph: Graph, attrs: dict):
        super().__init__(graph, {
            'type': None,
            'op': self.op,
            'infer': None,
            'in_ports_count': 6,
            'out_ports_count': 4,
        }, attrs)
