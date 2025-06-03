# 🧠 Latent Space Surgery

**Latent Space Surgery** is a research-driven generative modeling project focused on 
*precisely editing the latent representations* of deep models like GANs and VAEs. It allows 
independent manipulation of high-level features such as memory, emotion, and texture through 
interpretable, disentangled latent subspaces.

---

## 🚀 Project Goals

* 🎯 Design **disentangled latent spaces** where individual vectors correspond to 
interpretable attributes.
* 🛠️ Implement **modular editors** for memory, emotion, and texture manipulation.
* 🡬 Enable **latent traversal, interpolation, and surgery** on real and generated images.
* 📊 Visualize and evaluate edits using FID, CLIP, and disentanglement metrics.

---

## 🔍 Example Use Cases

* 🔄 Convert an image's emotional tone (e.g., from sad to joyful) without changing identity.
* 🧠 Simulate memory "insertion" or recall in a character generation pipeline.
* 🌊 Modify textures (e.g., cloth → fur, concrete → moss) in a localized and realistic 
way.

---
## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/nikosane/latent-space-surgery.git
cd latent-space-surgery

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Edit your settings in `config/config.yaml`:

```yaml
model: stylegan2
latent_dim: 512
attributes: ['emotion', 'texture', 'memory']
dataset: celeba_hq
```

---

## 🧪 Usage

### 🏁 Train base model

```bash
python scripts/train_gan.py
# or
python scripts/train_vae.py
```

### ✂️ Perform Latent Space Surgery

```bash
python scripts/edit_latent.py --attribute emotion --target happy
```

### 📊 Evaluate Results

```bash
python scripts/evaluate.py --metrics fid,clip,disentangle
```

---

## 🧠 Core Concepts

* **Latent Space Surgery:** Editing a vector in latent space without disturbing unrelated 
features.
* **Disentanglement:** Making latent directions independent and interpretable.
* **Projection:** Mapping real images back into latent space for manipulation.

---

## 🧪 Models & Techniques Used

* StyleGAN2, β-VAE, InfoGAN
* PCA/ICA-based disentanglement
* CLIP similarity and Fourier texture descriptors
* Attribute-specific vector offsets

---

## 📃 Research Reference

* *Disentangled Representations in VAEs* – Higgins et al.
* *GANSpace: Discovering Interpretable GAN Controls* – Härkönen et al.
* *StyleGAN2-ADA* – NVIDIA

---

## ✅ To-Do

* [ ] Add GUI-based latent editor
* [ ] Extend to video GANs with temporal smoothing
* [ ] Include text-guided editing (CLIP)

---

## 🤝 Contributing

Pull requests, discussions, and feature ideas are welcome. Please ensure changes are tested 
and documented.

---

## 📄 License

MIT License. See `LICENSE` file for details.

---

## 🙌 Acknowledgements

Thanks to open-source pioneers in generative modeling and the contributors to StyleGAN, 
β-VAE, and CLIP.

---
# 
Latent-space-surgery
