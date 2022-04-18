from colorama import Fore
import time
print(Fore.BLUE + "Welcome to supplyManage3 by COSMOS")
print(Fore.BLUE + "Type .help to view all commands.\n")
initcmd = input(Fore.RED + "$$: ")

while True: 
  if initcmd == '.help':
    print(Fore.BLUE +
      "Welcome to supplyManage3 by COSMOS. In this program you can\n"
      "create 'chains' which simulate real supplyChains. Create a\n"
      "a chain by using the command '.chain'. Create a product in a\n"
      "chain by '.chain.pro'.\n"
      "More than one product and chain can be added\n"
      "To export a chain: .chain.exp\n"
      "Get help to import a chain by .help.imp"
    )
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == '.chain':
    chainame = input("Name of Chain: ")
    chain = chainame.strip()
    chains = []
    chainprod = []
    chaintype = []
    chaindesti = []
    chains.append(chain)
    print("Chain {} has been generated.".format(chain))
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == '.{}.pro'.format(chain):
    prodname = input(Fore.GREEN + "What is the name of the product: ")
    chainprod.append(prodname)
    prodtype = input(Fore.GREEN + "What is the shipping type of product: ")
    chaintype.append(prodtype)
    proddesti = input(Fore.GREEN + "What is the final place of product: ")
    chaindesti.append(proddesti)
    print(Fore.GREEN + f"Product {prodname} is created.")
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == f'.{chain}.exp':
    print(Fore.CYAN + 'Exporting Chain into a data file.')
    time.sleep(2)
    textfile = open("data.txt", "w")
    for element in chainprod, chaintype, chaindesti:
      textfile.write(str(element) + '\n')
    textfile.close()
    print(Fore.GREEN + 'Done.')
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == '.help.imp': 
    print("To import, make sure that the data that\n")
    print("was exported through supplyManage remains\n")
    print("untouched. Use .import to get started\n")
    print("If import works, then instance will end.")
  elif initcmd == '.import':
    try:
      with open('data.txt', 'r') as filetype:
        a = filetype.read()
        print(a)
    except FileNotFoundError:
      print("No exported data file found.")
      initcmd = input(Fore.RED + "$$: ")
