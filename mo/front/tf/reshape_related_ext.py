# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import numpy as np

from ops.rank import Rank
from ops.size import Size
from front.extractor import FrontExtractorOp
from front.tf.extractors.utils import tf_int_list, tf_dtype_extractor
from graph.graph import Node
from ops.reshape import Reshape
from ops.shape import Shape
from ops.squeeze import Squeeze


class RankFrontExtractor(FrontExtractorOp):
    op = 'Rank'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        Rank.update_node_stat(node, {'output_type': np.int32})
        return cls.enabled


class ReshapeExtractor(FrontExtractorOp):
    op = 'Reshape'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        Reshape.update_node_stat(node, {'special_zero': False})
        return cls.enabled


class ShapeExtractor(FrontExtractorOp):
    op = 'Shape'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        Shape.update_node_stat(node, {'output_type': tf_dtype_extractor(node.pb.attr['out_type'].type, np.int32)})
        return cls.enabled


class SizeFrontExtractor(FrontExtractorOp):
    op = 'Size'
    enabled = True

    @classmethod
    def extract(cls, node):
        Size.update_node_stat(node, {'output_type': tf_dtype_extractor(node.pb.attr['out_type'].type, np.int32)})
        return cls.enabled


class SqueezeExtractor(FrontExtractorOp):
    op = 'Squeeze'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        Squeeze.update_node_stat(node, {'squeeze_dims': tf_int_list(node.pb.attr['squeeze_dims'].list)})
        return cls.enabled
