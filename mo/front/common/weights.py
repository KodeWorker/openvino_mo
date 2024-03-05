# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from utils.graph import Graph


def swap_weights_xy(graph: Graph, nodes: list):
    from front.tf.ObjectDetectionAPI import swap_weights_xy as new_swap_weights_xy
    new_swap_weights_xy(graph, nodes)
