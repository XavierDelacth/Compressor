import os
import time
import gzip
import zstandard as zstd
from PIL import Image

# Importando do módulo utilitário
from utils import calcular_taxa_compressao, gerar_grafico_comparativo

def ejecutar_analise_comparativa(nome_arquivo_imagem, qualidade_webp=80, nivel_zstd=3):
    # Caminhos base calculados a partir da localização deste script (dentro da pasta 'src')
    pasta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    pasta_origem = os.path.join(pasta_raiz, "midias_originais")
    pasta_destino = os.path.join(pasta_raiz, "midias_comprimidas")
    
    # Novas subpastas de organização exigidas
    pasta_gzip = os.path.join(pasta_destino, "gzip")
    pasta_zstd = os.path.join(pasta_destino, "zstd")
    pasta_analises = os.path.join(pasta_raiz, "analises_comparativas")
    
    caminho_original = os.path.join(pasta_origem, nome_arquivo_imagem)
    
    if not os.path.exists(caminho_original):
        print(f"[ERRO] Arquivo não encontrado em: {caminho_original}")
        return

    print(f"\n=== INICIANDO BENCHMARK MULTIMÉDIA: {nome_arquivo_imagem} ===")
    tam_original = os.path.getsize(caminho_original)
    
    nome_base = os.path.splitext(nome_arquivo_imagem)[0]
    
    # Definição dos novos caminhos estruturados
    caminho_temp_webp = os.path.join(pasta_destino, f"temp_{nome_base}.webp")
    caminho_final_zst = os.path.join(pasta_zstd, f"{nome_base}_combo_zstd.webp.zst")
    caminho_final_gzip = os.path.join(pasta_gzip, f"{nome_base}_combo_gzip.webp.gz")
    caminho_grafico = os.path.join(pasta_analises, f"analise_comparativa_{nome_base}.png")
    
    # Cria dinamicamente toda a árvore de diretorias necessária
    os.makedirs(pasta_destino, exist_ok=True)
    os.makedirs(pasta_gzip, exist_ok=True)
    os.makedirs(pasta_zstd, exist_ok=True)
    os.makedirs(pasta_analises, exist_ok=True)

    try:
        # --- CENÁRIO 1: Apenas WebP ---
        t_inicial_webp = time.time()
        img = Image.open(caminho_original)
        img.save(caminho_temp_webp, "WEBP", quality=qualidade_webp)
        tam_webp = os.path.getsize(caminho_temp_webp)
        t_final_webp = time.time() - t_inicial_webp
        
        with open(caminho_temp_webp, "rb") as f_in:
            dados_webp = f_in.read()
            
        # --- CENÁRIO 2: WebP + Zstandard ---
        t_inicial_zstd = time.time()
        cctx = zstd.ZstdCompressor(level=nivel_zstd)
        dados_zstd = cctx.compress(dados_webp)
        with open(caminho_final_zst, "wb") as f_out:
            f_out.write(dados_zstd)
        tam_zstd = os.path.getsize(caminho_final_zst)
        t_final_zstd = (time.time() - t_inicial_zstd) + t_inicial_webp 
        
        # --- CENÁRIO 3: WebP + GZIP ---
        t_inicial_gzip = time.time()
        with gzip.open(caminho_final_gzip, "wb") as f_out:
            f_out.write(dados_webp)
        tam_gzip = os.path.getsize(caminho_final_gzip)
        t_final_gzip = (time.time() - t_inicial_gzip) + t_inicial_webp 
        
        # --- GERAÇÃO DE GRÁFICOS E MÉTRICAS (Enviando para a nova pasta dedicada)
        gerar_grafico_comparativo(nome_arquivo_imagem, tam_original, tam_webp, tam_zstd, tam_gzip, caminho_grafico)
        
        # Exibição dos dados estruturados
        print("\n" + "="*50)
        print("          RELATÓRIO DE MÉTRICAS COMPARATIVAS          ")
        print("="*50)
        print(f"Ficheiro de Teste Original: {nome_arquivo_imagem}")
        print(f"Tamanho de Origem:          {tam_original / 1024:.2f} KB\n")
        
        print(f"1. PIPELINE ISOLADO (Apenas WebP):")
        print(f"   - Tamanho Final:         {tam_webp / 1024:.2f} KB")
        print(f"   - Redução Obtida:        {calcular_taxa_compressao(tam_original, tam_webp):.2f}%")
        print(f"   - Tempo de Execução:     {t_final_webp:.4f} seg\n")
        
        print(f"2. PIPELINE COMBINAÇÃO 1 (WebP + Zstandard):")
        print(f"   - Tamanho Final:         {tam_zstd / 1024:.2f} KB")
        print(f"   - Subpasta de Destino:   midias_comprimidas/zstd/")
        print(f"   - Redução Obtida:        {calcular_taxa_compressao(tam_original, tam_zstd):.2f}%")
        print(f"   - Tempo Total de Fluxo:  {t_final_zstd:.4f} seg\n")
        
        print(f"3. PIPELINE COMBINAÇÃO 2 (WebP + GZIP):")
        print(f"   - Tamanho Final:         {tam_gzip / 1024:.2f} KB")
        print(f"   - Subpasta de Destino:   midias_comprimidas/gzip/")
        print(f"   - Redução Obtida:        {calcular_taxa_compressao(tam_original, tam_gzip):.2f}%")
        print(f"   - Tempo Total de Fluxo:  {t_final_gzip:.4f} seg")
        print("="*50)
        
        # Conclusão automatizada baseada nos dados reais
        melhor_tam = min(tam_webp, tam_zstd, tam_gzip)
        if melhor_tam == tam_zstd:
            print("[CONCLUSÃO TÉCNICA] A combinação WebP + Zstandard apresentou maior eficiência volumétrica.")
        elif melhor_tam == tam_gzip:
            print("[CONCLUSÃO TÉCNICA] A combinação WebP + GZIP apresentou maior eficiência volumétrica.")
        else:
            print("[CONCLUSÃO TÉCNICA] O compressor espacial WebP isolado manteve o menor tamanho.")
            
    finally:
        # Remove o ficheiro temporário da raiz de mídias comprimidas
        if os.path.exists(caminho_temp_webp):
            os.remove(caminho_temp_webp)

if __name__ == "__main__":
    print("[AVISO] Para executar o projeto de forma interativa, use o 'main.py' na raiz.")