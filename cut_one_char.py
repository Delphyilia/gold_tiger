import os
from pydub import AudioSegment

def get_next_filename(base_name, extension):
    """
    base_name: str - The base name of the output file (e.g., "output")
    extension: str - The file extension (e.g., "mp3")
    
    Returns the next available filename with a sequential number.
    """
    index = 1
    while True:
        filename = f"{base_name}{index}.{extension}"
        if not os.path.exists(filename):
            return filename
        index += 1

def trim(input_file, base_output_name, start_time_ms, end_time_ms):
    """
    input_file: str - Path to the input audio file.
    base_output_name: str - Base name for the output file (e.g., "output").
    start_time_ms: int - Start time in milliseconds.
    end_time_ms: int - End time in milliseconds.
    """
    # Read the audio file
    audio = AudioSegment.from_file(input_file, format="mp3")

    # Trim the audio
    trimmed_audio = audio[start_time_ms:end_time_ms]

    # Generate the next available filename
    output_file = get_next_filename(base_output_name, "mp3")

    # Export the trimmed audio
    trimmed_audio.export(output_file, format="mp3")
    print(f"作成完了: {output_file}")

# Settings
input_mp3 = "./gold_tiger.mp3"
base_output_name = "./output"
start_ms = 3820
end_ms = 4238
trim(input_mp3, base_output_name, start_ms, end_ms)


'''
おまえのく
0~190     お none ま
190~300   ま お え
300~380   え ま の
380~510   の え く
510~630   く の ろ
630~920   ろ く ず    くろうをず　が　連音して　くろーーず　に聞こえるのでまとめる
920~1140  ず ろ と    ずっと　だが　ずと　にしか聞こえないので　っ　は省略
1140~1290 と ず み
1290~1390 み と て
1390~1510 て み い
1510~1590 い て た      聞こえにくい
1590~1730 た い ぞ
1730~1900 ぞ た ほ       ぞ　のあとは少しまがあく
1900~2370               無声
2370~2550 ほ ぞ ん
2550~2610               「ん」　が　直前の「ほ」に吸収されてほぼ聞こえない
2610~2710 と n う
2710~2810 う と に
2810~2910 に う よ
2910~3030 よ に く
3030~3170 く よ が
3170~3270 が く ん
3270~3380 ん が ば
3380~3480 ば ん っ
3480~3600 っ ば た
3600~3710 た っ な
3710~3820 な た n
3820~4238 がおー
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