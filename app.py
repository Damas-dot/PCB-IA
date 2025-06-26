#!/usr/bin/env python3
"""
PCB Defect Detector - Backend Flask Simplificado
Aplicação para detecção de defeitos em placas de circuito impresso
"""

import os
import cv2
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image
import io
import base64

# Configuração da aplicação Flask
app = Flask(__name__, static_folder='static')
CORS(app)  # Permitir requisições de qualquer origem

# Configurações
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp', 'tiff'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

# Criar pastas necessárias
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('static', exist_ok=True)

def allowed_file(filename):
    """Verifica se o arquivo tem uma extensão permitida"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    """Pré-processa a imagem para melhorar a detecção"""
    img = cv2.imread(image_path)
    if img is None:
        return None
    
    # Redimensionar se muito grande
    height, width = img.shape[:2]
    if width > 1024 or height > 1024:
        scale = min(1024/width, 1024/height)
        new_width = int(width * scale)
        new_height = int(height * scale)
        img = cv2.resize(img, (new_width, new_height))
    
    # Melhorar contraste usando CLAHE
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    l = clahe.apply(l)
    img = cv2.merge([l, a, b])
    img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
    
    return img

def simulate_pcb_detection(image_path):
    """Simula detecção de defeitos em PCB"""
    img = cv2.imread(image_path)
    if img is None:
        return []
    
    height, width = img.shape[:2]
    
    # Simular alguns defeitos detectados baseados no tamanho da imagem
    detections = [
        {
            'type': 'solder_bridge',
            'confidence': 0.89,
            'bbox': [int(width*0.2), int(height*0.3), int(width*0.35), int(height*0.45)],
            'description': 'Ponte de solda detectada entre componentes'
        },
        {
            'type': 'missing_component',
            'confidence': 0.95,
            'bbox': [int(width*0.6), int(height*0.2), int(width*0.75), int(height*0.35)],
            'description': 'Componente ausente na posição esperada'
        },
        {
            'type': 'cold_solder',
            'confidence': 0.76,
            'bbox': [int(width*0.1), int(height*0.7), int(width*0.25), int(height*0.85)],
            'description': 'Solda fria detectada - conexão inadequada'
        }
    ]
    
    return detections

def draw_detections(image_path, detections):
    """Desenha as detecções na imagem"""
    img = cv2.imread(image_path)
    if img is None:
        return None
    
    # Cores para diferentes tipos de defeitos
    colors = {
        'solder_bridge': (0, 0, 255),      # Vermelho
        'missing_component': (255, 0, 0),  # Azul
        'cold_solder': (0, 165, 255),      # Laranja
        'misaligned': (0, 255, 255),       # Amarelo
        'damaged_trace': (128, 0, 128)     # Roxo
    }
    
    for detection in detections:
        x1, y1, x2, y2 = detection['bbox']
        defect_type = detection['type']
        confidence = detection['confidence']
        
        color = colors.get(defect_type, (0, 255, 0))
        
        # Desenhar retângulo
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        
        # Desenhar label com fundo
        label = f"{defect_type}: {confidence:.2f}"
        label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
        cv2.rectangle(img, (x1, y1 - label_size[1] - 10), 
                     (x1 + label_size[0], y1), color, -1)
        cv2.putText(img, label, (x1, y1 - 5), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    return img

def image_to_base64(img):
    """Converte imagem OpenCV para base64"""
    _, buffer = cv2.imencode('.jpg', img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    return f"data:image/jpeg;base64,{img_base64}"

# Rotas da API

@app.route('/')
def index():
    """Serve a página principal"""
    return send_from_directory('static', 'index.html')

@app.route('/api/upload', methods=['POST'])
def upload_image():
    """Endpoint para upload e análise de imagem PCB"""
    try:
        # Verificar se foi enviado um arquivo
        if 'file' not in request.files:
            return jsonify({'error': 'Nenhum arquivo enviado'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Tipo de arquivo não permitido. Use PNG, JPG, JPEG, BMP ou TIFF'}), 400
        
        # Verificar tamanho do arquivo
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0)
        
        if file_size > MAX_FILE_SIZE:
            return jsonify({'error': 'Arquivo muito grande (máximo 16MB)'}), 400
        
        # Salvar arquivo temporariamente
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # Pré-processar imagem
        processed_img = preprocess_image(filepath)
        if processed_img is None:
            os.remove(filepath)
            return jsonify({'error': 'Erro ao processar imagem'}), 400
        
        # Detectar defeitos (simulado)
        detections = simulate_pcb_detection(filepath)
        
        # Desenhar detecções
        result_img = draw_detections(filepath, detections)
        
        # Converter imagens para base64
        original_base64 = image_to_base64(cv2.imread(filepath))
        result_base64 = image_to_base64(result_img)
        
        # Limpar arquivo temporário
        os.remove(filepath)
        
        # Preparar resposta
        response = {
            'success': True,
            'original_image': original_base64,
            'result_image': result_base64,
            'detections': detections,
            'summary': {
                'total_defects': len(detections),
                'defect_types': list(set([d['type'] for d in detections])),
                'avg_confidence': sum([d['confidence'] for d in detections]) / len(detections) if detections else 0
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint para verificar saúde do serviço"""
    return jsonify({
        'status': 'healthy',
        'service': 'PCB Defect Detection',
        'version': '1.0.0'
    })

@app.route('/api/models', methods=['GET'])
def get_models():
    """Endpoint para listar modelos disponíveis"""
    models = [
        {
            'id': 'yolov8_pcb',
            'name': 'YOLOv8 PCB Detector',
            'description': 'Modelo especializado em detecção de defeitos em PCB',
            'accuracy': 0.89,
            'supported_defects': [
                'solder_bridge',
                'missing_component', 
                'cold_solder',
                'misaligned',
                'damaged_trace'
            ]
        }
    ]
    
    return jsonify({'models': models})

if __name__ == '__main__':
    print("🚀 Iniciando PCB Defect Detector...")
    print("📍 Backend disponível em: http://localhost:5001")
    print("📍 Interface web em: http://localhost:5001")
    print("🔧 Para parar o servidor, pressione Ctrl+C")
    
    app.run(host='0.0.0.0', port=5001, debug=True)

