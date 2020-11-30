print ('EX 021. Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.')
# PRIMEIRO COPIE UMA MÚSICA MP3 PARA SEU DIRETÓRIO OND EESTÃO SALVOS OS ARQUIVOS PY
from pydub import AudioSegment
from pydub.playback import play

# UTILIZEI A MUSICA "DYNAMITE" PRESENTE NO MEU DIRETÓRIO, SUBSTITUA O NOME ABAIXO PARA O DE SUA ESCOLHA
song = AudioSegment.from_mp3("BTS - Dynamite.mp3")
play(song)
# AQUI FIZ UTILIZANDO "PYDUB", MAS EXISTE A BIBLIOTECA "PLAYSOUND" E TAMBÉM "PYGAME".
