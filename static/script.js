// セリフ
const tiger = [
    "お前の苦労をずっと見てたぞ.mp3",
    "本当によく頑張ったな.mp3",
    "ついに我慢が報われ莫大な富を得る.mp3",
    "これまでの苦労は全て水の泡だ.mp3",
    "節約ばかりの生活.mp3",
    "収入は増えず金は出てく一方.mp3",
    "将来に希望を持てず疲弊する日々.mp3",
    "そんな現実から抜け出す時が来た.mp3",
    "散らかり倒した狭い部屋を飛び出し.mp3",
    "贅沢で余裕のある生活を実現し.mp3",
  ];
  
  // ボタンコンテナを取得
  const buttonContainer = document.getElementById("button-container");
  
  // セリフごとにボタンを生成
  tiger.forEach(fileName => {
    // ボタンを作成
    const button = document.createElement("button");
    button.textContent = fileName.replace(".mp3", ""); // 拡張子を削除して表示
  
    // クリックイベントを設定
    button.addEventListener("click", () => {
      // 音声を再生
      const audio = new Audio(`templates/source/wav_source/${fileName}`);
      audio.play();
    });
  
    // コンテナにボタンを追加
    buttonContainer.appendChild(button);
  });
  




// 入力処理




  document.getElementById('audio-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const response = await fetch('/generate-audio', {
      method: 'POST',
      body: formData,
    });

    const resultContainer = document.getElementById('result-container');
    resultContainer.innerHTML = ''; // 前回の結果をクリア

    if (response.ok) {
      const data = await response.json();
      const audioUrl = data.audio_url;

      // 試聴用の再生ボタンを追加
      const audioElement = document.createElement('audio');
      audioElement.controls = true;
      audioElement.src = audioUrl;

      // ダウンロードリンクを追加
      const downloadLink = document.createElement('a');
      downloadLink.href = audioUrl;
      downloadLink.download = 'generated_audio.wav';
      downloadLink.textContent = 'ダウンロード';

      resultContainer.appendChild(audioElement);
      resultContainer.appendChild(document.createElement('br'));
      resultContainer.appendChild(downloadLink);
    } else {
      const errorData = await response.json();
      resultContainer.textContent = `エラー: ${errorData.error}`;
    }
  });