# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.eye import TFEye
from front.extractor import FrontExtractorOp
from front.tf.extractors.utils import tf_dtype_extractor


class EyeExtractor(FrontExtractorOp):
    op = 'Eye'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = {
            'output_type': tf_dtype_extractor(node.pb.attr["dtype"].type),
        }
        TFEye.update_node_stat(node, attrs)
        return cls.enabled
