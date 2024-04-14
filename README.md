# A Data Analysis Model Mainly Based on Neural Network
- **structure**:
  - Discover\
    - some codes to discover the data
  - NN\
    - main codes for NN defination, training and tuning
  - Process\
    - some codes to process the raw data
- NN\
  - DataSet: *load the data*
  - DataLoader: *prepare the data for training*
  - NnStruture: *define the network*
  - NnTrain: *train the network*
  - HyperTuning: *tuning the network(using optuna)*
  - storageLinkTemplate: *the database URL template for optuna*

# IMPORTANT
remember set you **own** database URL in `storageLinkTemplate.txt` and **change the name** of it to `storageLink.txt` after set the your own database URL, this file will be ignored in .gitignore to protect you database from leak