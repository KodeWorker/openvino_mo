# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import numpy as np

from front.common.partial_infer.utils import float32_array
from ops.bucketize import Bucketize
from front.extractor import FrontExtractorOp


class BucketizeFrontExtractor(FrontExtractorOp):
    op = 'Bucketize'
    enabled = True

    @classmethod
    def extract(cls, node):
        boundaries = float32_array(node.pb.attr['boundaries'].list.f)
        Bucketize.update_node_stat(node, {'boundaries': boundaries, 'with_right_bound': False, 'output_type': np.int32})
        return cls.enabled
