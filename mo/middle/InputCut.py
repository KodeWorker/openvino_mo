# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import add_input_ops
from graph.graph import Graph
from middle.replacement import MiddleReplacementPattern


class MiddleInputCut(MiddleReplacementPattern):
    enabled = True
    force_clean_up = True
    run_not_recursively = True

    def run_after(self):
        from middle.pass_separator import PreMiddleStart
        return [PreMiddleStart]

    def run_before(self):
        from middle.pass_separator import MiddleStart
        return [MiddleStart]

    def find_and_replace_pattern(self, graph: Graph):
        add_input_ops(graph, graph.graph['user_shapes'], False)
