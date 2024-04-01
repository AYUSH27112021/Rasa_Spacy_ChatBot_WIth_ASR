# Nemo Telugu ASR

After facing issues with inference time taken by the whisper model we changed our approach and trained a nemo model by Nvidia with CTC-sub-encoding which had a faster inference time

Installation
------------

Conda
We recommend installing NeMo in a fresh Conda environment.
~~~
conda create --name nemo python==3.8.10
conda activate nemo
~~~

Install PyTorch using their `configurator <https://pytorch.org/get-started/locally/>`_.
~~~
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
~~~
The command used to install PyTorch may depend on your system. Please use the configurator linked above to find the right command for your system.

Pip
~~~
apt-get update && apt-get install -y libsndfile1 ffmpeg
pip install Cython
pip install nemo_toolkit['all']
~~~

Depending on the shell used, you may need to use ``"nemo_toolkit[all]"`` instead in the above command.

Pip from source

Use this installation mode if you want the version from a particular GitHub branch (e.g main)
~~~
apt-get update && apt-get install -y libsndfile1 ffmpeg
pip install Cython
python -m pip install git+https://github.com/NVIDIA/NeMo.git@{BRANCH}#egg=nemo_toolkit[all]
~~~

RNNT

Note that RNNT requires numba to be installed from conda.
~~~
conda remove numba
pip uninstall numba
conda install -c conda-forge numba
~~~
Nemo Megatron

Nemo Megatron training requires NVIDIA Apex to be installed.
Install it manually if not using the NVIDIA PyTorch container.
~~~
git clone https://github.com/NVIDIA/apex.git
cd apex
git checkout 57057e2fcf1c084c0fcc818f55c0ff6ea1b24ae2
    pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" --global-option="--fast_layer_norm" --global-option="--distributed_adam" --global-option="--deprecated_fused_adam" ./
~~~

cuda-nvprof is needed to install Apex. The version should match the CUDA version that you are using:
~~~
conda install -c nvidia cuda-nvprof=11.8
pip install packaging
~~~

## Training
for training follow the code 
`ASR_CTC_Language_Finetuning`

## inference
for training follow the code 
`Offline_ASR`