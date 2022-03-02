# Thermal Imagery Processing

This project is part of a Research Assistantship program with the Computer Science Department at the [College of Charleston](https://cofc.edu), in the Data Mining & Connectivity (DMC) Research Lab.

The image processing model investigates the relationship between satellite images collected by [Landsat 8](https://www.usgs.gov/landsat-missions/landsat-8) and drone images collected with a [DJI Mavic 2 Enterprise Dual](https://www.dji.com/mavic-2-enterprise). 

## Requirements

The project runs on a [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

To start an environment from the [environment.yml](https://github.com/bksrocks/Cofc-Research/blob/main/environment.yml):

1. You can follow the steps on how to configure conda from its [documentation](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#starting-conda).
2. Once inside the terminal shell, go to the directory containing the environment.yml file and use the following command:
```
conda env create -f environment.yml
```
3. To activate the environment use:
```
conda activate myenv
```
4. To verify that the environment was installed correctly use:
```
conda env list
```

For more information on managing conda environments refer to [documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).

You can use the [requirements.txt](https://github.com/bksrocks/Cofc-Research/blob/main/requirements.txt) file to start a virtual environment using pip, but conda is recommended due to some library compatibilities.

System requirements include:
- Git;
- Python 3.8;

## Usage

The project contain three main files:
- **[dji_imgread.py](https://github.com/bksrocks/Cofc-Research/blob/main/dji_imgread.py)** for pre-processing drone imagery; 
- **[lsat_imgread.py](https://github.com/bksrocks/Cofc-Research/blob/main/lsat_imgread.py)** for pre-processing satellite imagery;
- **[image_comparison.py](https://github.com/bksrocks/Cofc-Research/blob/main/image_comparisson.py)** for comparing drone and satellite images.

 

## Credits
[Barbara Szwabowski](https://github.com/bksrocks) in collaboration with [Dr. Navid Hashemi](https://github.com/navid-hashemi).
