# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.activation_ops import Elu
from front.caffe.collect_attributes import collect_attributes
from front.extractor import FrontExtractorOp


class ELUFrontExtractor(FrontExtractorOp):
    op = 'ELU'
    enabled = True

    @classmethod
    def extract(cls, node):
        param = node.pb.elu_param
        attrs = collect_attributes(param)

        Elu.update_node_stat(node, attrs)
        return cls.enabled
