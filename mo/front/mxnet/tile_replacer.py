# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.common.partial_infer.utils import int64_array
from front.common.replacement import FrontReplacementOp
from graph.graph import Graph
from ops.const import Const


class TileReplacer(FrontReplacementOp):
    op = 'Tile'
    enabled = True

    def replace_sub_graph(self, graph: Graph, match: dict):
        node = match['op']
        if node.has_valid('reps'):
            tile_array = Const(graph, dict(value=int64_array(node.reps),
                                           symbol_dict={'name': node.id + '/tile_array'})).create_node()
            node.in_port(1).get_connection().set_source(tile_array.out_port(0))
