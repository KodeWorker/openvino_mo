# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import networkx as nx

from graph.graph import Graph
from middle.replacement import MiddleReplacementPattern


class AddIsCyclicAttribute(MiddleReplacementPattern):
    enabled = True

    def run_after(self):
        from middle.DeleteControlFlowEdges import DeleteControlFlowEdges
        return [DeleteControlFlowEdges]

    def run_before(self):
        return []

    @staticmethod
    def find_and_replace_pattern(graph: Graph):
        is_acyclic = nx.is_directed_acyclic_graph(graph)
        graph.graph['is_cyclic'] = not is_acyclic
