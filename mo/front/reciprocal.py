# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.elementwise import Pow
from front.common.partial_infer.utils import mo_array
from front.common.replacement import FrontReplacementOp
from graph.graph import Node, Graph
from ops.const import Const


class ReciprocalReplacer(FrontReplacementOp):
    op = "Reciprocal"
    enabled = True

    def replace_op(self, graph: Graph, node: Node):
        const = Const(graph, dict(value=mo_array(-1.), name=node.name + '/reciprocal_pow_const_')).create_node()
        reciprocal = Pow(graph, {'name': node.name + '/reciprocal_pow_'}).create_node()
        node.in_port(0).get_connection().set_destination(reciprocal.in_port(0))
        const.out_port(0).connect(reciprocal.in_port(1))
        return [reciprocal.id]
