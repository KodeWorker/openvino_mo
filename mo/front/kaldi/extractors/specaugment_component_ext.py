# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.identity import Identity
from front.extractor import FrontExtractorOp


class SpecAugmentComponentFrontExtractor(FrontExtractorOp):
    op = 'specaugmenttimemaskcomponent'
    enabled = True

    @classmethod
    def extract(cls, node):
        Identity.update_node_stat(node, {})
        return cls.enabled
