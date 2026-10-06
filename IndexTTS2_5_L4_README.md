# IndexTTS-2.5 on Google Colab Pro（L4）

[![在 Colab 中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zencolab/colab/blob/main/IndexTTS2_5_L4_Colab.ipynb)

适用于 **Google Colab Pro + NVIDIA L4** 的 IndexTTS-2.5 安装与使用 Notebook。

## 文件

- [`IndexTTS2_5_L4_Colab.ipynb`](IndexTTS2_5_L4_Colab.ipynb) — 完整、可逐格运行的 Colab Notebook（推理脚本已内置，不再依赖外部 .py）

## 更新（2026-10）

- 模型：`IndexTeam/IndexTTS-2.5`（官方当前最新模型）
- 代码默认固定到官方 `main` 最新提交 `d9e41aa`，包含 v2.5.0 之后的修复（结尾咔哒声淡出、`do_sample` 透传、推理提速、WebUI 修复与 `--share`）；可将 `CODE_REF` 改回 `v2.5.0`
- 修复 Colab 报错：Colab 预设的 `UV_PRERELEASE=`（空值）、`UV_CONSTRAINT`、`UV_SYSTEM_PYTHON`、`MPLBACKEND`、`PYTHONPATH` 会让 `uv sync` 报 `a value is required for '--prerelease'` 或导致 matplotlib 后端错误；现在所有 uv 命令都在清理后的环境中运行
- 上传的参考音频自动用 ffmpeg 转为单声道 WAV（支持 mp3/m4a/flac）
- WebUI 直接使用官方 `webui.py --share`

## 功能

- 使用 `uv sync --extra webui --frozen` 安装官方锁定依赖（PyTorch 2.8 + CUDA 12.8）
- L4 上自动启用 BF16
- 自动下载 IndexTTS-2.5 主模型与辅助模型
- 支持中文、英文、日语、西班牙语、阿拉伯语
- 支持音色克隆、独立情感音频、8 维情感向量、语速控制与发音标注
- 可选 Google Drive 模型缓存
- 可选 Gradio 公网临时 WebUI

## 快速开始

1. 点击上方 **在 Colab 中打开**。
2. 在 Colab 选择「运行时 → 更改运行时类型 → GPU」，优先选择 **L4**。
3. 从上到下运行单元格。
4. 上传一段 5–15 秒、已获授权的清晰参考音频。
5. 修改文本、语言和可选情感参数，运行推理单元格。

## 版本与来源

- IndexTTS 代码：<https://github.com/index-tts/index-tts>
- 中文文档：<https://github.com/index-tts/index-tts/blob/main/docs/README_zh.md>
- 模型：<https://huggingface.co/IndexTeam/IndexTTS-2.5>

## 合规与许可

只使用本人或已获明确授权的声音。请遵守适用法律，并在使用前阅读上游仓库的 `LICENSE`、`LICENSE_ZH.txt` 和 `DISCLAIMER`。本仓库不包含或重新分发模型权重。
