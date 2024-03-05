# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import argparse
# DIT +++ [2024/03/25, Kelvin]
from graph.graph import Graph
from pipeline.common import get_ir_version
from utils import class_registration
# DIT --- [2024/03/25, Kelvin]
def unified_pipeline(argv: argparse.Namespace):
    graph = Graph(cmd_params=argv, name=argv.model_name, ir_version=get_ir_version(argv))
    class_registration.apply_replacements(graph, [
        class_registration.ClassType.LOADER,
        class_registration.ClassType.FRONT_REPLACER,
        class_registration.ClassType.MIDDLE_REPLACER,
        class_registration.ClassType.BACK_REPLACER
    ])
    return graph
