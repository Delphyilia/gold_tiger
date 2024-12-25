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
output_mp3 = "./output7.mp3"
start_ms = 37500
end_ms = 40100

trim(input_mp3, output_mp3, start_ms, end_ms)


'''
0~2200
2200~4150
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