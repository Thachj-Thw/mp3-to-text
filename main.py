import speech_recognition as sr
import subprocess
import os


folder = os.path.dirname(os.path.normpath(__file__))
converter = os.path.join(folder, "ffmpeg", "bin", "ffmpeg.exe")

path_mp3 = os.path.join(folder, "input.mp3")
path_wav = os.path.join(folder, "audio.wav")

if os.path.exists(path_wav):
    os.unlink(path_wav)
# convert mp3 to wav
subprocess.call([converter, "-i", path_mp3, path_wav], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

# speech recognition
r = sr.Recognizer()
data = sr.AudioFile(path_wav)

with data as source:
    audio = r.record(source)
try:
    txt = r.recognize_google(audio, language="vi-VN")
except sr.UnknownValueError:
    txt = "noise!!!"
print(txt)

# save as text.txt
with open(os.path.join(folder, "text.txt"), mode="w", encoding="utf-8") as file:
    file.write(txt)
