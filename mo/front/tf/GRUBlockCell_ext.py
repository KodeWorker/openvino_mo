# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from ops.GRUBlockCell import GRUBlockCell


class GRUBlockCellExtractor(FrontExtractorOp):
    op = 'GRUBlockCell'
    enabled = True

    @classmethod
    def extract(cls, node):
        GRUBlockCell.update_node_stat(node, {'format': 'tf'})
        return cls.enabled
