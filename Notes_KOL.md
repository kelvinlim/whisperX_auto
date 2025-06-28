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