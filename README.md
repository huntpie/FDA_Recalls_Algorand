# FDA_Recalls_Algorand

Python script to pull OpenFDA Data for Food_Recalls from Dec 1st to Dec 2nd 2020

- Parse metadata number to see how many results the APi does
- Break results JSON data in half to fit in 1KB of Algo notefield
- Label first half of data with - Label second half of data

Use python sdk and a new python script to make a pay transaction contract

-Place DataExtraction first json_results variable into notefield

Use python sdk for indexer

-Use indexer to search for prefix

Future implementations

1. Decentralize the python script location and FDA data storage before Algo txn
2. Add other Recalls such as drug recalls
