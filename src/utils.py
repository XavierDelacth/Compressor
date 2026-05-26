import os
import matplotlib.pyplot as plt

def calcular_taxa_compressao(tamanho_original, tamanho_final):
    """Calcula a percentagem de redução de tamanho."""
    if tamanho_original == 0:
        return 0.0
    return (1 - (tamanho_final / tamanho_original)) * 100

def gerar_grafico_comparativo(nome_imagem, tam_original, tam_webp, tam_zstd, tam_gzip, caminho_salvar):
    """Gera um gráfico de barras comparando o impacto das diferentes combinações."""
    # Converter bytes para Kilobytes (KB)
    tamanhos_kb = [
        tam_original / 1024, 
        tam_webp / 1024, 
        tam_zstd / 1024, 
        tam_gzip / 1024
    ]
    etapas = ['Original (JPG)', 'Apenas WebP', 'WebP + Zstandard', 'WebP + GZIP']
    
    plt.figure(figsize=(10, 6))
    barras = plt.bar(etapas, tamanhos_kb, color=['#7f8c8d', '#3498db', '#2ecc71', '#e67e22'])
    
    # Adicionar os valores exatos em cima das barras
    for barra in barras:
        yval = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2.0, yval + (max(tamanhos_kb)*0.01), 
                 f"{yval:.2f} KB", ha='center', va='bottom', fontweight='bold')
                 
    plt.title(f"Análise Comparativa de Combinações - {nome_imagem}", fontsize=12, fontweight='bold')
    plt.ylabel("Tamanho do Ficheiro (KB)", fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Garantir que a pasta de destino existe
    os.makedirs(os.path.dirname(caminho_salvar), exist_ok=True)
    plt.savefig(caminho_salvar, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[INFO] Gráfico comparativo gerado em: {caminho_salvar}")