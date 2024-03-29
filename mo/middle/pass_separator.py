# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from graph.graph import Graph
from middle.replacement import MiddleReplacementPattern


class PreMiddleStart(MiddleReplacementPattern):
    enabled = True

    def run_after(self):
        return []

    def run_before(self):
        return []

    def find_and_replace_pattern(self, graph: Graph):
        pass


class MiddleStart(MiddleReplacementPattern):
    enabled = True

    def run_after(self):
        return []

    def run_before(self):

        return []

    def find_and_replace_pattern(self, graph: Graph):
        pass


class MiddleFinish(MiddleReplacementPattern):
    enabled = True

    def run_after(self):
        return []

    def run_before(self):
        return []

    def find_and_replace_pattern(self, graph: Graph):
        pass


class PostMiddleStart(MiddleReplacementPattern):
    enabled = True

    def run_after(self):
        return []

    def run_before(self):
        return []

    def find_and_replace_pattern(self, graph: Graph):
        pass

