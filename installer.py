import apt, sys, os
from colorama import Fore, Style
import time

os.system("clear")
input("Bienvenue dans le script appuyez sur 'enter' pour continuer...")
while 1:
	print("Menu Principal		")
	print(Fore.GREEN + Style.DIM +"[1] Installation et configuration automatique des drivers pour AWUS036ACH")
	print(Fore.GREEN+"[2] Activation du mode Monitor" + Fore.RESET)
	print(Fore.GREEN+"[3] Désactivation du mode Monitor" + Fore.RESET)
	print(Fore.GREEN + "[4] Changer l'adresse MAC d'un interface" + Fore.RESET)
	choix = input(Fore.GREEN + Style.DIM + "Choisissez une option (1/5) " + Fore.RED + ">> " + Style.RESET_ALL + Fore.RESET)
	if int(choix) == 1:
		os.system("clear")
		realtek = "realtek-rtl88xxau-dkms"

		cache = apt.cache.Cache()
		cache.update()
		cache.open()

		rtl = cache[realtek]
		if rtl.is_installed:
			print('Le package est installé')
		else:
			print(Fore.GREEN + Style.DIM + "[+]Mise-à-jour APT en cours..." + Fore.RESET)
			os.system("apt-get update")
			os.system("clear")
			print(Fore.GREEN + Style.DIM + "Mise-à-jour terminée" + Fore.RESET)
			print(Fore.GREEN + Style.DIM + "Installation de " + realtek + "en cours !!" + Style.RESET)
			os.system("apt-get install " + realtek)

		netconf = open("/etc/NetworkManager/NetworkManager.conf")
		if "\n#Automatically writed by KaraxZoR\n[devices]\nunmanaged-devices=interface-name:wlan0" in netconf.read():
			print("Prochaine Étape !")
		else:
			file = open("/etc/NetworkManager/NetworkManager.conf", "a")
			file.write("\n#Automatically writed by KaraxZoR\n[devices]\nunmanaged-devices=interface-name:wlan0")
			file.close()
		netconf.close()

		print("Redémarrage du service 'NetworkManager' en cours...")
		os.system("service network-manager restart")
		os.system("clear")
		print(Fore.GREEN+Style.DIM+"[+]Tout semble correcte !"+Fore.RESET)
		leave = input("Souhaitez-vous quitter? (o/n)")
		if leave == "o":
			print(Fore.GREEN+"Au revoir !")
			break
		else:
			print(Fore.GREEN+"[+]Retour au menu principal")


	if int(choix) == 2:
		os.system("clear")
		while 1:
			carte = input(Fore.GREEN + Style.DIM + "[+]Entrez le nom de l'interface que vous souhaitez mettre en mode 'Monitor'\n[+]Entrez la Commande 'ifconfig' ou 'iwconfig' pour accéder aux interfaces\n"+ Fore.GREEN + Style.DIM +"Interface : " + Style.RESET_ALL)
			if carte == "ifconfig":
				os.system("ifconfig")
			elif carte == "iwconfig":
				os.system("iwconfig")
			else:
				os.system("clear")
				break
		print(Fore.GREEN+ Style.DIM +"[+]Activation du mode monitor sur " + carte+ " en cours..." + Style.RESET_ALL + Fore.RESET)
		os.system("ifconfig " + carte + " down")
		os.system("iwconfig " + carte + " mode monitor")
		os.system("ifconfig " + carte + " up")
		os.system("sleep 3.5s")
		print("Mode monitor activé sur " + carte)
		leave = input("Souhaitez-vous quitter? (o/n)")
		if leave == "o":
			print("Au revoir !")
			break
		else:
			print("Retour au menu principal")

	if int(choix) == 3:
		os.system("clear")
		while 1:
			carte = input(Fore.GREEN + Style.DIM + "[+]Entrez le nom de l'interface sur laquelle vous souhaitez désactiver le mode 'Monitor'\n[+]Entrez la Commande 'ifconfig' ou 'iwconfig' pour accéder aux interfaces\n"+ Fore.GREEN + Style.DIM +"Interface : " + Style.RESET_ALL)
			if carte == "ifconfig":
				os.system("ifconfig")
			elif carte == "iwconfig":
				os.system("iwconfig")
			else:
				os.system("clear")
				break
		print(Fore.GREEN+ Style.DIM +"Désactivation du mode monitor..." + Fore.RESET + Style.RESET_ALL)
		os.system("ipconfig " + carte + " down")
		os.system("iwconfig " + carte + " mode managed" )
		os.system("ipconfig " + carte + " up")
		os.system("sleep 3.5s")
		os.system("clear")
		print(Fore.GREEN + Style.DIM + "Mode monitor désactivé sur " + carte + " !!" + Fore.RESET + Style.RESET_ALL)
		os.system("sleep 3s")
		os.system("iwconfig")
		leave = input("Souhaitez-vous quitter? (o/n)")
		if leave == "o":
			print("Au revoir !")
			break
		else:
			print("Retour au menu principal")
	if int(choix) == 4:
		os.system("clear")
		while 1:
			print(Fore.GREEN + "Entrez la commande 'ifconfig' pour accéder à la liste des interfaces disponibles")
			print(Fore.GREEN + "Entrez la commande 'iwconfig' pour accéder à la liste des interfaces et leur mode actuel")
			print(Fore.GREEN + "Entrez la commande 'clear' pour nettoyer le contenu de la console")
			interface = input(Fore.GREEN + "[" + Fore.RED + "!" + Fore.GREEN +"]" + "Veuillez choisir un interface\n" + Fore.GREEN + "Interface" + Fore.RED + " >> " + Fore.RESET)
			if interface == "ifconfig":
				os.system("ifconfig")
			elif interface == "iwconfig":
				os.system("iwconfig")
			elif interface == "clear":
				os.system("clear")
			elif interface == "wlan0" or "wlan1" or "wlan2" or "wlan3" or "wlan4" or "eth0":
				os.system("clear")
				print(Fore.GREEN + "Votre adresse mac actuelle est :")
				os.system("cat /sys/class/net/" + interface + "/address")
				os.system("sleep 5")
				os.system("clear")
				print(Fore.GREEN+ Style.DIM + "Changement de l'adresse MAC en cours..." + Fore.RESET + Style.RESET_ALL)
				os.system("ifconfig wlan0 down")
				os.system("macchanger -r {0}".format(interface))
				os.system("ifconfig wlan0 up")
				os.system("sleep 3.2")
				os.system("clear")
				print(Fore.GREEN + "L'adresse MAC à été changée avec succès ! Voici votre nouvelle adresse : ")
				os.system("cat /sys/class/net/" + interface + "/address")
				os.system("sleep 5")
				os.system("clear")
				break
			else:
				print(Fore.RED + "[!] NOM DE L'INTERFACE INCONNUE PAR LE TOOL [!]" + "Le tool va quand même essayer de changer l'adresse MAC de l'interface")
				print(Fore.GREEN+ Style.DIM + "Changement de l'adresse MAC en cours..." + Fore.RESET + Style.RESET_ALL)
				os.system("ifconfig wlan0 down")
				os.system("macchanger -r {0}".format(interface))
				os.system("ifconfig wlan0 up")
				print(Fore.GREEN + "Voici votre nouvelle adresse MAC :")
				os.system("cat /sys/class/net/" + interface + "/address")
				os.system("sleep 5")
				os.system("clear")
				break
