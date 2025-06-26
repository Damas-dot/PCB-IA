# 🔧 PCB Defect Detector - Versão Simplificada

Uma aplicação web para detecção de defeitos em placas de circuito impresso (PCB) usando HTML/CSS/JavaScript no frontend e Python/Flask no backend.

## ✨ Características

- **Interface Simples**: HTML, CSS e JavaScript puro (sem React/Node.js)
- **Backend Python**: Flask para processamento de imagens
- **Detecção de Defeitos**: Algoritmo simulado para 5 tipos de defeitos
- **Upload Fácil**: Drag & drop de imagens
- **Visualização Clara**: Comparação lado a lado das imagens

## 🎯 Defeitos Detectados

1. **Ponte de Solda** - Conexões indevidas entre componentes
2. **Componente Ausente** - Falta de componentes esperados
3. **Solda Fria** - Conexões de solda inadequadas
4. **Desalinhamento** - Componentes fora de posição
5. **Trilha Danificada** - Danos nas trilhas do circuito

## 📁 Estrutura dos Arquivos

```
pcb-detector-simple/
├── app.py                          # Servidor Flask (Backend)
├── requirements.txt                # Dependências Python
├── static/
│   └── index.html                  # Interface Web (Frontend)
├── uploads/                        # Pasta temporária para imagens
├── README_SIMPLES.md              # Este arquivo
└── INSTRUCOES_PASSO_A_PASSO.md    # Guia detalhado
```

## 🚀 Como Executar

### 1. Instalar Python
- Baixe em: https://www.python.org/downloads/
- Marque "Add Python to PATH" durante a instalação

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Executar o Servidor
```bash
python app.py
```

### 4. Acessar a Aplicação
Abra o navegador e acesse: `http://localhost:5001`

## 💡 Como Usar

1. **Upload**: Arraste uma imagem PCB ou clique para selecionar
2. **Análise**: Clique em "🔍 Analisar Defeitos"
3. **Resultados**: Veja a comparação e estatísticas

## 🔧 Tecnologias Utilizadas

### Backend (Python)
- **Flask**: Framework web
- **OpenCV**: Processamento de imagens
- **PIL**: Manipulação de imagens
- **NumPy**: Operações matemáticas

### Frontend (Web)
- **HTML5**: Estrutura da página
- **CSS3**: Estilização e layout responsivo
- **JavaScript**: Interatividade e comunicação com API

## 📊 Funcionalidades

### ✅ Implementadas
- Upload de imagens (PNG, JPG, JPEG, BMP, TIFF)
- Pré-processamento automático
- Detecção simulada de defeitos
- Visualização com bounding boxes
- Interface responsiva
- Estatísticas detalhadas

### 🔄 Futuras Melhorias
- Integração com modelo real de IA
- Banco de dados para histórico
- Relatórios em PDF
- Autenticação de usuários

## ❓ Problemas Comuns

### "python não é reconhecido"
**Solução**: Reinstale o Python marcando "Add to PATH"

### "pip não é reconhecido"
**Solução**: Use `python -m pip install -r requirements.txt`

### "Address already in use"
**Solução**: Mude a porta no arquivo `app.py` (linha final)

### Página não carrega
**Verificações**:
1. Servidor está rodando?
2. Endereço correto? (`http://localhost:5001`)
3. Firewall bloqueando?

## 📞 Suporte

Para dúvidas detalhadas, consulte o arquivo `INSTRUCOES_PASSO_A_PASSO.md` que contém um guia completo com capturas de tela e soluções para problemas comuns.

---

**🎉 Aplicação testada e funcionando! Pronta para detectar defeitos em PCB!**

