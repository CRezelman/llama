# LLaMa

Locally run LLaMa model

## Requirements
1. Install Visual Studio Installer. Select the following:
   - Visual Studio Community 2022
   - Visual Studio Build Tools >> Desktop Development with C++. See [here](https://medium.com/@piyushbatra1999/installing-llama-cpp-python-with-nvidia-gpu-acceleration-on-windows-a-short-guide-0dfac475002d)

2. CMake
3. Cuda Toolkit (I use v12.6)
4. Set ENV Variables before installinng `python-cpp-llama` to enable GPU Acceleration

```powershell
$env:FORCE_CMAKE='1'; $env:CMAKE_ARGS='-DGGML_CUDA=on -DLLAMA_AVX=off -DLLAMA_AVX2=off -DLLAMA_FMA=off -DCMAKE_GENERATOR_TOOLSET=cuda="C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.6"'
```

## Getting Started

Ensure you have Python 3 installed.
Navigate to `./`, using Powershell:

1. Create a Virtual Environment, run

```powershell
python -m venv venv
```

2. Actiavte Virtual Environment, run

```powershell
.\venv\Scripts\activate
```

3. Install Dependencies
   ```powershell
   python -m pip install -r .\requirements.txt
   ```
4. Install Models

Available models can be found [here](https://huggingface.co/TheBloke/NexusRaven-V2-13B-GGUF "NexusRaven"). This repo currently uses `nexusraven-v2-13b.Q5_K_M.gguf`

```powershell
huggingface-cli download TheBloke/NexusRaven-V2-13B-GGUF nexusraven-v2-13b.Q5_K_M.gguf --local-dir ./app/llm/models --local-dir-use-symlinks False
```

## Virtual Environment

A virtual environment (venv) lets you have a stable, reproducible, and portable environment. You are in control of which packages versions are installed and when they are upgraded.

### Activate Virtual Environment

```ps
.\venv\Scripts\activate
```

### Deactivate Virtual Environment

```ps
deactiavte
```

### Adding a Package

1. Ensure you have activated the virtual Environment
2. Install desired package:

```ps
python -m pip install <package_name>
```

3. Update the `requirements.txt` file with the new package

```ps
python -m pip freeze > requirements.txt
```
