import os
import sys

# Garantir que a raiz do projeto e a pasta 'src' estão no PATH do Python
pasta_raiz = os.path.dirname(os.path.abspath(__file__))
sys.path.append(pasta_raiz)
sys.path.append(os.path.join(pasta_raiz, 'src'))

# Importa explicitamente de src.compressor 
from src.compressor import ejecutar_analise_comparativa

def iniciar_menu_interativo():
    print("====================================================")
    print("   SISTEMA INTERATIVO DE COMPRESSÃO -               ")
    print("====================================================")
    
    pasta_origem = os.path.join(pasta_raiz, "midias_originais")
    
    if not os.path.exists(pasta_origem):
        os.makedirs(pasta_origem, exist_ok=True)
        print(f"[AVISO] A pasta '{pasta_origem}' foi criada.")
        print("Insira ficheiros de imagem válidos lá dentro e execute novamente.")
        return
        
    extensoes_suportadas = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    arquivos_originais = [f for f in os.listdir(pasta_origem) if f.lower().endswith(extensoes_suportadas)]
    
    if not arquivos_originais:
        print(f"[ERRO] Não existem imagens de teste na pasta: {pasta_origem}")
        print("Por favor, adicione imagens (.jpg ou .png) reais para prosseguir.")
        return
        
    print("\nSelecione a imagem original que deseja testar:")
    for i, arquivo in enumerate(arquivos_originais, start=1):
        tamanho_kb = os.path.getsize(os.path.join(pasta_origem, arquivo)) / 1024
        print(f" [{i}] {arquivo} ({tamanho_kb:.2f} KB)")
        
    # Validação da escolha da imagem
    while True:
        try:
            escolha = int(input("\nDigite o número correspondente à imagem: "))
            if 1 <= escolha <= len(arquivos_originais):
                imagem_selecionada = arquivos_originais[escolha - 1]
                break
            else:
                print(f"[ERRO] Por favor, selecione um número entre 1 e {len(arquivos_originais)}.")
        except ValueError:
            print("[ERRO] Entrada inválida. Digite um número inteiro.")
            
    # Pergunta técnica sobre as propriedades da mídia
    print("\nQual é o tipo predominante de elementos visuais nesta mídia?")
    print(" [1] Contém texto nítido, formas geométricas, gráficos ou elements vetorizados (Cores Sólidas)")
    print(" [2] É uma fotografia realista, paisagem natural ou imagem de transição cromática complexa")
    
    qualidade_definida = 80  
    while True:
        try:
            tipo_midia = int(input("\nEscolha uma opção (1 ou 2): "))
            if tipo_midia == 1:
                qualidade_definida = 90
                print("[CONFIGURAÇÃO] Parâmetro WebP otimizado para preservação de bordas (Quality: 90).")
                break
            elif tipo_midia == 2:
                qualidade_definida = 75
                print("[CONFIGURAÇÃO] Parâmetro WebP otimizado para alta compressão visual (Quality: 75).")
                break
            else:
                print("[ERRO] Opção inválida. Digite 1 ou 2.")
        except ValueError:
            print("[ERRO] Entrada inválida. Digite 1 ou 2.")
            
    # Executar a chamada com o nome correto
    ejecutar_analise_comparativa(imagem_selecionada, qualidade_webp=qualidade_definida, nivel_zstd=3)

if __name__ == "__main__":
    iniciar_menu_interativo()