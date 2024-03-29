# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.activation_ops import Floor
from front.extractor import FrontExtractorOp


class FloorExtractor(FrontExtractorOp):
    op = 'Floor'
    enabled = True

    @classmethod
    def extract(cls, node):
        Floor.update_node_stat(node, {})
        return cls.enabled
