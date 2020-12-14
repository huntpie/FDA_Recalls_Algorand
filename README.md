# FDA_Recalls_Algorand

Python script to pull OpenFDA Data for Food_Recalls from Dec 1st to Dec 2nd 2020

- Parse metadata number to see how many results the API needs for the URL
- Remove 'event_id', 'openfda','initial_firm_notification', 'address_2' to compress note to less than 1KB
  -append a 4 byte prefix to JSON notefield

Use python sdk and a new python script to make a pay transaction contract

Use python sdk for indexer

-Use indexer to search for prefix

Future implementations

1. Decentralize the python script location and FDA data storage before Algo txn
2. Add other Recalls such as drug recalls

Jason's Help

TXN encoding

const enc = new TextEncoder();
const note = enc.encode(yourjson);

    let txn = algoSdk.makePaymentTxnWithSuggestedParams(
      myAccount.addr,
      receiver,
      100000,
      undefined,
      note,
      params
    );

Indexer search

const enc = new TextEncoder();
const note = enc.encode(yourjsondata);
const buff = Buffer.from(note).toString("base64");

    let txns = await algodIndexer
      .lookupAccountTransactions(id)
      .notePrefix(buff)
      .do();
