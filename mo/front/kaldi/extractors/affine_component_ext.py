# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from front.kaldi.extractors.fixed_affine_component_ext import FixedAffineComponentFrontExtractor
from front.kaldi.utils import read_learning_info
from graph.graph import Node


class AffineComponentFrontExtractor(FrontExtractorOp):
    op = 'affinecomponent'
    enabled = True

    @classmethod
    def extract(cls, node: Node):
        read_learning_info(node.parameters)
        return FixedAffineComponentFrontExtractor.extract(node)
