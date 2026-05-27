#Compressão de Mídias: Combinação de Algoritmos

> **Instituição:** Instituto Superior Politécnico de Tecnologias e Ciências (ISPTEC)  
> **Disciplina:** Multimédia  
> **Estudante:** Henrique Mendes  


---

##  Visão Geral

Este projecto implementa um **sistema de benchmark de compressão híbrida de imagem**, combinando múltiplos algoritmos para analisar e comparar o desempenho de diferentes pipelines de compressão.

A solução testa três cenários distintos:

| Pipeline | Tipo | Descrição |
|----------|------|-----------|
| **WebP** (isolado) | Lossy | Compressão espacial/visual com perdas |
| **WebP + Zstandard** | Lossy + Lossless | Compressão visual seguida de compressão entrópica moderna |
| **WebP + GZIP** | Lossy + Lossless | Compressão visual seguida de compressão deflate clássica |

O objectivo é determinar se a **combinação de algoritmos** produz resultados superiores ao uso individual, medindo taxa de compressão, tamanho final e tempo de processamento.

##  Estrutura do Projecto


compressor/
│
├── main.py                        # Ponto de entrada — menu interactivo
│
├── src/
│   ├── __init__.py                # Marca 'src' como pacote Python
│   ├── compressor.py              # Lógica principal de compressão e benchmark
│   └── utils.py                   # Funções auxiliares: métricas e gráficos
│
├── midias_originais/              #  Coloque aqui as imagens de teste
│   └── (ex: foto.jpg, imagem.png)
│
├── midias_comprimidas/            # Gerado automaticamente
│   ├── zstd/                      # Ficheiros .webp.zst (WebP + Zstandard)
│   └── gzip/                      # Ficheiros .webp.gz  (WebP + GZIP)
│
├── analises_comparativas/         # Gerado automaticamente — gráficos PNG
│
├── requirements.txt               # Dependências do projecto
└── README.md                      # Este ficheiro


##  Requisitos do Sistema

- **Python** 3.10 ou superior
- **pip** (gestor de pacotes Python)
- Sistema operativo: Windows, Linux ou macOS

---

##  Instalação e Configuração

### 1. Clonar ou descompactar o projecto

Navegue até à pasta raiz do projecto no terminal:


cd caminho/para/compressor


### 2. (Recomendado) Criar um ambiente virtual


# Criar o ambiente
python -m venv venv

# Activar no Windows
venv\Scripts\activate

# Activar no Linux/macOS
source venv/bin/activate


### 3. Instalar as dependências


pip install -r requirements.txt


As dependências instaladas serão:

| Biblioteca | Versão Mínima | Função |
|-----------|--------------|--------|
| `Pillow` | ≥ 10.0.0 | Leitura e conversão de imagens para WebP |
| `zstandard` | ≥ 0.21.0 | Compressão entrópica de alta velocidade (Zstd) |
| `matplotlib` | ≥ 3.5.0 | Geração de gráficos comparativos |

---

## ▶️ Como Executar

### 1. Adicionar imagens de teste

Coloque imagens reais (`.jpg`, `.jpeg`, `.png`, `.bmp` ou `.tiff`) na pasta:


midias_originais/


>  **Sem imagens nesta pasta, o programa não executa.**

### 2. Executar o programa principal

python main.py


### 3. Seguir o menu interactivo

O programa irá:
1. **Listar** todas as imagens disponíveis em `midias_originais/`
2. **Pedir** para seleccionar a imagem a testar
3. **Perguntar** o tipo de conteúdo visual (para optimizar o parâmetro de qualidade WebP)
4. **Executar** os três pipelines de compressão
5. **Apresentar** o relatório de métricas no terminal
6. **Guardar** o gráfico comparativo em `analises_comparativas/`

**Exemplo de sessão:**

```
====================================================
   SISTEMA INTERATIVO DE COMPRESSÃO 
====================================================

Selecione a imagem original que deseja testar:
 [1] paisagem.jpg (2048.50 KB)
 [2] diagrama.png (540.20 KB)

Digite o número correspondente à imagem: 1

Qual é o tipo predominante de elementos visuais nesta mídia?
 [1] Contém texto nítido, formas geométricas ou gráficos (Cores Sólidas)
 [2] É uma fotografia realista ou paisagem natural

Escolha uma opção (1 ou 2): 2
[CONFIGURAÇÃO] Parâmetro WebP otimizado para alta compressão visual (Quality: 75).


---

##  Resultados e Saídas

Após a execução, são gerados:

- **Terminal:** Relatório detalhado com tamanhos, taxas de compressão e tempos
- **`midias_comprimidas/zstd/`** — ficheiro `.webp.zst` (pipeline WebP + Zstandard)
- **`midias_comprimidas/gzip/`** — ficheiro `.webp.gz` (pipeline WebP + GZIP)
- **`analises_comparativas/`** — gráfico de barras `.png` com comparação visual

---

## Algoritmos Utilizados

### WebP (Compressão com Perdas — Lossy)
Formato de imagem moderno desenvolvido pela Google, baseado em codificação preditiva intra-frame do codec VP8. Oferece compressão superior ao JPEG para fotografias, preservando qualidade perceptiva.

### Zstandard — zstd (Compressão sem Perdas — Lossless)
Algoritmo de compressão de alta velocidade desenvolvido pela Meta (Facebook), baseado em codificação ANS (Asymmetric Numeral Systems). Apresenta melhor rácio velocidade/compressão do que GZIP e BZIP2.

### GZIP (Compressão sem Perdas — Lossless)
Algoritmo clássico baseado no deflate (combinação de LZ77 + codificação de Huffman). Amplamente suportado e utilizado como referência de comparação.

---

## Métricas de Avaliação

Taxa de Compressão (%) = (1 - Tamanho_Final / Tamanho_Original) × 100


| Métrica | Descrição |
|---------|-----------|
| **Taxa de compressão** | Percentagem de redução em relação ao ori |
| **Tamanho final (KB)** | Tamanho do ficheiro após compressão |
| **Tempo de execução (s)** | Duração total do pipeline de compressão |

##  Resolução de Problemas Comuns

| Erro | Causa | Solução |
|------|-------|---------|
| `ModuleNotFoundError: No module named 'PIL'` | Pillow não instalado | `pip install pillow` |
| `ModuleNotFoundError: No module named 'zstandard'` | zstd não instalado | `pip install zstandard` |
| `[ERRO] Não existem imagens de teste` | Pasta `midias_originais/` vazia | Adicione imagens `.jpg` ou `.png` |
| `ImportError` ao executar `compressor.py` directamente | Importação relativa fora do pacote | Execute sempre via `python main.py` na raiz |

---

## Referências Bibliográficas

- **Pillow (PIL Fork)** — Alex Clark et al. *Pillow Documentation*. Disponível em: https://pillow.readthedocs.io
- **Zstandard** — Yann Collet, Meta Platforms. *Zstandard — Real-time data compression algorithm*. Disponível em: https://facebook.github.io/zstd/
- **WebP** — Google Developers. *WebP Compression Techniques*. Disponível em: https://developers.google.com/speed/webp
- **GZIP / RFC 1952** — Deutsch, P. (1996). *GZIP file format specification version 4.3*. IETF RFC 1952.
- **Matplotlib** — Hunter, J.D. (2007). *Matplotlib: A 2D Graphics Environment*. Computing in Science & Engineering, 9(3), 90–95.
- **Python Software Foundation** — *Python Language Reference, version 3.10+*. Disponível em: https://www.python.org