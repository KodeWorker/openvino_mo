# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from front.mxnet.extractors.utils import get_mxnet_layer_attrs
from graph.graph import Node
from ops.tile import Tile


class TileExt(FrontExtractorOp):
    op = 'tile'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        attrs = get_mxnet_layer_attrs(node.symbol_dict)
        Tile.update_node_stat(node, {
            'reps': attrs.tuple('reps', int, None),
        })
        return cls.enabled
