# WSDOT_TruckParking
Smart and Cooperative Truck Parking Monitoring and Calibration System Empowered by Machine Learning 
(FY 2021 High Priority Program – Innovative Technology Deployment Grant FM-MHP-21-2002)

## Update
(02/15) Test with multivariate
* *Truck_Parking_Prediction_DL-multivariate.ipynb*

(02/01) Modify Prediction algorithm
* *TruckParkingQuery_20220101_20220601.csv* real truck parking data from WisTransPortal
* *Truck_Parking_Prediction_DL-2_var.ipynb* well annotated prediction algorithm. Use 2 variables & yield the highest accuracy (l1 loss = 9.202)
* *Truck_Parking_Prediction_DL-3_var.ipynb* well annotated prediction algorithm. Use 3 variables (l1 loss = 16.068)
* *Truck_Parking_Prediction_DL-test_version.ipynb* another version of prediction algorithm *(ignore)*

~~(01/18) Modify *Truck_Parking_Prediction_DL.ipynb* (Not complete)~~

## Folder Structure
* code
  * **prediction_DL**: code for prediction using DL, in .py format (on-going)
  * **prediction_nph**: code for prediction using non-homogenous poisson, in .py format (COMPLETED)
  * *save_data.py*: code for pulling data from vendor's server in pilot project (COMPLETED)
* example
  * *save_data_example.ipynb*: A notebook for walking through process of pulling data from vendor's server in pilot project (COMPLETED)
  * **example_output**: output folder from save_data_example.ipynb (COMPLETED)
* DOCS
  * All related document (on-going)

## Reference for Prediction by using Deep Learning Method
H. Yang et al., "Truck Parking Pattern Aggregation and Availability Prediction by Deep Learning," in IEEE Transactions on Intelligent Transportation Systems, vol. 23, no. 8, pp. 12778-12789, Aug. 2022, doi: 10.1109/TITS.2021.3117290.
