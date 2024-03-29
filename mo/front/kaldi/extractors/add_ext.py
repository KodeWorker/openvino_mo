# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.elementwise import Add
from front.extractor import FrontExtractorOp


class AddFrontExtractor(FrontExtractorOp):
    op = 'Add'
    enabled = True

    @classmethod
    def extract(cls, node):
        Add.update_node_stat(node, {})
        return cls.enabled
