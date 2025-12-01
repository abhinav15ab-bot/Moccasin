from src import favorites

 
def deploy():
    favorites_contract = favorites.deploy()
    starting_number = favorites_contract.retrieve()
    print(f"Starting favorite number is: {starting_number}")
    # breakpoint()
    # print("hi")

def moccasin_main():
    deploy()


# if __name__ == "__main__":
#     moccasin_main()