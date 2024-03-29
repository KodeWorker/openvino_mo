# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.Cast import Cast
from ops.cumsum import CumSum
from front.common.partial_infer.utils import int64_array
from front.common.replacement import FrontReplacementOp
from front.mxnet.extractors.utils import get_mxnet_layer_attrs, mxnet_str_dtype_to_np
from front.tf.graph_utils import create_op_node_with_second_input
from graph.graph import Graph, rename_node, Node
from ops.const import Const


class CumSumFrontReplacer(FrontReplacementOp):
    op = 'MXNetCumSum'
    enabled = True

    def replace_op(self, graph: Graph, node: Node):
        name = node.soft_get('name', node.id)
        axis = node.soft_get('axis', 0)

        rename_node(node=node, name=name + '/to_be_removed')
        cumsum_node = create_op_node_with_second_input(graph, CumSum, int64_array(axis),
                                                       {'name': name, 'reverse': False, 'exclusive': False})
        rename_node(cumsum_node, name)

        node.in_port(0).get_connection().set_destination(cumsum_node.in_port(0))
        if node.has_valid('mx_out_type') and node['mx_out_type'] is not None:
            rename_node(node=cumsum_node, name=name + '/CumSum')
            convert = Cast(graph, {'name': name, 'dst_type': node['mx_out_type']}).create_node()
            rename_node(convert, name)
            cumsum_node.out_port(0).connect(convert.in_port(0))
            return [convert.id]
        else:
            return [cumsum_node.id]
