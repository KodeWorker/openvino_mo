# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import numpy as np

from ops.one_hot import OneHot
from front.extractor import FrontExtractorOp
from front.tf.extractors.utils import tf_dtype_extractor


class OneHotFrontExtractor(FrontExtractorOp):
    op = 'OneHot'
    enabled = True

    @classmethod
    def extract(cls, node):
        OneHot.update_node_stat(node, {'axis': node.pb.attr['axis'].i,
                                       'data_type': tf_dtype_extractor(node.pb.attr["T"].type, np.float32)})
        return cls.enabled
