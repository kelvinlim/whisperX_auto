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
```
./run_whisperx_gpu  7653.86s user 1066.49s system 549% cpu 26:26.58 total
```