# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import logging as log

import networkx as nx

from front.common.replacement import FrontReplacementOp
from graph.graph import Graph
from utils.error import Error


class NoOpElimination(FrontReplacementOp):
    """
    NoOp does nothing and it has no data flow edges.
    It operates only with control flow edges.
    """
    op = "NoOp"
    enabled = True

    def replace_sub_graph(self, graph: Graph, match: dict):
        node = match['op']
        in_edges = node.in_edges()
        out_edges = node.out_edges()
        if len(in_edges) == 0 and len(out_edges) == 0:
            graph.remove_node(node.id)
            log.debug('NoOp op was removed {}'.format(node.id))
        else:
            raise Error('NoOp node {} contains data flow edges'.format(node.id))
