# TP05 - Compressão de Mídias: Combinação de Algoritmos
**Instituição:** Instituto Superior Politécnico de Tecnologias e Ciências (ISPTEC)  
**Disciplina:** Multimédia  
**Trabalho:** Individual (TP05)  
**Estudante:** Henrique Mendes

---

## 1. Descrição do Projecto
[cite_start]Este projecto desenvolve uma solução prática e inovadora de compressão híbrida de imagem para o cumprimento das directrizes do TP05[cite: 7]. [cite_start]A pipeline combina dois algoritmos distintos para maximizar a eficiência[cite: 7, 37]:
1. [cite_start]**WebP (via Pillow):** Aplica uma compressão espacial/visual inicial com perdas (*lossy*)[cite: 45].
2. **Zstandard (zstd):** Aplica uma compressão estatística e entrópica sem perdas (*lossless*) sobre o binário do WebP, eliminando redundâncias residuais e metadados desnecessários.

[cite_start]O objectivo é analisar se esta combinação moderna supera o desempenho dos algoritmos quando utilizados individualmente em termos de taxa de compressão, tamanho final e tempo de processamento[cite: 7, 8, 9, 11, 12].

---

## 2. Requisitos e Dependências
[cite_start]O projecto foi desenvolvido utilizando a linguagem **Python 3.10+**[cite: 74]. [cite_start]As dependências de bibliotecas externas necessárias são:
* [cite_start]**Pillow:** Para a manipulação, leitura e conversão da imagem original para o formato WebP[cite: 80].
* **Zstandard (zstd):** Para a compressão de entropia secundária de alta velocidade e densidade.

---

## 3. Configuração do Ambiente e Instalação
[cite_start]Para configurar o ambiente de desenvolvimento e instalar todas as dependências do projecto, siga os passos abaixo no seu terminal[cite: 145, 146]:

1. Certifique-se de que tem o Python e o gestor de pacotes `pip` instalados.
2. Navegue até à pasta raiz do projecto.
3. [cite_start]Execute o comando para instalar as dependências listadas no `requirements.txt`[cite: 147]:
   ```bash
   pip install -r requirements.txt