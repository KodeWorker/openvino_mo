# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from front.FakeQuantWithMinMaxVars import FakeQuantWithMinMaxVarsToQuantize
from front.common.replacement import FrontReplacementPattern
from graph.graph import Graph


class DisableQuantizeValuePropagation(FrontReplacementPattern):
    enabled = True

    def run_after(self):
        return [FakeQuantWithMinMaxVarsToQuantize]

    @staticmethod
    def pattern():
        return dict(
            nodes=[
                ('quantize', dict(op='FakeQuantize', levels=lambda levels: levels != 2)),
            ],
            edges=[]
        )

    @staticmethod
    def replace_pattern(graph: Graph, match: dict):
        match['quantize']['stop_value_propagation'] = True
