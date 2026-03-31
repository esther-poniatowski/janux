# Installation

## Prerequisites

- Python >= 3.12
- conda (recommended) or pip

## Using pip

The package installs directly from the GitHub repository:

```sh
pip install git+https://github.com/esther-poniatowski/janux.git
```

## Using conda

The package is available on the `eresthanaconda` channel:

```sh
conda install -c eresthanaconda janux
```

## From Source

1. Clone the repository:

   ```sh
   git clone https://github.com/esther-poniatowski/janux.git
   ```

2. Create a dedicated environment and install:

   ```sh
   cd janux
   conda env create -f environment.yml
   conda activate janux
   ```
