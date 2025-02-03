from transformers import AutoFeatureExtractor, AutoModelForImageClassification, AutoImageProcessor
from PIL import Image
import torch


def main():


    processor = AutoImageProcessor.from_pretrained("chriamue/bird-species-classifier")
    model = AutoModelForImageClassification.from_pretrained("chriamue/bird-species-classifier")


    # Load an image
    image_path = "journals/testbird2.jpg"  # Replace with your image path
    image = Image.open(image_path).convert("RGB")  # Ensure it's in RGB mode

    # Preprocess the image
    inputs = processor(images=image, return_tensors="pt")  # Convert image into model-friendly format

    # Perform inference
    with torch.no_grad():  # No need to compute gradients
        outputs = model(**inputs)

    # Get the predicted class
    predicted_class_idx = outputs.logits.argmax(-1).item()
    print(f"Predicted class index: {predicted_class_idx}")

    # If the model has a label mapping, you might need to load them separately
    if model.config.id2label:
        print(f"Predicted bird species: {model.config.id2label[predicted_class_idx]}")










































if __name__ == "__main__":
    main()