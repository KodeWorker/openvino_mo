# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.common.replacement import FrontReplacementPattern
from graph.graph import Graph


class DeformableConvolutionReplacer(FrontReplacementPattern):
    # swap mask and weights inputs for ModulatedDeformableConvolution according to the specification
    enabled = True

    def find_and_replace_pattern(self, graph: Graph):

        for deform_conv in graph.get_op_nodes(type='DeformableConvolution'):
            if len(deform_conv.get_inputs()) != 4:
                return

            m_source = deform_conv.in_port(2).get_source()
            deform_conv.in_port(2).disconnect()

            deform_conv.in_port(3).get_connection().set_destination(deform_conv.in_port(2))
            m_source.connect(deform_conv.in_port(3))
