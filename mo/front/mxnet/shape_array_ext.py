# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from ops.shape import Shape


class ShapeArrayExtractor(FrontExtractorOp):
    op = 'shape_array'
    enabled = True

    @classmethod
    def extract(cls, node):
        Shape.update_node_stat(node, {})
        return cls.enabled

