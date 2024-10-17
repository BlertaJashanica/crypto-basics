from secretsharing import SecretSharer


shares = [
    "2-44b39e6ed7d54fa9eda31f14474428b11fb19a007da5879854d23ed5f1d3f96c",  # Share 2
    "3-1ebf4af3faec539fd9bf6b8b2727e72cdac931ccb76ff9a4bf744cc3da0aeafd"   # Share 3
]


recovered_key_hex = SecretSharer.recover_secret(shares)


recovered_key = bytes.fromhex(recovered_key_hex)
print(f"Gereconstrueerde sleutel: {recovered_key.hex()}")
