from pydub import AudioSegment

def trim(input_file, output_file, start_time_ms, end_time_ms):

    # 読み込み
    audio = AudioSegment.from_file(input_file, format="mp3")
    
    # トリミング
    trimmed_audio = audio[start_time_ms:end_time_ms]
    
    # 新規保存
    trimmed_audio.export(output_file, format="mp3")
    print(f"作成完了: {output_file}")


# 設定
input_mp3 = "./gold_tiger.mp3"
output_mp3 = "./output9.mp3"
start_ms = 380
end_ms = 510

trim(input_mp3, output_mp3, start_ms, end_ms)


'''
0~190 お none ま
190~300 ま お え
300~380 え ま の
380~510 の え く
4150~7220
~11900
~17900
~20500
~23190
~25500
~28100
~30750
~33450
~37500
'''