import os
import time
import zipfile
import datetime
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_data_formatada():
    return datetime.datetime.now().strftime('%d%m%y')


def iniciar_navegador():
    return webdriver.Edge()  #  -Removendo a opção headless para garantir que abra


def login_apache():
    pyautogui.typewrite("projetopw")
    pyautogui.press("tab")
    pyautogui.typewrite("GArrafa#20")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(1)


def login_php(navegador):
    time.sleep(2)  # Aguarda antes de interagir com a página
    navegador.find_element(By.ID, "input_username").send_keys("elton.oliveira")
    navegador.find_element(By.ID, "input_password").send_keys("Conan32@")
    navegador.find_element(By.ID, "input_go").click()


def exportar_banco(navegador, wait, banco):
    print(f"Exportando {banco}.sql...")
    url = f'http://192.168.50.253/phpmyadmin/index.php?route=/database/export&db={banco}'
    navegador.get(url)
    wait.until(EC.element_to_be_clickable((By.ID, "buttonGo"))).click()
    time.sleep(0.1)


def compactar_arquivos(arquivos, destino_zip):
    print("Zipando arquivos...")
    with zipfile.ZipFile(destino_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos:
            if os.path.exists(arquivo):
                zipf.write(arquivo, os.path.basename(arquivo))
                print(f"Comprimindo {os.path.basename(arquivo)}...")
    print("\nTodos os arquivos foram comprimidos com sucesso!")


def excluir_arquivos(arquivos):
    print("\nExcluindo arquivos da pasta de download...")
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            os.remove(arquivo)
            print(f"{arquivo} foi apagado.")
        else:
            print(f"O arquivo {arquivo} não foi encontrado...")


def main():
    data_formatada = get_data_formatada()
    navegador = iniciar_navegador()
    wait = WebDriverWait(navegador, 60)

    navegador.get('http://192.168.50.253/phpmyadmin/index.php?route=/')
    login_apache()
    login_php(navegador)

    bancos = ["information_schema", "mysql", "performance_schema", "PW", "sys"]
    for banco in bancos:
        exportar_banco(navegador, wait, banco)

    time.sleep(10)
    navegador.quit()

    arquivos_sql = [rf"C:\Users\elton.oliveira\Downloads\{banco}.sql" for banco in bancos]
    nome_arquivo_zip = rf"C:\Users\elton.oliveira\Documents\Export Automacoes\Backup_PHP\PW-{data_formatada}.zip"
    compactar_arquivos(arquivos_sql, nome_arquivo_zip)
    excluir_arquivos(arquivos_sql)

    print("\nPROCESSO FINALIZADO!")
    print(f"ARQUIVO ZIPADO SALVO EM: {nome_arquivo_zip}")
    time.sleep(1)


if __name__ == "__main__":
    main()