# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from ops.ClipByValueTF import ClibByValueTF


class ClipByValueExtractor(FrontExtractorOp):
    op = 'ClipByValue'
    enabled = True

    @classmethod
    def extract(cls, node):
        ClibByValueTF.update_node_stat(node, {})
        return cls.enabled
