# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from ops.activation_ops import SoftSign


class SoftSignExtractor(FrontExtractorOp):
    op = 'softsign'
    enabled = True

    @classmethod
    def extract(cls, node):
        SoftSign.update_node_stat(node, {})
        return cls.enabled
