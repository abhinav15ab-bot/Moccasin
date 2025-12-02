

 
from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network


def deploy_favorites() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    starting_number: int = favorites_contract.retrieve()
    print(f"Starting number is: {starting_number}")

    favorites_contract.store(77)
    ending_number: int = favorites_contract.retrieve()
    print(f"Ending number is: {ending_number}")
    # time.sleep(3)
    return favorites_contract
def moccasin_main() -> VyperContract:
    return deploy_favorites()


if __name__ == "__main__":
    moccasin_main() 
# from src import favorites
# from moccasin.boa_tools import VyperContract
# from moccasin.config import get_active_network


# def deploy_favorites() -> VyperContract:
#     active_network = get_active_network()
#     print("Currently on network: ", active_network.name)

#     favorites_contract: VyperContract = favorites.deploy()
#     print("Starting favorite number: ", favorites_contract.retrieve().call()
# )
#     favorites_contract.store(77)
#     print("Ending favorite number: ", favorites_contract.retrieve().call()
# )

#     if active_network.has_explorer():
#         print("Verifying contract on explorer...")
#         result = active_network.moccasin_verify(favorites_contract.retrieve().call()
# )
#         result.wait_for_verification()
#     return favorites_contract.retrieve().call()



# def moccasin_main() -> VyperContract:
#     return deploy_favorites()

# from src import favorites
# from moccasin.boa_tools import VyperContract
# from moccasin.config import get_active_network


# def deploy_favorites() -> VyperContract:
#     active_network = get_active_network()
#     print("Currently on network:", active_network.name)

#     # Deploy contract
#     favorites_contract: VyperContract = favorites.deploy()

#     # READ VALUES (NO .call() ON ZKSYNC)
#     starting_number = favorites_contract.retrieve()
#     print("Starting favorite number:", starting_number)

#     # WRITE VALUE
#     favorites_contract.store(77)

#     ending_number = favorites_contract.retrieve()
#     print("Ending favorite number:", ending_number)

#     # Verification (NO .call())
#     if active_network.has_explorer():
#         print("Verifying contract on explorer...")
#         result = active_network.moccasin_verify(favorites_contract)
#         result.wait_for_verification()

#     return favorites_contract


# def moccasin_main() -> VyperContract:
#     return deploy_favorites()
