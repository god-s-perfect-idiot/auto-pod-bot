import sys
import time 

sys.path.insert(0, 'helper')
from media_utils import get_audio, combine_audio
from chuckle_bot import get_chuckle


if(sys.argv[1] == 'chuckle'):
    for j in range(int(sys.argv[2])):
        jokes = []
        for i in range(9):
            jokes.append(get_chuckle())
            print('fetched chuckle', str(i+1))
            time.sleep(2)
        jokes_concat = ('\n\n').join(jokes)
        get_audio(jokes_concat, 'public/res.mp3', 'gtts')
        print('generated audio clip. saved as public/res.mp3')
        with open('tracker', 'r+') as f:
            pointer = f.read()
            f.seek(0)
            f.write(str(int(pointer)+1))
        combine_audio('public/cn_stock.mp4', 'public/res.mp3', 'public/Chuck Norris Jokes #'+pointer+'.mp4')
        print('generated final video')
        
