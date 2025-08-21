import os
import time
import zipfile
import datetime
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime('%d%m%y')

# Configurando as opções do navegador
navegador = webdriver.Edge()

# Abre a página da web onde você deseja preencher os campos de texto
navegador.get('http://192.168.50.12/phpmyadmin/index.php?route=/')

#logar no apache
pyautogui.typewrite("projetopw")
pyautogui.press("tab")
pyautogui.typewrite("GArrafa#20")
time.sleep(0.1)
pyautogui.press("enter")
time.sleep(1)

#logar no php
navegador.find_element(By.XPATH, '//*[@id="input_username"]').send_keys("elton.oliveira")
navegador.find_element(By.XPATH, '//*[@id="input_password"]').send_keys("Conan32@")
navegador.find_element(By.XPATH, '//*[@id="input_go"]').click()

#iniciar backup
time.sleep(1)
wait = WebDriverWait(navegador, timeout=60)

print("Exportando information_schema.sql...")
navegador.get('http://192.168.50.12/phpmyadmin/index.php?route=/database/export&db=information_schema')
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonGo"]'))).click()
time.sleep(0.1)

print("Exportando mysql.sql...")
navegador.get('http://192.168.50.12/phpmyadmin/index.php?route=/database/export&db=mysql')
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonGo"]'))).click()
time.sleep(0.1)

print("Exportando performance_schema.sql...")
navegador.get('http://192.168.50.12/phpmyadmin/index.php?route=/database/export&db=performance_schema')
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonGo"]'))).click()
time.sleep(0.1)

print("Exportando siscomex.sql...")
navegador.get('http://192.168.50.12/phpmyadmin/index.php?route=/database/export&db=siscomex')
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonGo"]'))).click()
time.sleep(0.1)

print("Exportando sys.sql...\n")
navegador.get('http://192.168.50.12/phpmyadmin/index.php?route=/database/export&db=sys')
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonGo"]'))).click()
time.sleep(0.1)

time.sleep(10)

# Fechando o navegador
navegador.quit()


arquivos_para_compressao = [r"C:\Users\elton.oliveira\Downloads\sys.sql",
                            r"C:\Users\elton.oliveira\Downloads\siscomex.sql",
                            r"C:\Users\elton.oliveira\Downloads\performance_schema.sql",
                            r"C:\Users\elton.oliveira\Downloads\mysql.sql",
                            r"C:\Users\elton.oliveira\Downloads\information_schema.sql"]

# Nome do arquivo ZIP de saída
print("Zipando arquivos...\n")
nome_arquivo_zip = r"C:\Users\elton.oliveira\Documents\Export Automacoes\Backup_PHP\API SISCOMEX-" + data_formatada + ".zip"

# Abra um arquivo ZIP em modo de escrita
with zipfile.ZipFile(nome_arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as meu_arquivo_zip:
    for arquivo in arquivos_para_compressao:
        # Determine o nome do arquivo no arquivo ZIP, sem os diretórios
        nome_arquivo_zip = os.path.basename(arquivo)
        meu_arquivo_zip.write(arquivo, nome_arquivo_zip)
        print("Comprimindo " + nome_arquivo_zip + "...")

print( f'\nTodos os arquivos foram comprimidos com sucesso!\n')

time.sleep(2)

print("\n Excluindo arquivos da pasta de download\n")

# Lista de caminhos para os 5 arquivos a serem apagados
arquivos_a_apagar = [r"C:\Users\elton.oliveira\Downloads\sys.sql",
                     r"C:\Users\elton.oliveira\Downloads\siscomex.sql",
                     r"C:\Users\elton.oliveira\Downloads\performance_schema.sql",
                     r"C:\Users\elton.oliveira\Downloads\mysql.sql",
                     r"C:\Users\elton.oliveira\Downloads\information_schema.sql"
                     ]

for caminho_arquivo in arquivos_a_apagar:
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
        print(f'{caminho_arquivo} foi apagado.')
    else:
        print(f'O arquivo {caminho_arquivo} não foi encontrado.')

print("\n PROCESSO FINALIZADO!\n")
print(r"ARQUIVO ZIPADO SALVO EM: C:\Users\elton.oliveira\PycharmProjects\relatorioAcessoEmail\download")

time.sleep(1)