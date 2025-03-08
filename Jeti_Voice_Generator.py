# Import the required module for text 
# to speech conversion
from gtts import gTTS

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def text_to_speech(text, lang='de', output_wav='output.wav'):
    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang=lang)
    
    # Save the speech as a temporary mp3 file
    temp_mp3 = 'temp.mp3'
    tts.save(temp_mp3)
    
    # Convert the mp3 file to wav format using pydub
    audio = AudioSegment.from_mp3(temp_mp3)
    audio.export(output_wav, format="wav")
    
    # Clean up the temporary mp3 file
    os.remove(temp_mp3)
    
    print(f"Speech saved as {output_wav}")


words = [["CS_Motor_ein", "Motor ein", "de"],
            ["CS_Motor_aus", "Motor aus", "de"],
            ["CS_Klappen_Start", "Startklappen", "de"],
            ["CS_Klappen_Lande", "Landeklappen", "de"],
            ["CS_Klappen_Aus", "Klappen aus", "de"],
            ["CS_Fahrwerk_ein", "Fahrwerk ein", "de"],
            ["CS_Fahrwerk_aus", "Fahrwerk aus", "de"],
            ["CS_Low_Rates", "Low Rates", "en"],
            ["CS_Mid_Rates", "Mid Rates", "en"],
            ["CS_High_Rates", "High Rates", "en"]]
            


# Example usage
for r in words:
    text_to_speech(r[1], r[2], output_wav=r[0] + '.wav')

