# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.activation_ops import LeakyReLU, ReLU
from front.extractor import FrontExtractorOp


class ReLUFrontExtractor(FrontExtractorOp):
    op = 'relu'
    enabled = True

    @classmethod
    def extract(cls, node):
        assert node.pb, 'Protobuf layer can not be empty'
        param = node.pb.relu_param
        negative_slope = param.negative_slope
        if negative_slope == 0:
            ReLU.update_node_stat(node)
        else:
            LeakyReLU.update_node_stat(node, {'negative_slope': negative_slope})
        return True
