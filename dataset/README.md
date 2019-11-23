# Dataset

For each experiment one HDF5 file is created. 
And each file contains the following Groups:

HDF Group 1: **lidar**

- Contains the LiDAR Point Cloud (X, Y, and Z) and the
coordinate reference is the World.
- The number of points (N) depends on the settings of the LiDAR sensor

Datasets descriptions:
| Dataset Name  |       Data Format: matrix float32 (N points, 3 columns)    |
|----------|:-------------:|
| timestamp 1 |  x0, y0, z0, ... xN, yN, zN |
| timestamp 2 |  x0, y0, z0, ... xN, yN, zN |
| timestamp FRAME_COUNT |  x0, y0, z0, ... xN, yN, zN |

Group Attributes description:
| Attributes  |   Description    |
|----------|:-------------:|
| LIDAR_CHANNELS | Number of channels used in the LiDAR |
| LIDAR_RANGE | Maximum range of the LiDAR sensor  |
| LIDAR_SETTINGS | ... |
| FRAME_COUNT | Number of Frames in the dataset  |


HDF Group 2: **imageX**

Multiple cameras can be setted up
- Contains the RGB Images of a X camera
- For each camera there is transformation to match with the point clouds

Datasets descriptions:

| Dataset Name  |       Data Format: matrix uint8 (height, width, 3)    |
|----------|:-------------:|
| timestamp 1 |  image (w,h,3) |
| timestamp 2 |  image (w,h,3) |


HDF Group 3: **bouding box**

Multiple cameras can be setted up
- Contains the RGB Images of a X camera
- For each camera there is transformation to match with the point clouds

Datasets descriptions:

| Dataset Name  |       Data Format: matrix uint8 (height, width, 3)    |
|----------|:-------------:|
| timestamp 1 |  image (w,h,3) |
| timestamp 2 |  image (w,h,3) |


HDF Group 3: **gnss**

Multiple cameras can be setted up
- Contains the RGB Images of a X camera
- For each camera there is transformation to match with the point clouds

Datasets descriptions:
| Dataset Name  |       Data Format: matrix uint8 (height, width, 3)    |
|----------|:-------------:|
| timestamp 1 |  image (w,h,3) |
| timestamp 2 |  image (w,h,3) |