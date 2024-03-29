# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.shufflechannel import ShuffleChannels
from front.caffe.collect_attributes import collect_attributes
from front.common.extractors.utils import layout_attrs
from front.extractor import FrontExtractorOp


class ShuffleChannelFrontExtractor(FrontExtractorOp):
    op = 'ShuffleChannel'
    enabled = True

    @classmethod
    def extract(cls, node):
        mapping_rule = collect_attributes(node.pb.shuffle_channel_param)
        mapping_rule.update(layout_attrs())

        # update the attributes of the node
        ShuffleChannels.update_node_stat(node, mapping_rule)
        return cls.enabled
