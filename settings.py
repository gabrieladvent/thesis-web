from pathlib import Path
import sys
from streamlit_webrtc import RTCConfiguration, ClientSettings

# Mendapatkan path default
FILE = Path(__file__).resolve()
# Mengambil direktori utama
ROOT = FILE.parent
#  Menambahkan jalur root ke daftar sys.path jika belum ada
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Mendapatkan relativ path dari direktori
ROOT = ROOT.relative_to(Path.cwd())

# Mode
HOME = 'Halaman Utama'
IMAGE = 'Gambar'
VIDEO = 'Video'
WEBCAM = 'Real-Time'
YOUTUBE = 'YouTube'

SOURCES_LIST = [HOME, IMAGE, VIDEO, YOUTUBE, WEBCAM]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'detect.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'detec_result.jpg'
IMAGE_HELP = IMAGES_DIR / 'detection-removebg-preview.png'

# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {
    'Video 1': VIDEO_DIR / 'video_1.mp4',
    'Video 2': VIDEO_DIR / 'video_2.mp4',
    'Video 3': VIDEO_DIR / 'video_3.mp4',
    'Video 4': VIDEO_DIR / 'video_4.mp4',
    'Video 5': VIDEO_DIR / 'video_5.mp4',
}

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'yolo-custom.pt'

# Webcam source
WEBCAM_PATH = 0

# konfigurasi live-cam
WEBRTC_CLIENT_SETTINGS = ClientSettings(
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False},
    )
# List clasname
CLASS_NAME = {
    0: "handphone", 
    1: "jam", 
    2: "mobil", 
    3: "orang", 
    4: "sepatu", 
    5: "tas"
            }
