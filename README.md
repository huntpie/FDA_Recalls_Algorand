# FDA_Recalls_Algorand

Python script to pull OpenFDA Data for Food_Recalls for December 1st.

Break results JSON data in half to fit in 1KB of Algo notefield

Label first half of data

Use python sdk to encode data into txn

Label second half of data

Encode JSON into uint8 array (if this is possible?)

Place Encoded uint8 array into txn note of TEAL program

Send a payment txn to receiver address

Use indexer from Algorand to find all transactions with "FDA Food Recalls" string in notefield

Future implementations

1. Decentralize the python script location and FDA data storage before Algo txn
2. Add other Recalls such as drug recalls
