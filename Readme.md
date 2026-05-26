# TP05 - Compressão de Mídias: Combinação de Algoritmos
**Instituição:** Instituto Superior Politécnico de Tecnologias e Ciências (ISPTEC)  
**Disciplina:** Multimédia  
**Trabalho:** Individual (TP05)  
**Estudante:** Henrique Mendes

## 1. Descrição do Projecto
Este projecto desenvolve uma solução prática e inovadora de compressão híbrida de imagem para o cumprimento das directrizes do TP05. A pipeline combina dois algoritmos distintos para maximizar a eficiência:
1. **WebP (via Pillow):** Aplica uma compressão espacial/visual inicial com perdas (*lossy*).
2. **Zstandard (zstd):** Aplica uma compressão estatística e entrópica sem perdas (*lossless*) sobre o binário do WebP, eliminando redundâncias residuais e metadados desnecessários.

O objectivo é analisar se esta combinação moderna supera o desempenho dos algoritmos quando utilizados individualmente em termos de taxa de compressão, tamanho final e tempo de processamento.

## 2. Requisitos e Dependências
O projecto foi desenvolvido utilizando a linguagem **Python 3.10+**. As dependências de bibliotecas externas necessárias são:
* **Pillow:** Para a manipulação, leitura e conversão da imagem original para o formato WebP.
* **Zstandard (zstd):** Para a compressão de entropia secundária de alta velocidade e densidade.

## 3. Configuração do Ambiente e Instalação
Para configurar o ambiente de desenvolvimento e instalar todas as dependências do projecto, siga os passos abaixo no seu terminal:

1. Certifique-se de que tem o Python e o gestor de pacotes `pip` instalados.
2. Navegue até à pasta raiz do projecto.
3. Execute o comando para instalar as dependências listadas no `requirements.txt`:
   pip install -r requirements.txt
