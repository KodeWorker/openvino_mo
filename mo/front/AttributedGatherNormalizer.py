# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.gather import Gather
from front.common.partial_infer.utils import int64_array
from front.common.replacement import FrontReplacementOp
from graph.graph import Graph
from ops.const import Const


class AttributedGatherNormalizer(FrontReplacementOp):
    op = "AttributedGather"
    enabled = True

    def replace_sub_graph(self, graph: Graph, match: dict):
        node = match['op']
        name = node.soft_get('name', node.id)
        assert node.has_valid('axis')

        axis = Const(graph, {'name': name + '/axis', 'value': int64_array(node.axis)}).create_node()
        gather = Gather(graph, {'name': name}).create_node()
        node.in_port(0).get_connection().set_destination(gather.in_port(0))
        node.in_port(1).get_connection().set_destination(gather.in_port(1))
        axis.out_port(0).connect(gather.in_port(2))
        node.out_port(0).get_connection().set_source(gather.out_port(0))
