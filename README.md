# FourierFilterMagic

# Descrição

FourierFilterMagic é um projeto de processamento de imagens que utiliza a Transformada de Fourier para remover ruído sistemático de imagens, referente a solução do exercício sobre DFT. Este repositório contém código para aplicar diferentes máscaras no domínio da frequência, avaliar a qualidade das imagens recuperadas usando SSIM e MSE, e melhorar a imagem final com técnicas de equalização de histograma e suavização.

# Estrutura do Repositório

    dft.py: Script principal que contém as funções para aplicar máscaras de Fourier, avaliar as imagens e plotar os resultados.
    images/: Diretório para armazenar as imagens de entrada e saída.
    results/: Diretório para armazenar os resultados e gráficos gerados pelo script.
    README.md: Documento que você está lendo agora.

# Dependências

Certifique-se de ter as seguintes bibliotecas Python instaladas:

    numpy
    matplotlib
    scikit-image

Você pode instalar as dependências usando o pip:

bash

pip install numpy matplotlib scikit-image

Como Usar

    Clone o repositório:

bash

git clone https://github.com/seu-usuario/FourierFilterMagic.git
cd FourierFilterMagic

    Coloque a imagem que deseja processar no diretório images/.

    Edite o caminho da imagem no script dft.py para apontar para sua imagem:

python

file_path = 'images/seu_arquivo.jpg'

    Execute o script:

bash

python dft.py

    Os resultados serão exibidos e salvos no diretório results/.

# Funcionalidades

    Aplicação de Máscaras de Fourier: Aplica máscaras verticais, horizontais e combinadas para remover ruído sistemático.
    Avaliação de Qualidade: Utiliza SSIM e MSE para avaliar a qualidade das imagens processadas.
    Equalização e Suavização: Aplica equalização de histograma e filtro Gaussiano para melhorar a qualidade visual da imagem final.

# Exemplo de Uso

Aqui está um exemplo de como os resultados são exibidos:

    Imagem Original
    Máscara de Fourier (Vertical)
    Imagem Recuperada (Vertical)
    Máscara de Fourier (Horizontal)
    Imagem Recuperada (Horizontal)
    Máscara de Fourier (Combinada)
    Imagem Recuperada (Combinada)
    Melhor Resultado (Equalizado + Suavizado)

# Resultados

O script calcula e exibe os valores de SSIM e MSE para cada técnica de máscara aplicada, além de mostrar o resultado visual das imagens processadas.

# Contribuição

Se você tiver alguma dúvida ou sugestão, entre em contato:

    Nome: Gabriel Anselmo & Laís Vossen
    GitHub: selmin01 & Laispvv