# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.TensorArrayGather import TensorArrayGather
from front.extractor import FrontExtractorOp
from front.tf.extractors.utils import tf_tensor_shape
from graph.graph import Node


class TensorArrayGatherV3Extractor(FrontExtractorOp):
    op = "TensorArrayGatherV3"
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        attrs = {
            'op': __class__.op,
            'element_shape': tf_tensor_shape(node.pb.attr["element_shape"].shape),
        }
        TensorArrayGather.update_node_stat(node, attrs)
        return cls.enabled

