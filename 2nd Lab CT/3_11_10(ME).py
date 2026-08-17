from bitcoinlib.transactions import Transaction, Output
from bitcoinlib.keys import Key

print("BITCOIN TRANSACTION SIGNING")
print("=" * 40)

SIGHASH_ALL = 1

key = Key()

tx = Transaction()

prev_txid = "1" * 64

tx.add_input(
    prev_txid=prev_txid,
    output_n=0,
    keys=key.public(),
    value=110000
)

receiver = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"

amount = 100000

tx.add_output(
    value=amount,
    address=receiver
)

signature_hash = tx.signature_hash(
    sign_id=0,
    hash_type=SIGHASH_ALL
)

tx.sign(
    key.private_byte,
    index_n=0,
    hash_type=SIGHASH_ALL
)

print("\nTransaction Details")
print("-------------------")
print("Receiver :", receiver)
print("Amount   :", amount, "satoshi")
print("SIGHASH  : SIGHASH_ALL (1)")

print("\nSignature Hash")
print(signature_hash.hex())

print("\nSigned Transaction Hex")
print(tx.raw_hex())

print("\nTransaction Verified")
print(tx.verify())

