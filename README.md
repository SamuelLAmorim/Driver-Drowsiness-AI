# 🤖 Driver Drowsiness AI - Sistema de Detecção de Sonolência

## 🌟 Visão Geral do Projeto

Este projeto implementa um sistema de monitoramento em tempo real para detectar sinais de fadiga ou sonolência em motoristas, utilizando Visão Computacional (Computer Vision) e o framework YOLO (You Only Look Once) para classificação de estado ocular. O sistema aciona um alerta sonoro e visual quando o tempo de fechamento dos olhos excede um limite de segurança.

A interface gráfica é construída usando a biblioteca OpenCV, focando na clareza e na experiência do usuário em um ambiente de cabine.

---

## ⚙️ Tecnologias Utilizadas

O sistema é construído majoritariamente em Python e depende das seguintes bibliotecas:

* **`opencv-python` (cv2):** Captura de vídeo e interface gráfica.
* **`ultralytics` (YOLO):** Carregamento e execução do modelo de detecção de objetos.
* **`numpy`:** Suporte a operações numéricas.
* **Biblioteca de Áudio (`AlertSystem`):** Para o alerta sonoro (depende da sua implementação no arquivo `alert.py`).

---

## 💻 Requisitos de Ambiente

Para garantir a **performance** e a **compatibilidade** do modelo YOLO, é **fortemente recomendado** o uso da seguinte configuração do interpretador:

* **Interpretador Python:** **Versão 3.11**
    > **Atenção:** Versões anteriores do Python podem apresentar problemas de compatibilidade com as versões mais recentes das bibliotecas `ultralytics` e dependências relacionadas, prejudicando a inicialização e a performance do modelo.

---

## 🚀 Instalação e Configuração

Para executar este projeto, siga os passos abaixo:

### 1. Pré-requisitos

Certifique-se de ter o **Python (3.11 recomendado)** instalado no seu sistema.

### 2. Clonar o Repositório

git clone [https://github.com/seu-usuario/drowsiness-ai.git](https://github.com/seu-usuario/drowsiness-ai.git)
cd drowsiness-ai

### 3. Instalar Dependências

Instale todas as bibliotecas necessárias usando o pip:
pip install opencv-python ultralytics numpy # + qualquer biblioteca que você use para o alerta sonoro (ex: simpleaudio, playsound)

### 4. Configurações do Modelo: 

Você deve ter os seguintes arquivos no diretório do projeto:

config.py: Deve conter o caminho para o modelo (MODEL_PATH) e o limiar de confiança (CONF_THRESHOLD).
Modelo YOLO: O arquivo de pesos do seu modelo (exemplo: best.pt) deve ser referenciado em config.py.

### 5. Configurações do Alarme: 

Verifique se o seu arquivo alert.py está configurado corretamente para reproduzir o alarme sonoro.

## ▶️ Como Executar o Sistema

Basta executar o arquivo principal:
python src/main.py  ---> O sistema será iniciado, abrindo a janela de vídeo da sua webcam.

## ⌨️ Comandos da Interface

### Tecla	                      Ação
Z ou F11	    Alterna entre o modo janela e o modo Tela Cheia (Fullscreen).
ESC	          Encerra a aplicação e fecha a janela.

## ⚠️ Estrutura do Código

### Arquivo/Pasta	                           Função
src/main.py	         Loop principal, captura de vídeo, renderização da interface (HUD) e lógica de tempo de fadiga.
detector.py	         Contém a classe EyeDetector. Carrega o modelo YOLO e retorna o estado booleano (True se fechado, False se aberto).
alert.py	           Classe ou funções responsáveis por acionar e parar o alarme sonoro.
config.py	           Armazena variáveis de configuração, como MODEL_PATH e CONF_THRESHOLD.


## 🤝 Contribuição
Sinta-se à vontade para sugerir melhorias, como novos modelos de detecção ou refatoração do código. Por favor, abra um issue ou envie um Pull Request no repositório.

## 📄 Licença
Feito por Samuel Leal Amorim
