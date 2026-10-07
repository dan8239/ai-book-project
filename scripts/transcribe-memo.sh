#!/usr/bin/env bash
# Transcribe a voice memo locally with mlx-whisper (Apple silicon, no ffmpeg needed).
# Writes "<memo name>.txt" next to the .m4a and prints the memo's fingerprint
# (duration + bytes) for references/voice-memo-log.md.
#
# Usage: ./scripts/transcribe-memo.sh ~/Downloads/"Deli Belli.m4a"
set -euo pipefail

memo="$1"
[ -f "$memo" ] || { echo "No such file: $memo" >&2; exit 1; }

venv="$HOME/.cache/book-whisper-venv"
if [ ! -x "$venv/bin/python" ]; then
  python3 -m venv "$venv"
  "$venv/bin/pip" install -q mlx-whisper numpy
fi

out="${memo%.*}.txt"
if [ -f "$out" ]; then
  echo "Transcript already exists: $out" >&2
else
  wav="$(mktemp -t memo).wav"
  afconvert -f WAVE -d LEI16@16000 -c 1 "$memo" "$wav"
  "$venv/bin/python" - "$wav" "$out" <<'EOF'
import sys, wave, numpy as np, mlx_whisper
wav, out = sys.argv[1], sys.argv[2]
w = wave.open(wav)
audio = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
r = mlx_whisper.transcribe(audio, path_or_hf_repo="mlx-community/whisper-large-v3-turbo", language="en")
open(out, "w").write("(Transcribed locally by mlx-whisper large-v3-turbo.)\n\n" + r["text"].strip() + "\n")
EOF
  rm -f "$wav"
  echo "Wrote $out"
fi

dur=$(afinfo "$memo" | awk '/estimated duration/ {printf "%d", $3}')
bytes=$(stat -f '%z' "$memo")
echo "Fingerprint: ${dur}s / ${bytes} bytes"
