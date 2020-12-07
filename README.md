# FDA_Recalls_Algorand

Python script to pull OpenFDA Data for Food_Recalls for the month of November 2020

Pull data into readable JSON Array

Encode JSON into uint8 array (if this is possible?)

Place Encoded uint8 array into txn note of TEAL program

Send a payment txn to receiver address

Use indexer from Algorand to find all transactions with Food_Recalls

Future implementations

1. Decentralize the python script location and FDA data storage before Algo txn
2. Add other Recalls such as drug recalls
