# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from subprocess_main import subprocess_main
from utils.telemetry_utils import init_mo_telemetry
init_mo_telemetry()
subprocess_main(framework=None)
