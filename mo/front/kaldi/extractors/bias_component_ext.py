# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.caffe.extractors.utils import embed_input
from front.extractor import FrontExtractorOp
from front.kaldi.loader.utils import find_next_tag, read_placeholder, collect_until_token
from front.kaldi.utils import read_binary_vector
from ops.scale_shift import ScaleShiftOp


class FixedBiasComponentFrontExtractor(FrontExtractorOp):
    op = 'fixedbiascomponent'
    enabled = True

    @classmethod
    def extract(cls, node):
        pb = node.parameters
        collect_until_token(pb, b'<Bias>')
        biases = read_binary_vector(pb)
        find_next_tag(pb)
        read_placeholder(pb, 1)

        mapping_rule = {
            'layout': 'NCHW',
            'bias_term': True,
            'out-size': biases.shape[0],
        }
        embed_input(mapping_rule, 2, 'biases', biases)

        ScaleShiftOp.update_node_stat(node, mapping_rule)
        return cls.enabled
