#!/usr/bin/python3
import string, sys, zipfile, os.path
from tqdm import tqdm

if len(sys.argv) < 3:
    print("Número incorreto de argumentos!")
    sys.exit(0)

#Verificar se os ficheiros existem
zip_file = sys.argv[1]
lista_passwords = sys.argv[2]

if os.path.exists(zip_file) == False:
    print("\nFicheiro zip " + zip_file + " não encontrado")
    sys.exit(0) 

if os.path.exists(lista_passwords) == False:
    print("\nFicheiro de senha " + lista_passwords + " não encontrado")
    sys.exit(0) 


ficheiro_zipado = zipfile.ZipFile(zip_file)
n_palavras = len(list(open(lista_passwords, "rb")))
print("Total passwords para testar:", n_palavras)


with open (lista_passwords, "rb") as lista_passwords:
    for word in tqdm(lista_passwords, total = n_palavras, unit=" word "):
        word = word.strip()
        try:
            ficheiro_zipado.extractall(pwd=word)
        except zipfile.BadZipFile:
            print ("Ocorreu um erro a abrir o ficheiro")
            sys.exit(0)
        except zipfile.LargeZipFile:
            print ("Ficheiro zip demasiado grande")
            sys.exit(0)
        except Exception as Erro:
            if "Senha inválida para o ficheiro!" in str(Erro):
                pass
            elif "Erro -3 ao descomprimir o ficheiro" in str(Erro):
                pass
            else:
                pass
        except KeyboardInterrupt:
                print("Programa terminado a pedido do utilizador!")
                sys.exit()
        else:
            print("Password encontrada! A password é:", word.decode())
            sys.exit(0)

print("[!] Senha não encontrada, tente outra lista de senhas.")

