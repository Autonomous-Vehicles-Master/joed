# Data Fusion and Multi-Task Learning

This project intends to study the Data Fusion and Multi-Task Learning
applied to the detection of danger situations during drive.

The project is divided in three parts:
1. Dataset Generation:
    - Uses CARLA simulator to generate the dataset
2. Opponent Detection
    - Convolutional Neural Networks
3. Situation Evaluation
    - Based on the opponent detection, car position

## Requirements

- Python3 and libraries
- Tensorflow 2.0 and PyTorch
- Carla Simulator 9.6.0+

Install python libraries:
```bash
python3 -m install pyqtgraph pygame matplotlib h5py opencv-python future numpy jupyter PyQt5 open3d
```

## 1. Dataset Generation

### Carla Simulator Setup

Carla Simulator is used to generate the dataset to train and test the network models.

Download and install:
```bash
mkdir -p simulator/carla
cd simulator/carla
wget http://carla-assets-internal.s3.amazonaws.com/Releases/Linux/CARLA_0.9.6.tar.gz
tar -xf CARLA_0.9.6.tar.gz
```

### Python scripts for data generation



### Generating Data

**Start Carla:**

```bash
./CarlaUE4.sh
```

One LiDAR sensor and 1-4 cameras are set up in the EGO vehicle.

**Run Scripts:**

```bash
cd scripts
python3 dataset_generation.py
```

The data generated will be stored on the **"./dataset"** folder.


