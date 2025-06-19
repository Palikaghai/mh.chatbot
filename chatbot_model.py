from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Load DialoGPT for conversational responses
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Load emotion detection model
emotion_classifier = pipeline("text-classification", model="finiteautomata/bertweet-base-emotion-analysis")

def get_chatbot_response(user_input):
    # Detect emotion
    emotion = emotion_classifier(user_input)[0]['label']
    
    # Generate chatbot response
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    chatbot_response_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    chatbot_response = tokenizer.decode(chatbot_response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    # Suggest coping mechanisms
    coping_tips = {
        "sadness": "💡 Try journaling or talking to a friend.",
        "anger": "💡 Take deep breaths or go for a walk.",
        "fear": "💡 Focus on breathing slowly. You're safe.",
        "joy": "💡 Great! Keep doing what makes you happy.",
        "surprise": "💡 Take a moment to process this.",
        "stress": "💡 Try the 4-7-8 breathing technique."
    }
    coping_tip = coping_tips.get(emotion, "💡 You're doing great! Keep going.")
    
    return {
        "response": chatbot_response,
        "emotion": emotion,
        "tip": coping_tip
    }