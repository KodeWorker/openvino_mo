# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.common.replacement import FrontReplacementOp
from graph.graph import Graph, Node, rename_nodes
from ops.flatten import FlattenONNX
from ops.reshape import Reshape
from ops.shape import Shape
from ops.log_softmax import LogSoftmax


class LogSoftmaxONNXFrontReplacer(FrontReplacementOp):
    """
    Replace LogSoftmaxONNX operation with FlattenONNX -> LogSoftmax -> Reshape subgraph
    """
    op = "LogSoftmaxONNX"
    enabled = True

    def run_before(self):
        from front.onnx.flattenONNX_to_reshape import FlattenONNXToReshape
        return [FlattenONNXToReshape]

    def replace_op(self, graph: Graph, node: Node):
        node_name = node.soft_get('name', node.id)
        assert node.has_valid('axis'), 'The node "{}" does not have mandatory attribute "axis"'.format(node_name)

        flatten_node = FlattenONNX(graph, {'name': node_name + '/FlattenONNX_', 'axis': node.axis}).create_node()
        shape_node = Shape(graph, {'name': node_name + '/ShapeOf_'}).create_node()
        logsoftmax_node = LogSoftmax(graph, {'name': node_name + '/LogSoftmax_', 'axis': 1}).create_node()
        reshape_node = Reshape(graph,  {}).create_node()

        rename_nodes([(node, node_name + '/delete'), (reshape_node, node_name)])

        shape_node.out_port(0).connect(reshape_node.in_port(1))
        logsoftmax_node.out_port(0).connect(reshape_node.in_port(0))
        flatten_node.out_port(0).connect(logsoftmax_node.in_port(0))

        source = node.in_port(0).get_source()

        flatten_node.in_port(0).connect(source)
        shape_node.in_port(0).connect(source)

        return [reshape_node.id]
