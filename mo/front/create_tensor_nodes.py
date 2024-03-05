# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.common.replacement import FrontReplacementPattern
from front.extractor import create_tensor_nodes
from graph.graph import Graph


class CreateTensorNodes(FrontReplacementPattern):
    enabled = True
    force_clean_up = True

    def run_before(self):
        return []

    def run_after(self):
        from front.pass_separator import FrontFinish
        return [FrontFinish]

    def find_and_replace_pattern(self, graph: Graph):
        graph.stage = 'middle'
        graph.strict_mode = False
        create_tensor_nodes(graph)
        graph.strict_mode = True
