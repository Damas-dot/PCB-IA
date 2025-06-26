# 📋 PCB Defect Detector - Instruções Passo a Passo

## 🎯 O que você vai aprender

Neste guia, você aprenderá a executar uma aplicação web para detecção de defeitos em PCB usando:
- **Backend**: Python + Flask (servidor)
- **Frontend**: HTML + CSS + JavaScript (interface)

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

### 1. Python 3.7 ou superior
**Windows:**
- Baixe em: https://www.python.org/downloads/
- Durante a instalação, marque "Add Python to PATH"

**macOS:**
```bash
# Usando Homebrew
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Verificar instalação
Abra o terminal/prompt de comando e digite:
```bash
python --version
# ou
python3 --version
```

Deve mostrar algo como: `Python 3.x.x`

## 🚀 Passo 1: Baixar os arquivos

1. **Baixe todos os arquivos** da aplicação para uma pasta no seu computador
2. **Estrutura esperada:**
   ```
   pcb-detector-simple/
   ├── app.py                          # Servidor Python
   ├── requirements.txt                # Dependências
   ├── static/
   │   └── index.html                  # Interface web
   └── INSTRUCOES_PASSO_A_PASSO.md    # Este arquivo
   ```

## 🚀 Passo 2: Abrir o terminal na pasta

### Windows:
1. Abra o **Explorador de Arquivos**
2. Navegue até a pasta `pcb-detector-simple`
3. Clique na barra de endereço e digite `cmd`
4. Pressione **Enter**

### macOS/Linux:
1. Abra o **Terminal**
2. Use o comando `cd` para navegar até a pasta:
   ```bash
   cd caminho/para/pcb-detector-simple
   ```

## 🚀 Passo 3: Instalar dependências Python

No terminal, execute:

```bash
# Instalar as bibliotecas necessárias
pip install -r requirements.txt
```

**Se der erro, tente:**
```bash
pip3 install -r requirements.txt
```

**Aguarde a instalação** (pode demorar alguns minutos na primeira vez)

## 🚀 Passo 4: Executar o servidor

No terminal, execute:

```bash
python app.py
```

**Se der erro, tente:**
```bash
python3 app.py
```

**Você deve ver algo assim:**
```
🚀 Iniciando PCB Defect Detector...
📍 Backend disponível em: http://localhost:5000
📍 Interface web em: http://localhost:5000
🔧 Para parar o servidor, pressione Ctrl+C
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
```

## 🚀 Passo 5: Acessar a aplicação

1. **Abra seu navegador** (Chrome, Firefox, Edge, Safari)
2. **Digite na barra de endereço:**
   ```
   http://localhost:5000
   ```
3. **Pressione Enter**

**Você deve ver a interface da aplicação!** 🎉

## 🔧 Como usar a aplicação

### 1. Upload de Imagem
- **Arraste uma imagem** para a área de upload, ou
- **Clique na área** para selecionar um arquivo
- **Formatos aceitos:** PNG, JPG, JPEG, BMP, TIFF
- **Tamanho máximo:** 16MB

### 2. Análise
- Após selecionar a imagem, clique em **"🔍 Analisar Defeitos"**
- Aguarde o processamento (alguns segundos)

### 3. Visualizar Resultados
- **Aba Visualização:** Compare a imagem original com os defeitos marcados
- **Aba Detalhes:** Veja estatísticas e lista detalhada dos defeitos

## ❌ Solucionando Problemas

### Problema: "python não é reconhecido"
**Solução:** Python não está instalado ou não está no PATH
- Reinstale o Python marcando "Add to PATH"
- Ou use `python3` em vez de `python`

### Problema: "pip não é reconhecido"
**Solução:**
```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
python3 -m pip install -r requirements.txt
```

### Problema: Erro ao instalar opencv-python
**Solução:**
```bash
# Instalar dependências do sistema (Linux)
sudo apt install python3-opencv

# Ou instalar versão headless
pip install opencv-python-headless
```

### Problema: "Address already in use"
**Solução:** A porta 5000 já está sendo usada
- Feche outros programas que possam estar usando a porta
- Ou mude a porta no arquivo `app.py` (linha final):
  ```python
  app.run(host='0.0.0.0', port=5001, debug=True)
  ```

### Problema: Página não carrega
**Verificações:**
1. O servidor está rodando? (veja mensagens no terminal)
2. O endereço está correto? (`http://localhost:5000`)
3. Firewall bloqueando? (temporariamente desative)

## 🛑 Como parar a aplicação

1. **No terminal onde o servidor está rodando**
2. **Pressione:** `Ctrl + C` (Windows/Linux) ou `Cmd + C` (macOS)
3. **Confirme** se necessário

## 📁 Estrutura dos Arquivos

### `app.py` - Servidor Backend
- **Função:** Processa as imagens e detecta defeitos
- **Tecnologia:** Python + Flask
- **Não modifique** a menos que saiba o que está fazendo

### `static/index.html` - Interface Web
- **Função:** Interface visual para o usuário
- **Tecnologia:** HTML + CSS + JavaScript
- **Você pode personalizar** cores, textos, etc.

### `requirements.txt` - Dependências
- **Função:** Lista as bibliotecas Python necessárias
- **Usado pelo:** comando `pip install -r requirements.txt`

## 🎨 Personalizações Simples

### Mudar cores da interface
Edite o arquivo `static/index.html` e procure por:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Mudar título
No arquivo `static/index.html`, procure por:
```html
<title>PCB Defect Detector - Detecção de Defeitos</title>
```

## 🔄 Próximos Passos

### Para uso em produção:
1. **Integrar modelo real** de IA (substituir simulação)
2. **Configurar banco de dados** para salvar resultados
3. **Adicionar autenticação** de usuários
4. **Deploy em servidor** web

### Para desenvolvimento:
1. **Estudar o código** Python em `app.py`
2. **Modificar a interface** em `static/index.html`
3. **Adicionar novas funcionalidades**

## 📞 Suporte

Se tiver problemas:
1. **Verifique os pré-requisitos** estão instalados
2. **Siga os passos exatamente** como descritos
3. **Leia as mensagens de erro** no terminal
4. **Consulte a seção de problemas** acima

---

**🎉 Parabéns! Você agora tem uma aplicação web funcionando para detecção de defeitos em PCB!**

