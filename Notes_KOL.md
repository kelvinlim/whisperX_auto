# Notes kolim

To export environment for the same os
```
conda env export > environment.yml
```

For Reproducibility Across Different Operating Systems 
```
conda env export --from-history > environment.yml
```

To create a new environment
```
conda env create -f environment.yml
```

## Timings

On mac studio Max2Ultra  

While you're running a _gpu script, the 549% cpu indicates that a significant portion of the work, or at least a large amount of parallelization, is still happening on the CPU. This is common with WhisperX, particularly for the diarization (speaker separation) step, which can be very CPU-intensive and often doesn't fully utilize the GPU even if it's available.

```
./run_whisperx_gpu  7653.86s user 1066.49s system 549% cpu 26:26.58 total
```

## On nvidia gpu 2070

```
ubuntu 2404

time ./run_whisperx_gpu 
ASR device: cuda
Diarization device: cuda
Alignment device: cuda
2025-07-23 06:37:47
===transcribe start
>>Performing voice activity detection using Pyannote...
Lightning automatically upgraded your loaded checkpoint from v1.5.4 to v2.5.2. To apply the upgrade to your files permanently, run `python -m pytorch_lightning.utilities.upgrade_checkpoint whisperx/assets/pytorch_model.bin`
Model was trained with pyannote.audio 0.0.1, yours is 3.3.2. Bad things might happen unless you revert pyannote.audio to 0.x.
Model was trained with torch 1.10.0+cu102, yours is 2.5.1. Bad things might happen unless you revert torch to 1.x.
/home/kolim/miniconda3/envs/whisperx_auto/lib/python3.12/site-packages/pyannote/audio/utils/reproducibility.py:74: ReproducibilityWarning: TensorFloat-32 (TF32) has been disabled as it might lead to reproducibility issues and lower accuracy.
It can be re-enabled by calling
   >>> import torch
   >>> torch.backends.cuda.matmul.allow_tf32 = True
   >>> torch.backends.cudnn.allow_tf32 = True
See https://github.com/pyannote/pyannote-audio/issues/1370 for more details.

  warnings.warn(
===transcribe end
2025-07-23 06:38:39
===align start
===align end
2025-07-23 06:39:08
===diarize start
/home/kolim/miniconda3/envs/whisperx_auto/lib/python3.12/site-packages/pyannote/audio/models/blocks/pooling.py:104: UserWarning: std(): degrees of freedom is <= 0. Correction should be strictly less than the reduction factor (input numel divided by output numel). (Triggered internally at /opt/conda/conda-bld/pytorch_1729647378361/work/aten/src/ATen/native/ReduceOps.cpp:1823.)
  std = sequences.std(dim=-1, correction=1)
===diarize end
2025-07-23 06:39:42

real    1m58.102s
user    1m56.834s
sys     0m10.631s



```

## On wsl with gtx1660

```
NVIDIA GeForce GTX 1660 

(whisperx_auto) kolim@DESKTOP-7KIDSEU:~/Projects/whisperX_auto$ time ./run_whisperx_gpu 
ASR device: cuda
Diarization device: cuda
Alignment device: cuda
2025-07-23 07:06:39
===transcribe start
>>Performing voice activity detection using Pyannote...
Lightning automatically upgraded your loaded checkpoint from v1.5.4 to v2.5.2. To apply the upgrade to your files permanently, run `python -m pytorch_lightning.utilities.upgrade_checkpoint whisperx/assets/pytorch_model.bin`
Model was trained with pyannote.audio 0.0.1, yours is 3.3.2. Bad things might happen unless you revert pyannote.audio to 0.x.
Model was trained with torch 1.10.0+cu102, yours is 2.5.1. Bad things might happen unless you revert torch to 1.x.
/home/kolim/anaconda3/envs/whisperx_auto/lib/python3.12/site-packages/pyannote/audio/utils/reproducibility.py:74: ReproducibilityWarning: TensorFloat-32 (TF32) has been disabled as it might lead to reproducibility issues and lower accuracy.
It can be re-enabled by calling
   >>> import torch
   >>> torch.backends.cuda.matmul.allow_tf32 = True
   >>> torch.backends.cudnn.allow_tf32 = True
See https://github.com/pyannote/pyannote-audio/issues/1370 for more details.

  warnings.warn(
===transcribe end
2025-07-23 07:08:02
===align start
===align end
2025-07-23 07:08:30
===diarize start
/home/kolim/anaconda3/envs/whisperx_auto/lib/python3.12/site-packages/pyannote/audio/models/blocks/pooling.py:104: UserWarning: std(): degrees of freedom is <= 0. Correction should be strictly less than the reduction factor (input numel divided by output numel). (Triggered internally at /opt/conda/conda-bld/pytorch_1729647378361/work/aten/src/ATen/native/ReduceOps.cpp:1823.)
  std = sequences.std(dim=-1, correction=1)
===diarize end
2025-07-23 07:10:25

real    3m50.282s
user    4m45.294s
sys     0m13.546s
(whisperx_auto) kolim@DESKTOP-7KIDSEU:~/Projects/whisperX_auto$ nvidia-smi
Wed Jul 23 07:11:00 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.35.02              Driver Version: 560.94         CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce GTX 1660        On  |   00000000:09:00.0  On |                  N/A |
| 40%   46C    P8             11W /  130W |     560MiB /   6144MiB |      1%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
(whisperx_auto) kolim@DESKTOP-7KIDSEU:~/Projects/whisperX_auto$ 

batchsize = 4
File produced is wrong!  All words are you in result['segments']

batchsize=16
CUDA failed with error out of memory

batch_size = 8 - all you

batch_size = 10
```