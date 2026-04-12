# ML to Text-to-Image — Study Plan

**Domain**: Machine Learning → Deep Learning → Generative Models → Text-to-Image
**Owner**: Nufa (Farahana Suhaimi)
**Created**: 2026-04-12
**Background**: CNN/deep learning experience (PhD — Medical Image Processing). Needs basics refresher before advancing.
**End Goal**: Understand and build something with text-to-image models (e.g., Stable Diffusion)
**Study Mode**: Dedicated study blocks

---

## Overview

Text-to-image is not purely LLM territory. Models like Stable Diffusion combine:
- A **text encoder** (transformer/LLM side) — understands the prompt
- A **diffusion process** (image generation side) — generates the image from noise

Nufa's CNN background gives a head start on the image side. The gap is transformers, embeddings, and diffusion theory.

---

## Phase 1 — ML Basics Refresher

**Goal**: Rebuild intuition, not memorize formulas.

| Topic | Description |
|-------|-------------|
| Linear & logistic regression | Loss functions, gradient descent |
| Backpropagation | How gradients flow through a network |
| Regularization | Overfitting, dropout, L1/L2 |
| Evaluation | Train/val/test split, metrics |

**Resources**:
- Andrew Ng — Machine Learning Specialization (Coursera)
- fast.ai — Practical Deep Learning for Coders (Part 1)

**Milestone**: Comfortable explaining why a model overfits and how to fix it.

---

## Phase 2 — Deep Learning Refresher

**Goal**: Understand how text gets represented as vectors. CNNs are light review only.

| Topic | Description |
|-------|-------------|
| CNNs | Light review — Nufa knows this |
| Embeddings | How words/tokens become vectors |
| Attention mechanism | The core idea behind transformers |
| Transformers | Architecture end-to-end |

**Resources**:
- Andrej Karpathy — "Neural Networks: Zero to Hero" (YouTube series)
- Paper: "Attention is All You Need" (Vaswani et al., 2017)
- HuggingFace NLP Course (free, online)

**Milestone**: Able to explain what a transformer does without looking it up.

---

## Phase 3 — Generative Models

**Goal**: Understand how images are generated from noise.

| Topic | Description |
|-------|-------------|
| VAEs | Variational Autoencoders — latent space concept |
| GANs | Brief context only — historical, less used now |
| Diffusion Models | Core of modern text-to-image — denoising process |

**Resources**:
- Paper: "Denoising Diffusion Probabilistic Models" (Ho et al., 2020)
- Lilian Weng's blog — "What are Diffusion Models?" (lilianweng.github.io)
- HuggingFace `diffusers` library documentation

**Milestone**: Able to explain what diffusion models do and why they replaced GANs.

---

## Phase 4 — Text-to-Image

**Goal**: Understand the full architecture and build something real.

| Topic | Description |
|-------|-------------|
| CLIP | How text and image are linked in a shared embedding space |
| Stable Diffusion architecture | UNet + VAE + text encoder working together |
| Inference | Run text-to-image locally with HuggingFace diffusers |
| Fine-tuning | Textual Inversion or DreamBooth — adapt to custom concepts |

**Resources**:
- HuggingFace `diffusers` library + Stable Diffusion pipeline docs
- Paper: "High-Resolution Image Synthesis with Latent Diffusion Models" (Rombach et al., 2022)
- Fast.ai — Practical Deep Learning Part 2 (covers diffusion)

**Milestone**: Run a Stable Diffusion pipeline locally. Generate an image from a custom prompt. Attempt one fine-tuning experiment.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Primary language |
| PyTorch | Deep learning framework (already in use) |
| HuggingFace `diffusers` | Text-to-image pipeline |
| HuggingFace `transformers` | Tokenizers and text encoders |
| Jupyter Notebook | Experimentation |

**Hardware**: Nufa's home PC has a GPU — use it for local training/inference.

---

## Study Block Structure (Suggested)

Each study block:
1. **Review** — 10 min recap of last block
2. **Learn** — read/watch new material
3. **Code** — implement or experiment
4. **Log** — save diary entry documenting what clicked and what didn't

---

## Progress Tracker

| Phase | Status | Completed |
|-------|--------|-----------|
| Phase 1 — ML Basics | In progress | — |
| Phase 2 — Deep Learning | Not started | — |
| Phase 3 — Generative Models | Not started | — |
| Phase 4 — Text-to-Image | Not started | — |

### Phase 1 Progress Log

| Date | File | Topics Covered |
|------|------|----------------|
| 2026-04-12 | `synthetic_data.py` | Linear regression, MSE loss, backprop (`loss.backward()`), autograd with `requires_grad=True` |

---

*Update the Progress Tracker as each phase completes. Log diary entries per study block.*
