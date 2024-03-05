# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from ops.log_softmax import LogSoftmax
from front.extractor import FrontExtractorOp


class LogSoftMaxComponentExtractor(FrontExtractorOp):
    op = 'logsoftmaxcomponent'
    enabled = True

    @classmethod
    def extract(cls, node):
        LogSoftmax.update_node_stat(node, {'axis': 1})
        return cls.enabled
