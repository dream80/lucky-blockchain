from enum import Enum


class ProtocolMessageTypes(Enum):
    # Shared protocol (all services)
    handshake = 1+6

    # Harvester protocol (harvester <-> farmer)
    harvester_handshake = 3+6
    # new_signage_point_harvester = 4 Changed to 66 in new protocol
    new_proof_of_space = 5+6
    request_signatures = 6+6
    respond_signatures = 7+6

    # Farmer protocol (farmer <-> full_node)
    new_signage_point = 8+6
    declare_proof_of_space = 9+6
    request_signed_values = 10+6
    signed_values = 11+6
    farming_info = 12+6

    # Timelord protocol (timelord <-> full_node)
    new_peak_timelord = 13+6
    new_unfinished_block_timelord = 14+6
    new_infusion_point_vdf = 15+6
    new_signage_point_vdf = 16+6
    new_end_of_sub_slot_vdf = 17+6
    request_compact_proof_of_time = 18+6
    respond_compact_proof_of_time = 19+6

    # Full node protocol (full_node <-> full_node)
    new_peak = 20+6
    new_transaction = 21+6
    request_transaction = 22+6
    respond_transaction = 23+6
    request_proof_of_weight = 24+6
    respond_proof_of_weight = 25+6
    request_block = 26+6
    respond_block = 27+6
    reject_block = 28+6
    request_blocks = 29+6
    respond_blocks = 30+6
    reject_blocks = 31+6
    new_unfinished_block = 32+6
    request_unfinished_block = 33+6
    respond_unfinished_block = 34+6
    new_signage_point_or_end_of_sub_slot = 35+6
    request_signage_point_or_end_of_sub_slot = 36+6
    respond_signage_point = 37+6
    respond_end_of_sub_slot = 38+6
    request_mempool_transactions = 39+6
    request_compact_vdf = 40+6
    respond_compact_vdf = 41+6
    new_compact_vdf = 42+6
    request_peers = 43+6
    respond_peers = 44+6

    # Wallet protocol (wallet <-> full_node)
    request_puzzle_solution = 45+6
    respond_puzzle_solution = 46+6
    reject_puzzle_solution = 47+6
    send_transaction = 48+6
    transaction_ack = 49+6
    new_peak_wallet = 50+6
    request_block_header = 51+6
    respond_block_header = 52+6
    reject_header_request = 53+6
    request_removals = 54+6
    respond_removals = 55+6
    reject_removals_request = 56+6
    request_additions = 57+6
    respond_additions = 58+6
    reject_additions_request = 59+6
    request_header_blocks = 60+6
    reject_header_blocks = 61+6
    respond_header_blocks = 62+6

    # Introducer protocol (introducer <-> full_node)
    request_peers_introducer = 63+6
    respond_peers_introducer = 64+6

    # Simulator protocol
    farm_new_block = 65+6

    # New harvester protocol
    new_signage_point_harvester = 66+6
    request_plots = 67+6
    respond_plots = 68+6
