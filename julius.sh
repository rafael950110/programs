
# マイクの設定
sudo amixer -c 0 sset 'Mic' 100%
# スピーカーの設定
sudo amixer -c 0 sset 'PCM' 100%


# 録音
arecord -D plughw:0,0 -f cd test.wav
# 再生
aplay -D plughw:0,0 test.wav
aplay -D plughw:0,0 /usr/share/sounds/alsa/*.wav

# 普通に起動
cd ~/julius/gramtools/mkdfa
sudo julius -C /home/pi/julius-kits/grammar-kit-4.3.1/hmm_mono.jconf -input mic -gram try -nostrip

# モジュールモードで起動
sudo modprobe snd-pcm-oss
cd ~/julius/gramtools/mkdfa
sudo julius -C /home/pi/julius-kits/grammar-kit-4.3.1/hmm_mono.jconf -nostrip -input mic -gram try -module &