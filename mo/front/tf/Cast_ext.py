# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.Cast import Cast
from front.extractor import FrontExtractorOp
from front.tf.common import tf_data_type_decode


class CastFrontExtractor(FrontExtractorOp):
    op = 'Cast'
    enabled = True

    @classmethod
    def extract(cls, node):
        cast_dst_type = tf_data_type_decode[node.pb.attr['DstT'].type][0]
        Cast.update_node_stat(node, {'dst_type': cast_dst_type})
        return cls.enabled
