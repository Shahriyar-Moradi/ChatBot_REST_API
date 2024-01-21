
from .utils import load_local_gpt2_model
from .models import ChatMessage
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch
from rest_framework.views import APIView
from .models import ChatMessage
from .serializers import BotSerializer


# Get an instance of a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('chatbot-logs.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def generate_response(model, tokenizer, input_text, max_length=100):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Check if the input tensor is not empty
    if input_ids.size(1) > 0:
        # Generate a response
        with torch.no_grad():
            # output = model.generate()
            output = model.generate(
    input_ids,
    do_sample=False,  # You can omit this line as `False` is the default
    # max_length=max_length,
    max_length=100,
    
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    pad_token_id=tokenizer.eos_token_id,
    attention_mask=None
)

        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return response
    else:
        return "Input tensor is empty."






class ChatBotAPIView(APIView):
    serializer_class = BotSerializer
    def post(self, request, *args, **kwargs):
        serializer = BotSerializer(data=request.data)
        if serializer.is_valid():
            user_text = serializer.validated_data['user']
            conversation_id = serializer.validated_data['conversation_id']

            # Retrieve or create a conversation instance
            conversation, created = ChatMessage.objects.get_or_create(
                conversation_id=conversation_id
            )

    
            model, tokenizer = load_local_gpt2_model()

        # Generate response using the model
            bot_response = generate_response(model, tokenizer, user_text)
               # Log the request
            logger.info(f"Request from conversation {conversation_id}: {user_text} and bot response is {bot_response}.")
            
            chat_history = ChatMessage.objects.all()

            # Update conversation history
            conversation.history += f"User: {user_text}\nBot: {bot_response}\n"
            conversation.save()

            # Log the response
            logger.info(f"Response to conversation {conversation_id}: {bot_response}")

            return Response({
                "conversationID": conversation_id,
                "responseText": bot_response
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)