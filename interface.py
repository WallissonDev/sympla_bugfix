import tkinter as tk
from tkinter import messagebox
import sys
import os
import functions
import psutil

class MeuSoftware:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reset Sympla")
        self.root.geometry("500x300")
        # Criar os elementos da interface
        self.criar_interface()

    def criar_interface(self):
        # Botão 1
        btn1 = tk.Button(self.root, text="Procurar Processo",  command=self.funcao1, width=20, height=2 )
        btn1.pack(pady=10)

        #Botão 2
        btn2 = tk.Button(self.root, text="Fechar Processo", command=self.funcao2, width=20, height=2)
        btn2.pack(pady=10)

        #Botão 3
        btn3 = tk.Button(self.root, text="Abrir Programa", command=self.funcao3, width=20, height=2)
        btn3.pack(pady=10)

        # Área de texto para output
        self.text_area = tk.Text(self.root, height=30, width=60)
        self.text_area.pack(pady=10)

    # Executa a listagem de processols
    def funcao1(self):
        self.adicionar_texto(f"Procurando Processo!\n")
        for processo in psutil.process_iter(['pid', 'name']):
            if "steam.exe" in processo.info["name"]:
                self.adicionar_texto(f"Processo Encontrado! steam.exe encontrado! PID -> {processo.info["pid"]}\n")

    def funcao2(self):
        self.adicionar_texto("Fechando processo\n")
        functions.fechar_processo_por_nome("steam.exe")

    def funcao3(self):
        self.adicionar_texto("Abrindo steam.exe\n")
        functions.abrir_programa()

    def adicionar_texto(self, texto):
        self.text_area.insert(tk.END, texto)
        self.text_area.see(tk.END)

    def executar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MeuSoftware()
    app.executar()
