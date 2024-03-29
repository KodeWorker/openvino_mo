# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import numpy as np

from ops.argmax import arg_ops_infer
from graph.graph import Graph
from ops.op import Op


class ArgMinOp(Op):
    op = 'ArgMin'
    enabled = False

    def __init__(self, graph: Graph, attrs: dict):
        mandatory_props = {
            'type': None,
            'op': self.op,
            'infer': arg_ops_infer,
            'output_type': np.int64,
            'in_ports_count': 2,
            'out_ports_count': 1,
        }
        super().__init__(graph, mandatory_props, attrs)

    def supported_attrs(self):
        return [
            'top_k',
            'axis',
        ]
