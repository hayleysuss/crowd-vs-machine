### data/directory
- Raw input: csv (taken from https://www.kaggle.com/ericpierce/austinhousingprices) of house listings and associated features (including Zillow ID, price, square footage...), where each home occupies one row in the CSV. This data will be used to train the neural network and a subset of homes and features will be used in the HITs
- quality_aggregation_module: Python code to perform quality control and aggregation computations

#### Quality Control
A good guessed price was defined as one within 1 standard deviation of the guessed prices for a given home. Workers were assigned weights equal to the reciprocal of their average distance from the mean.

- QC_input: Sample input for quality control module, csv with sample data outputted by the MTurk HIT, including workerId and the home features the workers were presented with in the HIT
- QC1_ouptut: Sample output from our QC module (removal of bad results), csv with columns workerId (corresponding to the MTurk worker who completed the HIT), answerPrice (the worker's guess for the house), and zpid (Zillow ID of the home)
- QC2_output: csv with columns mapping workers to quality (their computed worker weight)

#### Aggregation
We aggregated by taking the mean of the good workers' answers as well as the weighted average accounting for worker weights.

- AG1_output: csv mapping house ID to the average over all good workers, using QC1_output as input
- AG2_output: csv mapping house ID to the weighted average over all workers, using qualities computed in QC2_output

