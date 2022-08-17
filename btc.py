import blockcypher as by

def searchBTCbyHeight(number):
    temp = by.get_block_overview(number)
    height = temp.get('height')
    hash = temp.get('hash')
    bits = temp.get('bits')
    size = temp.get('size')
    fees = temp.get('fees')
    n_tx = temp.get('n_tx')
    return height,hash,bits,size,fees,n_tx


def searchBTCbyHash(hash):
    print(hash)
    temp = by.get_block_overview(hash)
    print(temp)
    height = temp.get('height')
    hash = temp.get('hash')
    bits = temp.get('bits')
    size = temp.get('size')
    fees = temp.get('fees')
    n_tx = temp.get('n_tx')
    return height,hash,bits,size,fees,n_tx

def searchBTCtransactionByHash(hash):
    temp = by.get_transaction_details(hash)
    block_hash = temp.get('block_hash')
    block_number = temp.get('block_height')
    confirmations = temp.get('confirmations')
    total = temp.get('total')
    size = temp.get('size')
    return block_hash,block_number,confirmations,total,size
    print()


print(searchBTCbyHash('f854aebae95150b379cc1187d848d58225f3c4157fe992bcd166f58bd5063449'))