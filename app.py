from fastai.vision.all import *
import gradio as gr

learn = load_learner("model.pkl")

def predict(img):
    pred_class, pred_idx, probs = learn.predict(img)
    return {learn.dls.vocab[i]: float(probs[i]) for i in range(len(probs))}

interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"), 
    outputs=gr.Label(num_top_classes=5),
    title="LEGO Brick Classifier",
    theme="default"
)

interface.launch()
