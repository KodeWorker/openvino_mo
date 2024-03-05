# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.sparse_segment_sum import SparseSegmentSum
from front.extractor import FrontExtractorOp


class SparseSegmentSumFrontExtractor(FrontExtractorOp):
    op = 'SparseSegmentSum'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = {}

        SparseSegmentSum.update_node_stat(node, attrs)

        return cls.enabled
