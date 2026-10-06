#!/usr/bin/env python3
"""Memory-conscious IndexTTS-2.5 inference for Google Colab (L4)."""
import argparse, json, random
from pathlib import Path
import numpy as np, torch
from indextts.infer_v2_5 import IndexTTS2

def parse_vector(raw):
    raw = (raw or "").strip()
    if not raw:
        return None
    values = json.loads(raw) if raw.startswith("[") else [x for x in raw.replace("，", ",").split(",")]
    values = [float(x) for x in values]
    if len(values) != 8 or any(not 0 <= x <= 1 for x in values):
        raise ValueError("emo_vector 需要 8 个 0~1 之间的数字")
    return values

p = argparse.ArgumentParser()
p.add_argument("--model_dir", required=True)
p.add_argument("--prompt_wav", required=True)
p.add_argument("--text", required=True)
p.add_argument("--lang", choices=["ZH", "EN", "JA", "ES", "AR"], default="ZH")
p.add_argument("--output", required=True)
p.add_argument("--duration_factor", type=float, default=1.0)
p.add_argument("--emo_vector", default="")
p.add_argument("--emo_audio", default="")
p.add_argument("--emo_alpha", type=float, default=0.8)
p.add_argument("--seed", type=int, default=1234)
a = p.parse_args()
if not 0.5 <= a.duration_factor <= 2.0: raise ValueError("duration_factor 需在 0.5~2.0")
if not 0.0 <= a.emo_alpha <= 1.0: raise ValueError("emo_alpha 需在 0~1")

random.seed(a.seed); np.random.seed(a.seed); torch.manual_seed(a.seed)
if torch.cuda.is_available(): torch.cuda.manual_seed_all(a.seed)
use_bf16 = bool(torch.cuda.is_available() and torch.cuda.is_bf16_supported())
print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU", "| BF16:", use_bf16)

m = Path(a.model_dir)
tts = IndexTTS2(cfg_path=str(m / "config.yaml"), model_dir=str(m), use_bf16=use_bf16,
                use_cuda_kernel=False, use_deepspeed=False, use_accel=False,
                use_torch_compile=False, use_qwen_emo=False)
vec = parse_vector(a.emo_vector)
if vec is not None:
    vec = tts.normalize_emo_vec(vec, apply_bias=True)
out = Path(a.output); out.parent.mkdir(parents=True, exist_ok=True)
tts.infer(spk_audio_prompt=a.prompt_wav, text=a.text, lang=a.lang, output_path=str(out),
          emo_audio_prompt=a.emo_audio or None, emo_vector=vec, emo_alpha=a.emo_alpha,
          use_random=False, duration_factor=a.duration_factor, verbose=True)
print("Saved:", out.resolve())
