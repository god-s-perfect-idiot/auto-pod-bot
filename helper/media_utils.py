from gtts import gTTS
import pyttsx3
import moviepy.editor as mpe

def get_audio(text, output_path, engine='gtts'):
    if(engine == 'gtts'):
        tts = gTTS(text)
        tts.save(output_path)
    # elif(engine == 'pyttsx3'):
    #     engine = pyttsx3.init()
    #     voices = engine.getProperty('voices')
    #     engine.setProperty('rate', 90)
    #     engine.setProperty('voice', voices[17].id)
    #     engine.say('The quick brown fox jumped over the lazy dog.')
    #     engine.runAndWait() 

def combine_audio(vidname, audname, outname, fps=60): 
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)