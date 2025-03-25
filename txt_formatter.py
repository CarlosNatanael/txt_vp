import tkinter as tk
from tkinter import filedialog, messagebox

def carregar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(filetypes=[('Arquivos de texto', '*.txt')])
    if caminho_arquivo:
        try:
            with open(caminho_arquivo, "r" ,encoding="latin-1") as arquivo:
                conteudo = arquivo.readlines()
        except UnboundLocalError:
            with open(caminho_arquivo, "r", encoding="latin-1") as arquivo:
                conteudo = arquivo.readlines()
        processar_conteudo(conteudo)

def processar_conteudo(conteudo):
    linhas_formatadas = []
    for linha in conteudo:
        codigo = linha[:13].strip().ljust(13)  
        descricao = linha[13:33].strip().ljust(20)  
        valor = linha[33:].strip().zfill(20)  
        linhas_formatadas.append(f"{codigo}{descricao}{valor}")
    exibir_preview(linhas_formatadas)

def exibir_preview(linhas):
    global conteudo_formatado
    preview_text.config(state=tk.NORMAL)
    preview_text.delete("1.0", tk.END)
    for linha in linhas:
        preview_text.insert(tk.END, linha + "\n")
    preview_text.config(state=tk.DISABLED)
    conteudo_formatado = linhas

def salvar_arquivo():
    global conteudo_formatado
    if not conteudo_formatado:
        messagebox.showwarning("Atenção", "Nenhum arquivo processado")
        return
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])
    if caminho_arquivo:
        with open(caminho_arquivo, "w" ,encoding="utf-8") as arquivo:
            for linha in conteudo_formatado:
                arquivo.write(linha + "\n")
        messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso")
root = tk.Tk()
root.title("Formatador de TXT")
root.geometry("600x500")
frame = tk.Frame(root)
frame.pack(pady=10)

frame_preview = tk.Frame(root)
frame_preview.pack(pady=10)

tk.Button(frame, text="Carregar arquivo", command=carregar_arquivo).pack(pady=10)
tk.Button(frame, text="Salvar arquivo", command=salvar_arquivo).pack(pady=10)

scrollbar = tk.Scrollbar(frame_preview, orient=tk.VERTICAL)
preview_text = tk.Text(frame_preview, height=25, width=80, yscrollcommand=scrollbar.set, state=tk.DISABLED)
scrollbar.config(command=preview_text.yview)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
preview_text.pack(side=tk.LEFT)

conteudo_formatado = []

root.mainloop()
