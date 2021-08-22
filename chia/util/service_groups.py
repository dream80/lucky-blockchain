from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "lucky_harvester lucky_timelord_launcher lucky_timelord lucky_farmer lucky_full_node lucky_wallet".split(),
    "node": "lucky_full_node".split(),
    "harvester": "lucky_harvester".split(),
    "farmer": "lucky_harvester lucky_farmer lucky_full_node lucky_wallet".split(),
    "farmer-no-wallet": "lucky_harvester lucky_farmer lucky_full_node".split(),
    "farmer-only": "lucky_farmer".split(),
    "timelord": "lucky_timelord_launcher lucky_timelord lucky_full_node".split(),
    "timelord-only": "lucky_timelord".split(),
    "timelord-launcher-only": "lucky_timelord_launcher".split(),
    "wallet": "lucky_wallet lucky_full_node".split(),
    "wallet-only": "lucky_wallet".split(),
    "introducer": "lucky_introducer".split(),
    "simulator": "lucky_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
