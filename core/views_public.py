from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import SupportTicket, SupportMessage


# Публичные страницы
def home(request):
    """Главная страница"""
    return render(request, 'public/home.html')


def product(request):
    """Страница о продукте"""
    return render(request, 'public/product.html')


def pricing(request):
    """Страница тарифов"""
    plans = [
        {
            'name': 'Free',
            'price': '0',
            'tokens': '1,000',
            'features': ['Basic AI Tasks', '1000 tokens/month', 'Email support']
        },
        {
            'name': 'Pro',
            'price': '$29',
            'tokens': '50,000',
            'features': ['All AI features', '50,000 tokens/month', 'Priority support', 'API access'],
            'highlighted': True
        },
        {
            'name': 'Enterprise',
            'price': 'Custom',
            'tokens': 'Unlimited',
            'features': ['All Pro features', 'Unlimited tokens', 'Dedicated support', 'Custom integrations']
        }
    ]
    return render(request, 'public/pricing.html', {'plans': plans})


def about(request):
    """Страница О нас"""
    return render(request, 'public/about.html')


def faq(request):
    """Страница FAQ"""
    faqs = [
        {
            'question': 'Что такое Nerman-Ai и как он работает?',
            'answer': 'Nerman-Ai — это передовая платформа на базе искусственного интеллекта, которая автоматизирует процесс создания и редактирования видео. Вы загружаете исходные материалы, а наши алгоритмы анализируют контент, нарезают лучшие моменты, добавляют субтитры и эффекты, создавая готовый к публикации ролик за считанные минуты.'
        },
        {
            'question': 'Нужно ли мне уметь монтировать чтобы пользоваться Nerman-Ai?',
            'answer': 'Абсолютно нет! Nerman-Ai создан специально для того, чтобы заменить сложные профессиональные программы. Вам не нужно знать, как работать с таймлайном или цветокоррекцией — просто выберите стиль, и ИИ сделает всю работу за вас.'
        },
        {
            'question': 'Какие форматы видео поддерживает Nerman-Ai?',
            'answer': 'Мы поддерживаем загрузку всех популярных видеоформатов (MP4, MOV, AVI, и др.). Экспорт оптимизирован под современные социальные сети: вертикальные (9:16) для Reels/TikTok/Shorts, и горизонтальные (16:9) для YouTube.'
        },
        {
            'question': 'Сколько времени занимает монтаж?',
            'answer': 'Скорость — наше главное преимущество. Обработка стандартного ролика занимает от 1 до 3 минут. Это в десятки раз быстрее, чем ручной монтаж, который может длиться часами.'
        },
        {
            'question': 'Могу ли я добавлять свои субтитры, музыку, или правки?',
            'answer': 'Да, конечно. После автоматической обработки вы попадаете в редактор, где можете изменить текст субтитров, выбрать другую фоновую музыку из нашей библиотеки или загрузить свою, а также скорректировать длительность сцен.'
        },
        {
            'question': 'Автоматически добавляются субтитры?',
            'answer': 'Да, Nerman-Ai имеет встроенную мощную систему распознавания речи (Whisper), которая автоматически генерирует точные субтитры. Вы можете выбрать стиль анимации субтитров, шрифт и цвет.'
        },
        {
            'question': 'Будет ли водяной знак?',
            'answer': 'На тарифе Free видео могут содержать небольшой водяной знак. На всех платных тарифах (Pro и выше) водяной знак полностью отсутствует, и вы получаете видео в максимальном качестве.'
        },
        {
            'question': 'Есть ли бесплатный период?',
            'answer': 'Да! При регистрации вы получаете 1000 бесплатных токенов. Этого достаточно, чтобы создать несколько пробных видео и полностью оценить возможности платформы без каких-либо обязательств.'
        },
        {
            'question': 'Можно ли использовать без привязки карты в Демо-версии?',
            'answer': 'Да, для регистрации и использования бесплатных стартовых токенов привязка банковской карты не требуется. Мы не списываем деньги скрыто.'
        },
        {
            'question': 'Какие возможности будут добавлены в будущем?',
            'answer': 'Мы постоянно развиваемся. В ближайших обновлениях: клонирование вашего голоса, генерация видео-аватаров, автоматический перевод видео на другие языки (дубляж) и прямая интеграция с YouTube и Instagram для автопостинга.'
        }
    ]
    return render(request, 'public/faq.html', {'faqs': faqs})


def blog(request):
    """Страница блога"""
    posts = [
        {
            'title': 'Как AI меняет бизнес-процессы в 2026',
            'excerpt': 'Искусственный интеллект революционизирует способы работы компаний по всему миру...',
            'author': 'Команда NERMAN.AI',
            'date': '2026-01-10'
        },
        {
            'title': 'Топ-5 способов автоматизации с помощью AI',
            'excerpt': 'Узнайте, какие процессы можно автоматизировать прямо сейчас...',
            'author': 'Команда NERMAN.AI',
            'date': '2026-01-05'
        }
    ]
    return render(request, 'public/blog.html', {'posts': posts})


@login_required
def contact(request):
    """Страница службы поддержки (Чат)"""
    ticket, created = SupportTicket.objects.get_or_create(
        user=request.user,
        status__in=[SupportTicket.Status.OPEN, SupportTicket.Status.IN_PROGRESS],
        defaults={'subject': 'Chat Support'}
    )
    
    if created:
        # Авто-ответ при создании тикета
        SupportMessage.objects.create(
            ticket=ticket,
            sender=SupportMessage.Sender.SUPPORT,
            content="Здравствуйте! Чем я могу помочь вам сегодня?"
        )
    
    messages = ticket.messages.all()
    return render(request, 'public/contact.html', {
        'ticket': ticket,
        'chat_messages': messages
    })


@login_required
def send_support_message(request):
    """AJAX endpoint для отправки сообщения"""
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        content = data.get('content')
        ticket_id = data.get('ticket_id')
        
        ticket = get_object_with_404(SupportTicket, id=ticket_id, user=request.user)
        
        # Сохраняем сообщение пользователя
        message = SupportMessage.objects.create(
            ticket=ticket,
            sender=SupportMessage.Sender.USER,
            content=content
        )
        
        # Имитация авто-ответа (Auto-reply)
        auto_reply_content = ""
        if "привет" in content.lower() or "hello" in content.lower():
            auto_reply_content = "Привет! Я бот поддержки NERMAN.AI. Могу подсказать по тарифам или функциям редактора."
        elif "цена" in content.lower() or "price" in content.lower():
            auto_reply_content = "Наши тарифы начинаются от $0. Вы можете посмотреть подробности на странице 'Подписка'."
        else:
            auto_reply_content = "Ваше сообщение получено. Наши специалисты ответят вам в ближайшее время."
            
        if auto_reply_content:
            SupportMessage.objects.create(
                ticket=ticket,
                sender=SupportMessage.Sender.SUPPORT,
                content=auto_reply_content
            )

        return JsonResponse({
            'status': 'success',
            'message': {
                'content': message.content,
                'timestamp': message.timestamp.strftime('%H:%M'),
                'sender': message.sender
            },
            'auto_reply': {
                'content': auto_reply_content,
                'sender': 'support'
            } if auto_reply_content else None
        })
    return JsonResponse({'status': 'error'}, status=400)


@login_required
def get_support_messages(request, ticket_id):
    """AJAX endpoint для получения новых сообщений (polling)"""
    ticket = get_object_with_404(SupportTicket, id=ticket_id, user=request.user)
    last_id = request.GET.get('last_id', 0)
    
    messages = ticket.messages.filter(id__gt=last_id)
    
    return JsonResponse({
        'messages': [{
            'id': m.id,
            'content': m.content,
            'sender': m.sender,
            'timestamp': m.timestamp.strftime('%H:%M'),
        } for m in messages]
    })


def ai_video_editor(request):
    """Страница ИИ-Видеоредактора (теперь встроена в Product)"""
    return render(request, 'public/product.html')
