# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.activation_ops import SoftPlus
from front.extractor import FrontExtractorOp


class SoftPlusExtractor(FrontExtractorOp):
    op = 'Softplus'
    enabled = True

    @classmethod
    def extract(cls, node):
        SoftPlus.update_node_stat(node, {})
        return cls.enabled
