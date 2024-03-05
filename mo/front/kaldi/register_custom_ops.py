# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.common.replacement import FrontReplacementOp, FrontReplacementSubgraph, FrontReplacementPattern
from front.extractor import FrontExtractorOp


def get_front_classes():
    front_classes = [FrontExtractorOp, FrontReplacementOp, FrontReplacementPattern, FrontReplacementSubgraph]
    return front_classes
