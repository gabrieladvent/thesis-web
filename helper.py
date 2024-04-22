from ultralytics import YOLO
import time
import streamlit as st
import cv2
from pytube import YouTube
from tempfile import NamedTemporaryFile

from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, WebRtcMode

import settings


def load_model(model_path):
    model = YOLO(model_path)
    return model


def showDetectFrame(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    """
    Algoritma.

    Args:
    - conf (float): Confidence threshold for object detection.
    - model (YoloV8): A YOLOv8 object detection model.
    - st_frame (Streamlit object): A Streamlit object to display the detected video.
    - image (numpy array): A numpy array representing the video frame.
    - is_display_tracking (bool): A flag indicating whether to display object tracking (default=None).

    Returns:
    None
    """

    # Resize the image 720x405.
    # image = cv2.resize(image, (720, int(720*(9/16))))

    # Predict the objects in the image using the YOLOv8 model
    res = model.predict(image, conf=conf)

    # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   )

def play_youtube(conf, model):
    """

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None

    Raises:
        None
    """
    source_youtube = st.text_input("Silahkan Masukan Link YouTube")

    if st.button('Deteksi'):
        try:
            yt = YouTube(source_youtube)
            stream = yt.streams.filter(file_extension="mp4", res=720).first()
            vid_cap = cv2.VideoCapture(stream.url)

            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    showDetectFrame(conf,
                                    model,
                                    st_frame,
                                    image
                                   )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Ada Kesalahan Saat Memproses Link: " + str(e))


def play_webcam(conf, model):
    """
    Algoritma.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None

    Raises:
        None
    """
    source_webcam = settings.WEBCAM_PATH
    
    if st.button('Deteksi Secara Langsung'):
        try:
            vid_cap = cv2.VideoCapture(source_webcam)
            st_frame = st.empty()
            stop_button = st.button('Berhenti')
            while (vid_cap.isOpened() and not stop_button):
                success, image = vid_cap.read()
                if success:
                    showDetectFrame(conf,
                                    model,
                                    st_frame,
                                    image
                                   )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.error("Ada Kesalahan Saat Proses Deteksi: " + str(e))


import av


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")

def live (model, conf):
    webrtc_streamer(key="example", video_frame_callback=video_frame_callback)



def process_uploaded_video(conf, model):
    uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    
    if uploaded_video is not None:
        with NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
            temp_file.write(uploaded_video.read())
            temp_video_path = temp_file.name
        
        with open(temp_video_path, 'rb') as video_file:
            video_bytes = video_file.read()
        if video_bytes:
            st.video(video_bytes)
            
        if st.button('Deteksi'):
            try:
                vid_cap = cv2.VideoCapture(temp_video_path)
                st_frame = st.empty()
                while (vid_cap.isOpened()):
                    success, image = vid_cap.read()
                    if success:
                        showDetectFrame(conf,
                                        model,
                                        st_frame,
                                        image
                                       )
                    else:
                        vid_cap.release()
                        break
            except Exception as e:
                st.error("Error loading video: " + str(e))
    


def play_stored_video(conf, model):
    """
    Plays a stored video file. Tracks and detects objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None

    Raises:
        None
    """
    source_vid = st.selectbox(
        "Silahkan Pilih Video yang Sudah Disediakan", settings.VIDEOS_DICT.keys())

    with open(settings.VIDEOS_DICT.get(source_vid), 'rb') as video_file:
        video_bytes = video_file.read()
    if video_bytes:
        st.video(video_bytes)

    if st.button('Deteksi Video'):
        try:
            vid_cap = cv2.VideoCapture(
                str(settings.VIDEOS_DICT.get(source_vid)))
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    showDetectFrame(conf,
                                    model,
                                    st_frame,
                                    image
                                   )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.error("Ada Kesalahan Saat Proses Video: " + str(e))
            
def take_picture(conf, model):
    picture = st.camera_input("Silahkan Mengambil Gambar")

    if picture:
        with NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
            temp_file.write(picture.read())
            temp_pict_path = temp_file.name
            
        if st.button('Deteksi Foto'):
            try:
                vid_cap = cv2.VideoCapture(temp_pict_path)
                st_frame = st.empty()
                while (vid_cap.isOpened()):
                    success, image = vid_cap.read()
                    if success:
                        showDetectFrame(conf,
                                        model,
                                        st_frame,
                                        image
                                       )
                    else:
                        vid_cap.release()
                        break
            except Exception as e:
                st.error("Error loading video: " + str(e))

def helpFunction():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')
    with col2:
        st.image(str(settings.IMAGE_HELP))
    with col3:
        st.write(' ')
        
    html_temp_about1= """
                <div style="padding:10px; text-align:center;">
                        <h2>
                            DETEKSI OBJEK
                        </h2>
                    </div>
                    """
    st.markdown(html_temp_about1, unsafe_allow_html=True)

    html_temp4 = """
                <div style="padding:10px">
                    <p>
                        Website ini adalah hasil dari penelitian saya tentang <strong>"Pengengalan Objek Untuk Pembelajaran Anak-Anak"</strong>.
                    </p>
                    <p>
                        Website ini dibuat dengan bantuan sebuah alat bernama <a rel="noopener" href="https://streamlit.io" target="_blank">Streamlit</a>. Saya juga menggunakan teknologi <a rel="noopener" href="https://docs.ultralytics.com" target="_blank">You Only Look Once</a> (YOLO) versi 8 dari <a rel="noopener" href="https://www.ultralytics.com" target="_blank">Ultralytics</a> untuk mengembangkan modelnya.
                    </p>
                    <p>
                        Dalam penelitian ini, ada 6 benda yang bisa kita kenali, yaitu: <strong>Handphone, Jam, Mobil, Orang, Sepatu,</strong> dan <strong>Tas</strong>. Website ini memiliki 4 cara untuk mengenal benda, yaitu: <strong>mengupload foto</strong>, <strong>mengupload video</strong>, <strong>menyalin link YouTube</strong>, dan <strong>deteksi langsung</strong>.
                    </p>
                    <p>
                        Saya berharap website ini dapat membantu teman-teman, terutama anak-anak usia 3 - 5 tahun, untuk lebih cepat mengenal benda-benda di sekitarnya.
                    </p>
                    <p>
                        Setelah mencoba website ini, tolong isi <a rel="noopener" href="https://forms.gle/k4ULtjY2ShkAegtm8" target="_blank">kuesioner</a> untuk memberikan masukan kepada saya.
                    </p>
                    <p>
                        Jika ada yang ingin ditanyakan, silakan hubungi saya via <a rel="noopener" href="mailto:bie.ritan112@gmail.com">Email</a>.
                    </p>
                    <p>
                        Terima kasih dan Semoga Menyenangkan!
                    </p>

                </div>
                
                <br>
                
                <div>
                    <p>
                        Fitur yang belum berjalan: Mode Real-Time
                    </p>
                </div>
                """

    st.markdown(html_temp4, unsafe_allow_html=True)