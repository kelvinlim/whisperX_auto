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