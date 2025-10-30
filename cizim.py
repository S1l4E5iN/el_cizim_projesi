import cv2
import mediapipe as mp
import numpy as np

# MediaPipe el modeli
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Kamerayı başlat
cap = cv2.VideoCapture(0)
canvas = None

# Başlangıç ayarları
draw_color = (255, 0, 0)  # Mavi
brush_thickness = 6
drawing = False

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    if canvas is None:
        canvas = np.zeros_like(frame)

    # RGB'ye dönüştür
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            # İşaret parmağı ve baş parmak ucu koordinatları
            index_x, index_y = lm_list[8]
            thumb_x, thumb_y = lm_list[4]

            # İki parmak arası mesafe
            distance = np.hypot(index_x - thumb_x, index_y - thumb_y)

            # Parmağın pozisyonuna göre çizim aktif/pasif
            if distance < 30:
                drawing = False
            else:
                drawing = True

            # Sürekli çizgi (önceki noktadan yeni noktaya)
            if drawing:
                if 'prev_x' in locals() and 'prev_y' in locals():
                    cv2.line(canvas, (prev_x, prev_y), (index_x, index_y), draw_color, brush_thickness)
                prev_x, prev_y = index_x, index_y
            else:
                prev_x, prev_y = None, None

    # Çizim katmanını kamerayla birleştir
    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    cv2.imshow("El Çizim Uygulamasi", frame)

    key = cv2.waitKey(1) & 0xFF

    # ESC -> çıkış
    if key == 27:
        break

    # C -> tuvali temizle
    elif key == ord('c'):
        canvas = np.zeros_like(frame)

    # E -> silgi modu
    elif key == ord('e'):
        draw_color = (0, 0, 0)
        brush_thickness = 50

    # B -> mavi kalem modu
    elif key == ord('b'):
        draw_color = (255, 0, 0)
        brush_thickness = 6

cap.release()
cv2.destroyAllWindows()
