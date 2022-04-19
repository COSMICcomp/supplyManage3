from colorama import Fore
import time
print(Fore.BLUE + "Welcome to supplyManage3 by COSMOS")
print(Fore.BLUE + "Type 'help' to view all commands.\n")
initcmd = input(Fore.RED + "$$: ")
chain = ''
axad = ''
while True:
  if initcmd == 'help':
    print(Fore.BLUE +
      "Welcome to supplyManage3 by COSMOS. In this program you can\n"
      "create 'chains' which simulate real supplyChains. Create a\n"
      "a chain by using the command 'chain'. Create a product in a\n"
      "chain by 'chain.pro'.\n"
      "More than one product can be added\n"
      "No More than one chain\n"
      "To export a chain: chain.export\n"
      "Get help to import a chain by help.import\n"
      "To return a product from a chain: find\n"
      "After import read it by: import.read\n"
      "To delete a product: del\n"
      "New product with a preset shipping and destination: pro.help"
      "To list all in CMD: display"
    )
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == 'chain':
    chainame = input("Name of Chain: ")
    chain = chainame.strip()
    chains = []
    chainprod = []
    chaintype = []
    chaindesti = []
    chains.append(chain)
    print("Chain {} has been generated.".format(chain))
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == '{}.pro'.format(chain):
    prodname = input(Fore.GREEN + "What is the name of the product: ")
    chainprod.append(prodname)
    prodtype = input(Fore.GREEN + "What is the shipping type of product: ")
    chaintype.append(prodtype)
    proddesti = input(Fore.GREEN + "What is the final place of product: ")
    chaindesti.append(proddesti)
    print(Fore.GREEN + f"Product {prodname} is created.")
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == f'{chain}.export':
    print(Fore.CYAN + 'Exporting Chain into a data file.')
    time.sleep(2)
    textfile = open("data.txt", "w")
    for element in chainprod, chaintype, chaindesti:
      textfile.write(str(element) + '\n')
    textfile.close()
    print(Fore.GREEN + 'Done.')
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == 'help.import':
    print("To import, make sure that the data that\n")
    print("was exported through supplyManage commands\n")
    print("untouched. Use import to get started\n")
    print("If import works, then instance will end.")
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == 'import':
    try:
      with open('data.txt', 'r') as filetype:
        a = filetype.read()
        print(a)
        g = True
        lines = filetype.readlines()
        initcmd = input(Fore.RED + "$$: ")      
    except FileNotFoundError:
      print("No exported data file found.")
      g = False
      initcmd = input(Fore.RED + "$$: ")
  elif initcmd == 'find':
    askprx = input(Fore.CYAN + "Name of Product: ").strip()
    if askprx in chainprod:
      res = chainprod.index(askprx)
      type = chaintype[res]
      desti = chaindesti[res]
      print(f"The product {askprx} was found")
      print("The shipping type is " + str(type))
      print("The destination is " + str(desti))
      initcmd = input(Fore.RED + "$$: ")
    else:
      print("Not Found")
      initcmd = input(Fore.RED + "$$: ")
  elif initcmd == 'import.read':
    if g == True:
      print(*a)
      initcmd = input(Fore.RED + "$$: ")
    elif g == False:
      print("Not Found")
      initcmd = input(Fore.RED + "$$: ")
    else:
      print("Not Found")
      initcmd = input(Fore.RED + "$$: ")
  elif initcmd == 'del':
    watdn = input("Which product: ").strip()
    if watdn in chainprod:
      res = chainprod.index(watdn)
      type = chaintype[res]
      desti = chaindesti[res]
      del chaintype[res]
      del chaindesti[res]
      del chainprod[res]
      initcmd = input(Fore.RED + "$$: ")
    else:
      print("Not Found")
      initcmd = input(Fore.RED + "$$: ")
  elif initcmd == 'pro.help':
    print("You can preset a destination and shipping type with\n")
    print("the command: 'pro set'. Then to make product use chain.pro.setname")
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == 'pro set':
    settyep = []
    setname = []
    setdesi = []
    axad = input(Fore.GREEN + "Set Name: ")
    setname.append(axad)
    axaf = input(Fore.GREEN + "Destination: ")
    setdesi.append(axaf)
    axam = input(Fore.GREEN + "Shipping: ")
    settyep.append(axam)
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == f'{chain}.pro.{axad}':
    xprodname = input(Fore.GREEN + "What is the name of the product: ").strip()
    xres = setname.index(axad)
    xres2 = setdesi[xres]
    xres3 = settyep[xres]
    chainprod.append(xprodname)
    chaintype.append(xres2)
    chaindesti.append(xres3)
    initcmd = input(Fore.RED + "$$: ")
  elif initcmd == 'display':
    proxxi = chainprod[:10]  
    proxxii = chaintype[:10]  
    proxxioo = chaindesti[:10]  
    askifasspasm = int(input("Products, Shipping, or Destination(1, 2, 3): "))
    if askifasspasm == 1:
      print(proxxi)
      initcmd = input(Fore.RED + "$$: ")
    elif askifasspasm == 2:
      print(proxxii)
      initcmd = input(Fore.RED + "$$: ")
    elif askifasspasm == 3:
      print(proxxioo)
      initcmd = input(Fore.RED + "$$: ")
    else:
      print('Not Valid')
      initcmd = input(Fore.RED + "$$: ")
  elif initcmd == 'cosmos.des{all}':
    break
  elif ValueError:
    print("Not A Command! Try Again")
    initcmd = input(Fore.RED + "$$: ")