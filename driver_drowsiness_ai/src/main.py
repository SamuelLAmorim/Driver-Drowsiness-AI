import cv2
import time
from detector import EyeDetector 
from alert import AlertSystem
from datetime import datetime
import numpy as np 

# Inicialização
detector = EyeDetector()
alert = AlertSystem()

cap = cv2.VideoCapture(0)

closed_start = None
fullscreen = False 

WINDOW = "Driver Drowsiness AI"
cv2.namedWindow(WINDOW, cv2.WINDOW_NORMAL)


def draw_ui(frame, is_closed, timer):
    h, w, _ = frame.shape
    MAX_TIME = 3.0 

    if is_closed and timer >= MAX_TIME:
        # Borda Vermelha (Alerta Crítico)
        cv2.rectangle(frame, (0,0), (w,h), (0,0,255), 15)
        cv2.putText(frame, "ALERTA: Olhos fechados!", (50, 80),
                     cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)
    else:
        # Borda Normal (Ciano Escuro/Azul)
        cv2.rectangle(frame, (0,0), (w,h), (0,40, 200,), 2)

    cv2.rectangle(frame, (0,0), (w,50), (20,20,20), -1)

    cv2.putText(frame, "Driver Drowsiness AI", (20, 35),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)

    now = datetime.now().strftime("%H:%M:%S")
    cv2.putText(frame, now, (w-150, 35),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
    
    # STATUS TEXTUAL
    status_text = "Status: Olhos Abertos"
    status_color = (0, 255, 0) # Verde
    
    if is_closed:
        status_text = "Status: Olhos Fechados"
        status_color = (0, 165, 255) # Laranja
        if timer >= MAX_TIME:
            status_text = "Status: SONOLENCIA CRITICA!"
            status_color = (0, 0, 255) # Vermelho
            
    cv2.putText(frame, status_text, (50, h - 30),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)


    # BARRA DE PROGRESSO
    if is_closed:
        progress = min(timer / MAX_TIME, 1.0) 
        
        # Posições e Dimensões da Barra (canto inferior direito)
        bar_w = 100
        bar_h = 15
        bar_x = w - bar_w - 50
        bar_y = h - bar_h - 30
        
        # Fundo da barra (Cinza Escuro)
        cv2.rectangle(frame, (bar_x, bar_y), 
                      (bar_x + bar_w, bar_y + bar_h), (50, 50, 50), -1)
        
        # Preenchimento da barra
        fill_color = (0, 255, 255) # Amarelo/Ciano
        if progress >= 1.0:
            fill_color = (0, 0, 255) # Vermelho
            
        cv2.rectangle(frame, (bar_x, bar_y), 
                      (bar_x + int(bar_w * progress), bar_y + bar_h), 
                      fill_color, -1)
                      
        # Borda da barra (Branca)
        cv2.rectangle(frame, (bar_x, bar_y), 
                      (bar_x + bar_w, bar_y + bar_h), (255, 255, 255), 1)

    return frame


while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    

    is_closed = detector.detect(frame)

    # CONTAGEM
    timer = 0
    if is_closed:
        if closed_start is None:
            closed_start = time.time()
        timer = time.time() - closed_start
    else:
        closed_start = None
        alert.stop()

    # ALERTA APÓS 2s
    if timer >= 3:
        alert.play()

    # DESENHO INTERFACE (CHAMADA SEM EAR)
    frame = draw_ui(frame, is_closed, timer)

    # Exibe o frame na janela
    cv2.imshow(WINDOW, frame)

    # Captura a tecla pressionada
    k = cv2.waitKey(1)

    # === F11 TELA CHEIA (CORRIGIDO) ===
    if k == 122: # F11
        fullscreen = not fullscreen
        if fullscreen:
            # Alterna para MODO TELA CHEIA
            cv2.setWindowProperty(WINDOW,
                cv2.WND_PROP_FULLSCREEN,
                cv2.WINDOW_FULLSCREEN)
        else:
            # Alterna para MODO JANELA
            cv2.setWindowProperty(WINDOW,
                cv2.WND_PROP_FULLSCREEN,
                cv2.WINDOW_NORMAL)
    # ==================================

    # ESC = SAIR
    if k == 27:
        break

# Limpeza e Encerramento
cap.release()
cv2.destroyAllWindows()
alert.stop()