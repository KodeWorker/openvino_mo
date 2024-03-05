# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.caffe.extractors.utils import embed_input
from front.extractor import FrontExtractorOp
from front.kaldi.loader.utils import find_next_tag, read_placeholder, collect_until_token
from front.kaldi.utils import read_binary_vector
from ops.scale_shift import ScaleShiftOp


class NaturalGradientPerElementScaleComponentFrontExtractor(FrontExtractorOp):
    op = 'naturalgradientperelementscalecomponent'
    enabled = True

    @classmethod
    def extract(cls, node):
        pb = node.parameters
        collect_until_token(pb, b'<Params>')
        weights = read_binary_vector(pb)
        find_next_tag(pb)
        read_placeholder(pb, 1)

        mapping_rule = {
            'layout': 'NCHW'
        }
        embed_input(mapping_rule, 1, 'weights', weights)

        ScaleShiftOp.update_node_stat(node, mapping_rule)
        return cls.enabled


class FixedScaleComponentFrontExtractor(FrontExtractorOp):
    op = 'fixedscalecomponent'
    enabled = True

    @classmethod
    def extract(cls, node):
        pb = node.parameters
        collect_until_token(pb, b'<Scales>')
        weights = read_binary_vector(pb)
        find_next_tag(pb)
        read_placeholder(pb, 1)

        mapping_rule = {
            'layout': 'NCHW',
            'out-size': weights.shape[0],
        }
        embed_input(mapping_rule, 1, 'weights', weights)

        ScaleShiftOp.update_node_stat(node, mapping_rule)
        return cls.enabled
