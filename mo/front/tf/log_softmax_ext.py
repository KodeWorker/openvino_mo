# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.extractor import FrontExtractorOp
from ops.log_softmax import LogSoftmax


class LogSoftmaxExtractor(FrontExtractorOp):
    op = 'LogSoftmax'
    enabled = True

    @classmethod
    def extract(cls, node):
        # the default value for the TF LogSoftmax is -1
        axis = -1
        if 'axis' in node.pb.attr:
            axis = node.pb.attr['axis'].i
        LogSoftmax.update_node_stat(node, {'axis': axis})
        return cls.enabled
