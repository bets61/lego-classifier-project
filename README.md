# LEGO Brick Classifier 🧱

This project is a LEGO brick image classifier built using [Fastai](https://docs.fast.ai/) and [Gradio](https://gradio.app/), deployed on [Hugging Face Spaces](https://huggingface.co/spaces/Bets61/lego-classifier-project).

## 🔍 Demo
🧪 Try it here:  
👉 [LEGO Classifier on Hugging Face Spaces](https://huggingface.co/spaces/Bets61/lego-classifier-project)

## 📂 Project Structure

- `app.py` – Gradio interface to interact with the trained model
- `requirements.txt` – Dependencies required to run the app
- `model.pkl` – Trained Fastai model (stored on Hugging Face, not in repo due to size)

## 📸 Dataset

The dataset contains labeled images of various LEGO bricks such as:
- Brick 2x2  
- Plate 1x2  
- Technic Lever 3M  
- Cross Axle with Friction  
- etc.

## 🧠 Model

- Architecture: `resnet34`
- Library: `fastai`
- Trained for: 5 epochs
- Accuracy: ~98%

## 🚀 Deployment

- Uses Gradio for web interface
- Hosted on Hugging Face Spaces
- `model.pkl` is loaded locally within the Space

## 📦 Installation (if you want to run locally)

```bash
pip install -r requirements.txt
python app.py
