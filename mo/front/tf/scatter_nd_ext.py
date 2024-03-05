# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.scatternd import TFScatterND
from front.extractor import FrontExtractorOp


class ScatterNDExtractor(FrontExtractorOp):
    op = 'ScatterNd'
    enabled = True

    @classmethod
    def extract(cls, node):
        TFScatterND.update_node_stat(node, {})
        return cls.enabled
