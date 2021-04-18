# NETS213: Crowd vs Machine
## Contributors: Stefan Papazov, Nina Tansey, Hayley Sussman, Aidan Padala, Phillip Tchourioukanov
Repository for the NETS213 Final Project: Crowd vs Machine. This project aims to determine whether crowd wisdom or machine learning is more accurate in predicting home prices, specifically for homes in Austin, Texas.

### docs/directory
- Flow diagram outlining major components of the project
- Mockup of our HIT
- README outlining the major components of the project

### data/directory
- Raw input: csv (taken from https://www.kaggle.com/ericpierce/austinhousingprices) of house listings and associated features (including Zillow ID, price, square footage...), where each home occupies one row in the CSV. This data will be used to train the neural network and a subset of homes and features will be used in the HITs
- Sample input for QC module: csv with information outputted by the MTurk HIT, including workerId and the home features the workers were presented with in the HIT
- Sample output from our QC module: filtered csv with columns workerId (corresponding to the MTurk worker who completed the HIT), answerPrice (the worker's guess for the house), and zpid (Zillow ID of the home). Only those results within 80% of the actual home price were included.
- Sample input for aggregation module: output csv from QC module
- Sample output for aggregation module: csv containing the zpid for each home and average price over all results (filtered through QC module). These average prices will be compared to the machine learning predictions for the same houses to assess the accuracy of crowd wisdom.
