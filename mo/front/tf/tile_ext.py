# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from ops.tile import Tile


class TileExtractor(FrontExtractorOp):
    op = 'Tile'
    enabled = True

    @classmethod
    def extract(cls, node):
        Tile.update_node_stat(node, {})
        return cls.enabled
