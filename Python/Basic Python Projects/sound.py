import sounddevice as sd
import scipy.io.wavfile as wav

# Ask user for recording time
sec = int(input("Record seconds: "))

# Audio settings
fs = 44100     # Sample rate (44.1 kHz CD quality)

print("Recording...")

# Record audio
audio = sd.rec(int(sec * fs), samplerate=fs, channels=2)
sd.wait()      # Wait until recording is finished

# Save the file
wav.write("record.wav", fs, audio)

print("Saved as record.wav")
