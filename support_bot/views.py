import json
import logging
import asyncio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .bot import send_message, get_bot
from .utils import search_faq, format_faq_response, format_category_faqs
from .keyboards import get_category_keyboard, get_support_keyboard
from telegram import Update

logger = logging.getLogger(__name__)


@csrf_exempt
@require_http_methods(["POST"])
def webhook(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        logger.info(f"Received webhook data: {data}")
        
        # Handle callback queries (button clicks)
        if 'callback_query' in data:
            callback_query = data['callback_query']
            chat_id = callback_query['message']['chat']['id']
            callback_data = callback_query['data']
            
            if callback_data.startswith('cat_'):
                category = callback_data.replace('cat_', '')
                response_text = format_category_faqs(category)
                asyncio.run(send_message_with_keyboard(chat_id, response_text, get_support_keyboard()))
            
            elif callback_data == 'back_to_menu':
                response_text = (
                    "Assalomu alaykum! 👋\n\n"
                    "Men NERMAN.AI support boti.\n"
                    "Quyidagi kategoriyalardan birini tanlang:"
                )
                asyncio.run(send_message_with_keyboard(chat_id, response_text, get_category_keyboard()))
            
            return JsonResponse({'status': 'ok'})
        
        # Handle regular messages
        if 'message' not in data:
            logger.warning("No message in webhook data")
            return JsonResponse({'status': 'ok'})
        
        message = data['message']
        chat_id = message['chat']['id']
        
        if 'text' in message:
            text = message['text']
            
            # /start command
            if text == '/start':
                response_text = (
                    "Assalomu alaykum! 👋\n\n"
                    "Men NERMAN.AI support boti.\n\n"
                    "Savolingizni yozing yoki quyidagi kategoriyalardan birini tanlang:"
                )
                asyncio.run(send_message_with_keyboard(chat_id, response_text, get_category_keyboard()))
            
            else:
                # Search FAQ
                faqs = search_faq(text)
                
                if faqs:
                    # Send top match
                    response_text = f"Sizning savolingizga javob:\n\n{format_faq_response(faqs[0])}\n\n"
                    
                    # If multiple matches, mention them
                    if len(faqs) > 1:
                        response_text += "\n\nQo'shimcha ma'lumotlar:\n"
                        for faq in faqs[1:]:
                            response_text += f"• {faq.icon} {faq.question}\n"
                    
                    asyncio.run(send_message_with_keyboard(chat_id, response_text, get_support_keyboard()))
                else:
                    # No match found
                    response_text = (
                        f"Sizning savolingiz: \"{text}\"\n\n"
                        "Kechirasiz, bu savolga javobni topa olmadim. 😔\n\n"
                        "Iltimos, quyidagi kategoriyalardan birini tanlang yoki to'g'ridan-to'g'ri support jamoamizga yozing."
                    )
                    asyncio.run(send_message_with_keyboard(chat_id, response_text, get_category_keyboard()))
        
        return JsonResponse({'status': 'ok'})
    
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {str(e)}")
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    
    except Exception as e:
        logger.error(f"Webhook error: {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


async def send_message_with_keyboard(chat_id, text, keyboard):
    try:
        bot = get_bot()
        await bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=keyboard
        )
        logger.info(f"Message with keyboard sent to chat_id: {chat_id}")
        return True
    except Exception as e:
        logger.error(f"Failed to send message with keyboard: {str(e)}")
        return False

