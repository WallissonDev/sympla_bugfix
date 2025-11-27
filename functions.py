import psutil
import time
import os
import subprocess

def listar_processos():
    """Lista todos os processos em execução"""
    print("==== Processo em Execução====")
    for processo in psutil.process_iter(['pid', 'name']):
        print(f"PID: {processo.info["pid"]} | Nome: {processo.info['name']}")

def fechar_processo_por_nome(nome_processo):
    """
    Fecha um processo pelo nome
    nome_processo: string com o nome do processo (ex: 'notepad.exe')
    :param nome_processo:
    """
    try:
        processos_fechados = 0

        # Percorre todos os processos
        for processo in psutil.process_iter(['pid', 'name']):
            # Verifica se o nome do processo corresponde
            if processo.info['name'].lower() == nome_processo.lower():
                try:
                    print(f"Fechando processo: {processo.info['name']} PID: {processo.info['pid']}")
                    # Encerra o processo
                    processo.terminate()
                    # Aguarda o processo fechar
                    processo.wait(timeout=3)
                    print("Processo fechado com sucesso!")
                except psutil.NoSuchProcess:
                    print("Processo já foi fechado!")
                except psutil.AccessDenied:
                    print("Permissão negada para fechar o Processo")
                except psutil.TimeoutExpired:
                    print("Timeout - Processo não fechou a tempo")
    except Exception as e:
        print(f"Erro inesperado! -> {e}")

def abrir_programa():
    caminho_absoluto = "D:\Steam\steam.exe"
    if os.path.exists(caminho_absoluto):
        subprocess.Popen([caminho_absoluto])


