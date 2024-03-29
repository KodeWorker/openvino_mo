# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.sparse_segment_mean import SparseSegmentMean
from front.extractor import FrontExtractorOp


class SparseSegmentMeanFrontExtractor(FrontExtractorOp):
    op = 'SparseSegmentMean'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = {}

        SparseSegmentMean.update_node_stat(node, attrs)

        return cls.enabled
