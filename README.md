# Speech Recognition using Vosk models

A speech recognition python script that uses Python and the Vosk module. The script will output the word along with the start and stop time and confidence percentage.

## Requirements

* Python version: 3.5-3.9 (**IMPORTANT**)
* pip version: 20.3 and newer
* Vosk module (https://alphacephei.com/vosk/install)
* (Optional) Create conda environment which contains python version along with vosk in order to prevent the need to downgrade your currently installed python version.

## IDE Preference (Optional)

* Visual Studio Code (https://code.visualstudio.com/download)
    * Will make your life easier when it comes to debugging and running the script.

## Installation
### Step 1: Install Vosk module
```bash
pip install vosk
```
### Step 2: Download Vosk model
```bash
ttps://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
```
### Step 3: Unzip Vosk model

### Step 4: Download speech recognition script

### Step 5: Edit speech recognition script
```bash
model_path = "/PATH/TO/VOSK/MODEL"
# Example: model_path = "C:/Users/JohnDoe/Desktop/vosk-model-small-en-us-0.15"
```
```bash
audio_filename = glob.glob("/PATH/TO/FOLDER/AUDIO/FILES/*n##*.wav")
# Example: audio_filename = glob.glob("C:/Users/JohnDoe/Desktop/AudioFiles/*n##*.wav")
# Note: The # in n## would be changed to the number of the audio file. For example, if the audio file is named "audio1.wav", then the # would be changed to 1.
```

### Step 6: Run speech recognition script
```bash
Output will be formatted as follows:
Word, Start Time (Secs), Stop Time (Secs), Confidence Percentage
```
## Installation using Conda (Optional)
### Step 1: Create conda environment
```bash
conda create --name SpeechRecognition python=3.9
# Note: The python version can be changed to any version that is supported by Vosk.
# Note: Name of environment can be changed to anything you want.
```

### Step 2: Activate conda environment
```bash
conda activate SpeechRecognition
```
### Step 3: Follow steps 1-6 from the Installation section.