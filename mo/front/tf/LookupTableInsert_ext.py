# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.LookupTableInsert import LookupTableInsert
from front.extractor import FrontExtractorOp


class LookupTableInsertFrontExtractor(FrontExtractorOp):
    op = 'LookupTableInsert'
    enabled = True

    @classmethod
    def extract(cls, node):
        LookupTableInsert.update_node_stat(node, {})
        return cls.enabled


class LookupTableInsertV2FrontExtractor(FrontExtractorOp):
    op = 'LookupTableInsertV2'
    enabled = True

    @classmethod
    def extract(cls, node):
        LookupTableInsert.update_node_stat(node, {})
        return cls.enabled
