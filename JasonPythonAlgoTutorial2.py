import base64
import json
import time

import OpenFDA_food_json_results
from algosdk import algod, mnemonic, transaction


def wait_for_confirmation(algod_client, txid):
    last_round = algod_client.status().get('lastRound')
    while True:
        txinfo = algod_client.pending_transaction_info(txid)
        if txinfo.get('round') and txinfo.get('round') > 0:
            print("Transaction {} confirmed in round {}.".format(
                txid, txinfo.get('round')))
            break
        else:
            print("Waiting for confirmation...")
            last_round += 1
            algod_client.status_after_block(last_round)


def send_note():
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    passphrase = "neglect struggle demand unfold knee salute mechanic enlist tray mind outside topple garage antique invest narrow gesture cat mouse solid slight myself favorite about raw"

    private_key = mnemonic.to_private_key(passphrase)
    my_address = mnemonic.to_public_key(passphrase)
    print("My address: {}".format(my_address))

    params = algod_client.suggested_params()
    note = OpenFDA_food_json_results.results_json_1.encode()
    receiver = "GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A"

    data = {
        "sender": my_address,
        "receiver": receiver,
        "fee": params.get('minFee'),
        "flat_fee": True,
        "amt": 0,
        "first": params.get('lastRound'),
        "last": params.get('lastRound') + 1000,
        "note": note,
        "gen": params.get('genesisID'),
        "gh": params.get('genesishashb64')
    }

    txn = transaction.PaymentTxn(**data)
    signed_txn = txn.sign(private_key)
    txid = signed_txn.transaction.get_txid()
    print("Signed transaction with txID: {}".format(txid))

    algod_client.send_transaction(signed_txn)

    # wait for confirmation
    wait_for_confirmation(algod_client, txid)

    try:
        confirmed_txn = algod_client.transaction_info(my_address, txid)
    except Exception as err:
        print(err)
    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn.get('noteb64')).decode()))
    person_dict = json.loads(base64.b64decode(
        confirmed_txn.get('noteb64')).decode())
    # print(person_dict['firstName'])


send_note()
