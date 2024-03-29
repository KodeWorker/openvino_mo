# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.select import Select
from front.extractor import FrontExtractorOp


class WhereFrontExtractor(FrontExtractorOp):
    op = 'where'
    enabled = True

    @classmethod
    def extract(cls, node):
        Select.update_node_stat(node, {})
        return cls.enabled
