from chia.util.ints import uint32, uint64
import  random

# 1 Chia coin = 1,000,000,000,000 = 1 trillion mojo.
_mojo_per_chia = 1000000000000
_blocks_per_year = 1681920   # 32 * 6 * 24 * 365
_blocks_per_month = 138240  # 32 * 6 * 24 * 30

#贯穿整个区块链的幸运奖励
def  lucky_reward(height):   
    strs = str(height)
    n=0
    last_one=strs[-1:]
    last_two=strs[-2:]
    last_three=strs[-3:]
    
    #if lucky_rand():
    #    n=999
    if last_three == '666':
        n=666
    elif last_two =='66' :
        n=66
    elif last_one == '6':
        n=6
    else:
        n=0
    return n



# 区块彩蛋奖励，大概每周一爆，每次固定999！
def lucky_rand():
    if random.randint(1,32256)==666:
        return True
    else :
        return False


def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    if height == 0:
        return uint64(int((1 / 3) * 1 * _mojo_per_chia))
    elif height==1:
        return uint64(int((1 / 3) * 666666 * _mojo_per_chia))
    elif height<1 * _blocks_per_month:
        return uint64(int((1 / 3) * 18 * _mojo_per_chia))
    elif height < 3 * _blocks_per_year:
        return uint64(int((1 / 3) * 6 * _mojo_per_chia))
    elif height < 6 * _blocks_per_year:
        return uint64(int((1 / 3) * 3 * _mojo_per_chia))
    elif height < 9 * _blocks_per_year:
        return uint64(int((1 / 3) * 1.5 * _mojo_per_chia))
    elif height < 12 * _blocks_per_year:
        return uint64(int((1 / 3) * 0.75 * _mojo_per_chia))
    else:
        return uint64(int((1 / 3) * 0.375 * _mojo_per_chia))

def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """
    luckycoin=lucky_reward(height) 

    if height == 0:
        return uint64(int((2 / 3) * 1 * _mojo_per_chia))
    elif height==1:
        return uint64(int((2 / 3) * 666666 * _mojo_per_chia))
    elif luckycoin != 0:
        return uint64(int((3 / 3) * luckycoin * _mojo_per_chia)) 
    elif height<1 * _blocks_per_month:
        return uint64(int((2 / 3) * 18 * _mojo_per_chia))
    elif height < 3 * _blocks_per_year:
        return uint64(int((2 / 3) * 6 * _mojo_per_chia))
    elif height < 6 * _blocks_per_year:
        return uint64(int((2 / 3) * 3 * _mojo_per_chia))
    elif height < 9 * _blocks_per_year:
        return uint64(int((2 / 3) * 1.5 * _mojo_per_chia))
    elif height < 12 * _blocks_per_year:
        return uint64(int((2 / 3) * 0.75 * _mojo_per_chia))
    else:
        return uint64(int((2 / 3) * 0.375 * _mojo_per_chia))

