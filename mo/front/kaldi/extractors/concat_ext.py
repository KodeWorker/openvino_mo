# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from ops.concat import Concat


class ConcatFrontExtractor(FrontExtractorOp):
    op = 'concat'
    enabled = True

    @classmethod
    def extract(cls, node):
        mapping_rule = {
           'axis': 1
        }
        Concat.update_node_stat(node, mapping_rule)
        return cls.enabled
