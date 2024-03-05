# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import sys

from utils.cli_parser import get_all_cli_parser  # pylint: disable=no-name-in-module,import-error

from openvino.frontend import FrontEndManager  # pylint: disable=no-name-in-module,import-error


if __name__ == "__main__":
    from main import main
    sys.exit(main(get_all_cli_parser(), 'paddle'))
