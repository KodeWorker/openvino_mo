# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.caffe.collect_attributes import merge_attrs
from front.extractor import FrontExtractorOp
from ops.tile import AttributedTile


class TileFrontExtractor(FrontExtractorOp):
    op = 'Tile'
    enabled = True

    @classmethod
    def extract(cls, node):
        proto_layer = node.pb
        param = proto_layer.tile_param
        mapping_rule = {
            'axis': int(param.axis),
            'tiles': int(param.tiles),
        }
        mapping_rule = merge_attrs(param, mapping_rule)

        AttributedTile.update_node_stat(node, mapping_rule)
        return cls.enabled
