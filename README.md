# KerasOCRTextBoxRecognizer
Keras-OCR Text Box Recognizer

This a simple command line client to Keras-OCR Text Recognizer.<br>

<h2> 
1 Install python venv
</h2>
Please create a python3 venv on Windows 11.<br>
and install it. We use Windows11 OS.<br>
<pre>
>python -m venv c:/py38-keras-ocr
>cd ./py38-keras-ocr
>scripts/activate
</pre>

<br>
<h2>
2 Install python packages
</h2>
Please clone this repository to your local PC.<br>
We use Python3 venv on Windows11 OS.
<br>
<pre>
>mkdir c:/keras-ocr
>cd c;/keras-ocr
>git clone https://github.com/zephyr-antillia/KerasOCRTextBoxRecognizer.git
>cd KerasOCRTextBoxRecognizer
>pip install requirements.txt
</pre>


<h2>
3 Sample Program
</h2>
Please open Windows Powershell console, and run the following command in the console window.<br>
<pre>
> python KerasOCRTextBoxRecognizer.py
</pre>

<br>
This <a href="./KerasOCRTexBoxRecognizer.py">KerasOCRTextBoxRecognizer.py</a> script reads the recognition.conf file.<br>
<pre>
[parameter]
images_dir   = "./samples"
output_dir   = "./preprocessed"
;image_format = ".png"

[preprocessor]
preprocessing    = True
gray_image       = True
image_scaling    = 3
contrast         = 1.5
sharpness        = 3

[visualizer]
font_name        = "arial.ttf"
draw_boundingbox = True
expanding_ratio  = 1.0
scaling_on_nonpreprocessing = 3
</pre>

Example 1: ARTIZON_MUSEUM.png<br>
<img src="./samples/ARTIZON_MUSEUM.png" width="1024" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./preprocessed/preprocessed_scaling_3_contrast_1.5_sharpness_3_ARTIZON_MUSEUM.png"
     width="1024" height="auto">
<br>

Example 2: Inference_Result.png<br>
<img src="./samples/Inference_Result.png" width="1024" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./preprocessed/preprocessed_scaling_3_contrast_1.5_sharpness_3_Inference_Result.png"
     width="1024" height="auto">
<br>

Example 3: RoadSign.png<br>
<img src="./samples/RoadSign.png" width="1024" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./preprocessed/preprocessed_scaling_3_contrast_1.5_sharpness_3_RoadSign.png"
     width="1024" height="auto">
<br>

Example 4: RoadSign_US.png<br>
<img src="./samples/RoadSign_US.png" width="1024" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./preprocessed/preprocessed_scaling_3_contrast_1.5_sharpness_3_RoadSign_US.png"
     width="1024" height="auto">
<br>

Example 5: SDGS.png<br>
<img src="./samples/SDGS.png" width="1024" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./preprocessed/preprocessed_scaling_3_contrast_1.5_sharpness_3_SDGS.png"
     width="1024" height="auto">
<br>

Example 6: USA_RoadSigns.png<br>
<img src="./samples/USA_RoadSigns.png" width="1024" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./preprocessed/preprocessed_scaling_3_contrast_1.5_sharpness_3_USA_RoadSigns.png"
     width="1024" height="auto">
<br>


Example 7: VSCodeScreenShot.png<br>
<img src="./samples/VSCodeScreenShot.png" width="1024" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./preprocessed/preprocessed_scaling_3_contrast_1.5_sharpness_3_VSCodeScreenShot.png"
     width="1024" height="auto">
<br>



