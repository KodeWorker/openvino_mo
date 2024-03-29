# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
from middle.InsertSelect import check_inputs
from middle.MakeKaldiConstReshapable import create_const_with_batch_from_input
from front.common.replacement import FrontReplacementPattern
from graph.graph import Graph


class ReplaceDropoutMaskPattern(FrontReplacementPattern):
    enabled = True

    def run_after(self):
        from front.restore_ports import RestorePorts
        return [RestorePorts]

    def run_before(self):
        from front.kaldi.replace_lstm_nonlinearity import ReplaceLstmNonLinearityPattern
        return [ReplaceLstmNonLinearityPattern]

    def find_and_replace_pattern(self, graph: Graph):
        inp = check_inputs(graph)
        batch_port = inp.out_port(0)
        replace_nodes = graph.get_op_nodes(op='dropoutmaskcomponent')
        for dropout_node in replace_nodes:
            assert dropout_node.has_and_set('size'), "DropoutMaskComponent has not set size attribute"
            assert dropout_node.size > 0, "DropoutMaskComponent has negative or zero size attribute"
            assert dropout_node.has_and_set('dropout_proportion'), \
                "DropoutMaskComponent has not set dropout_proportion attribute"
            assert dropout_node.dropout_proportion > 0, \
                "DropoutMaskComponent has negative or zero dropout_proportion attribute"
            dp_const_node = create_const_with_batch_from_input(batch_port, dropout_node.size,
                                                               dropout_node.dropout_proportion)
            dropout_node.out_port(0).get_connection().set_source(dp_const_node.out_port(0))
            graph.remove_node(dropout_node.id)
