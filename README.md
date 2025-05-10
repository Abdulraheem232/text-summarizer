
---

```markdown
# 📝 Text Summarizer using T5 Transformer

This project is a **Text Summarization tool** built using the **T5 Transformer model**, powered by HuggingFace's Transformers library. It includes a **Streamlit-based Web UI** and supports custom training using pretrained T5 models.

---

## 🚀 Features

- Summarize large texts using the T5 transformer
- Pretrained and fine-tuned model support
- **Interactive Streamlit Web UI**
- Clean Python code with `.ipynb` notebook for training
- Modular and easy to extend

---

## 🧠 Model Details

- **Model**: T5 (Text-To-Text Transfer Transformer)
- **Input**: Long-form text
- **Output**: Short-form summary
- **Training**: Using pretrained weights with option to train further

---

## 📂 File Structure

```

text-summarizer/
├── main.py               # Main backend logic
├── app.py                # Streamlit web app interface
├── training.ipynb        # Notebook for training the model
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

````

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Abdulraheem232/text-summarizer.git
cd text-summarizer
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the training notebook

> ⚠️ **Before running the app**, make sure to execute `training.ipynb` to initialize and (optionally) train the model.

You can open the notebook using Jupyter or VS Code.

### 4. Launch the Web App

```bash
streamlit run main.py
```

---

## 🧪 Custom Training

You can customize the training process (e.g., number of epochs, dataset, model size) in the `training.ipynb` file. The current setup uses a pretrained T5 model, but **you can train for more epochs** or with your own dataset to improve performance.

---

## 📫 Contact

**📧 Email**: [abdulraheemabdullah859@gmail.com](mailto:abdulraheemabdullah859@gmail.com)
**💬 GitHub**: [github.com/Abdulraheem232/text-summarizer](https://github.com/Abdulraheem232/text-summarizer)

---

### **❗️ Please contact me and feel free to ask a question — I will help you!**

---

## ✅ TODOs

* Add support for summarizing web pages or PDFs
* Improve model evaluation with ROUGE and BLEU metrics

---

## 🧾 License

This project is licensed under the MIT License.
```
