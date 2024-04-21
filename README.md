<img src="https://github.com/gabrieladvent/nice-one/blob/main/assets/pic.png" > 


# <span> Object Detection With YOLOv8 Algorithm </span>

This repository is the  finished product of my final project in college that combines object detection using **YOLOv8**, an object detection algorithm, and **Streamlit**, a popular Python framework for creating interactive web applications. This project has four different detection modes, including realtime mode, detection mode from YouTube URLs, as well as detection mode from videos and static images.

## <span>WebApp Demo</span>

Thanks to [Streamlit](<https://github.com/streamlit/streamlit>) team for providing cloud uploads so that I can make this webApp more accessible to the general public.

This app is up and running on Streamlit cloud server!!! You can check the demo of this web application on this link 
[Object Detection With YOLOv8 Algorithm](https://web-detection-thesis.streamlit.app/)

## Requirements

Python 3+ \
YOLOv8 \
Streamlit

```bash
pip install ultralytics streamlit pytube
```

## Installation

- Clone the repository: git clone <https://github.com/CodingMantras/yolov8-streamlit-detection-tracking.git>

- Change to the repository directory: `cd yolov8-streamlit-detection-tracking`

- Create `weights`, `videos`, and `images` directories inside the project.

- Download the pre-trained YOLOv8 weights from (<https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt>) and save them to the `weights` directory in the same project.

- Or if you have a model created with yolov8, you can save to the `weights` directory in the same project.

## Usage

- Run the app with the following command: `streamlit run app.py`

- The app will be opened in a new browser window.

### Detection on images

- The default image with its objects-detected image is displayed on the main page.

- Select a source. (radio option selection `Image`).

- Upload an image by clicking on the "Browse files" button.

- Click the `Deteksi` button to run the object detection algorithm on the uploaded image with the selected confidence threshold.

- The output  with objects detected will be displayed on the page.

## Detection in Videos

- I have two options for video detection, namely using the videos that I have prepared in this project, or uploading them myself

- If you choose to upload the video yourself, then please select the `upload tab`

- After  The preview video has been displayed, you can click the `Deteksi` button then the detection results will be displayed

- If you choose to use a video that I have prepared, you can select the `sumber asal tab`

- Then you have to choose 1 of the 4 videos that have been prepared

- Click on `Deteksi` button and detection will start on the selected video.

### Detection on YouTube Video URL

- Select the source as YouTube

- Copy paste the url inside the text box.

- The detection task will start on the YouTube video url

## Acknowledgements

This app uses [YOLOv8](<https://github.com/ultralytics/ultralytics>) for object detection algorithm and [Streamlit](<https://github.com/streamlit/streamlit>) library for the user interface.

### Disclaimer

Please note that this project is intended for educational purposes only and is the final result of my thesis. so it should not be used in production environments

**Hit star ⭐ if you like this repo!!!**
