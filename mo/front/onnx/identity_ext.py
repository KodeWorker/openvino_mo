# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from ops.identity import Identity


class IdentityFrontExtractor(FrontExtractorOp):
    op = 'Identity'
    enabled = True

    @classmethod
    def extract(cls, node):
        Identity.update_node_stat(node)
        return cls.enabled
