# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.common.replacement import FrontReplacementOp, FrontReplacementPattern, FrontReplacementSubgraph
from front.extractor import FrontExtractorOp, CaffePythonFrontExtractorOp


def get_front_classes():
    front_classes = [FrontExtractorOp, CaffePythonFrontExtractorOp, FrontReplacementOp,
                     FrontReplacementPattern, FrontReplacementSubgraph]
    return front_classes
