# openvino_mo

This is and example project for freezing Model Optimizer of OpenVINO 2023.3.0

# Instructions
1. Create the environment
```conda env create -f ./openvino.yml```
2. Activate the environment
```conda activate openvino```
3. Freeze the Model Optimizer
```pyinstaller mo.spec```

# User Guide
1. Settings in openvino.yml & mo.spec

The binaries list in mo.spec and openvino-dev package options are depend on the models of your choice.
In my use case, tensorflow2 and onnx model are two kinds of model to be converted.
Therefore, ```openvino-dev[tensorflow2, onnx]``` is picked and the corresponding DLLs is included in ```mo.spec```

2. What's in the mo directory?

This directory is acually copied from the openvino/tools/mo in the virtual environment.
In order to freeze the tool properly, the following files are modified:
- mo/main.py
- mo/convert_impl.py
- mo/utils/cli_parser.py
- mo/utils/find_ie_version.py
- mo/utils/version