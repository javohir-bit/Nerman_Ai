from django.core.management.base import BaseCommand
from support_bot.models import FAQ


class Command(BaseCommand):
    help = 'Load initial FAQ data'

    def handle(self, *args, **options):
        faqs = [
            # Platform
            {
                'category': 'platform',
                'icon': '❌',
                'question': 'Funksiya ishlamayapti',
                'answer': 'Iltimos, sahifani yangilang (Ctrl + F5) va qayta urinib ko\'ring. Agar muammo saqlanib qolsa, brauzer va qurilma nomini yozib qoldiring.',
                'keywords': 'ishlamayapti, ishlayapti, ishlamadi, xatolik, nima qilish'
            },
            {
                'category': 'platform',
                'icon': '⚠️',
                'question': 'Funksiya noto\'g\'ri ishlayapti',
                'answer': 'Bu vaqtinchalik xatolik bo\'lishi mumkin. Hisobingizdan chiqib, qayta kiring va yana urinib ko\'ring.',
                'keywords': 'noto\'g\'ri, xato, ishlayapti, muammo, chiqish, kirish'
            },
            {
                'category': 'platform',
                'icon': '🔄',
                'question': 'O\'zgarishlar saqlanmayapti',
                'answer': 'Internet aloqangizni tekshiring. O\'zgarishdan keyin "Saqlash" tugmasi bosilganiga ishonch hosil qiling.',
                'keywords': 'saqlanmayapti, saqlash, o\'zgarish, internet, aloqa'
            },
            {
                'category': 'platform',
                'icon': '🐞',
                'question': 'Bug topildi',
                'answer': 'Rahmat! Iltimos, muammo qachon va qanday paydo bo\'lganini qisqacha yozib qoldiring — biz tezda tekshiramiz.',
                'keywords': 'bug, xatolik, muammo, topildi, xato'
            },
            {
                'category': 'platform',
                'icon': '⏳',
                'question': 'Platforma sekin ishlayapti',
                'answer': 'Hozir tizimda yuklama bo\'lishi mumkin. Bir necha daqiqadan so\'ng qayta urinib ko\'ring.',
                'keywords': 'sekin, asta, sekinlashdi, tormoz, yuklama'
            },
            {
                'category': 'platform',
                'icon': '💥',
                'question': 'Oq ekran / xato chiqyapti',
                'answer': 'Brauzer keshini tozalang yoki boshqa brauzerda ochib ko\'ring.',
                'keywords': 'oq ekran, xato, error, kesh, brauzer, ochilmayapti'
            },
            
            # Video
            {
                'category': 'video',
                'icon': '📹',
                'question': 'Video yuklanmayapti',
                'answer': 'Video hajmi va formatini tekshiring (MP4 tavsiya qilinadi).',
                'keywords': 'video, yuklanmayapti, upload, hajm, format, mp4'
            },
            {
                'category': 'video',
                'icon': '📤',
                'question': 'Video yuklanadi, lekin qayta ishlanmaydi',
                'answer': 'Iltimos, bir oz kuting. Agar 10 daqiqadan oshsa, bizga xabar bering.',
                'keywords': 'qayta ishlanmayapti, processing, yuklanadi, kutish, vaqt'
            },
            {
                'category': 'video',
                'icon': '🎵',
                'question': 'Musiqa qo\'shilmayapti',
                'answer': 'Musiqa uzunligi video davomiyligidan oshmaganiga ishonch hosil qiling.',
                'keywords': 'musiqa, qo\'shilmayapti, audio, uzunligi, davomiyligi'
            },
            {
                'category': 'video',
                'icon': '✂️',
                'question': 'Montaj noto\'g\'ri ishlayapti',
                'answer': 'Sahifani yangilab, montajni boshidan qayta sinab ko\'ring.',
                'keywords': 'montaj, noto\'g\'ri, edit, yangilash, qayta'
            },
            {
                'category': 'video',
                'icon': '🎞',
                'question': 'Natija previewdan farq qiladi',
                'answer': 'Bu eksport sifati bilan bog\'liq bo\'lishi mumkin. Yakuniy render — to\'g\'ri natija hisoblanadi.',
                'keywords': 'preview, farq, natija, render, eksport, sifat'
            },
            {
                'category': 'video',
                'icon': '🗑',
                'question': 'Loyiha yo\'qolgan',
                'answer': 'Iltimos, akkauntingizga to\'g\'ri kirganingizni tekshiring.',
                'keywords': 'loyiha, yo\'qolgan, topilmadi, akkaunt, kirish'
            },
            
            # AI
            {
                'category': 'ai',
                'icon': '🧠',
                'question': 'Natija noto\'g\'ri chiqdi',
                'answer': 'So\'rovingizni aniqroq va batafsil yozib ko\'ring.',
                'keywords': 'natija, noto\'g\'ri, ai, so\'rov, aniq, batafsil'
            },
            {
                'category': 'ai',
                'icon': '🔁',
                'question': 'AI javob bermayapti',
                'answer': 'Hozir xizmat vaqtincha band bo\'lishi mumkin. Birozdan keyin urinib ko\'ring.',
                'keywords': 'ai, javob bermayapti, ishlamayapti, band, kutish'
            },
            {
                'category': 'ai',
                'icon': '📉',
                'question': 'Sifat pasaydi',
                'answer': 'Model yangilanmoqda. Tez orada yaxshilanadi.',
                'keywords': 'sifat, pasaydi, past, yomon, model, yangilanish'
            },
            {
                'category': 'ai',
                'icon': '❓',
                'question': 'AI so\'rovni tushunmadi',
                'answer': 'Murakkab gaplarni qisqa va oddiy qilib yozing.',
                'keywords': 'tushunmadi, so\'rov, murakkab, oddiy, qisqa'
            },
            {
                'category': 'ai',
                'icon': '⛔️',
                'question': 'AI ishlamayapti',
                'answer': 'Funksiya vaqtinchalik o\'chirilgan bo\'lishi mumkin.',
                'keywords': 'ishlamayapti, o\'chirilgan, faol emas, vaqtinchalik'
            },
            
            # Account
            {
                'category': 'account',
                'icon': '🚪',
                'question': 'Akkauntga kira olmayapman',
                'answer': 'Login va parolni tekshiring yoki "Parolni unutdingizmi?" ni bosing.',
                'keywords': 'kira olmayapman, login, parol, akkaunt, kirish'
            },
            {
                'category': 'account',
                'icon': '🔑',
                'question': 'Kod / xat kelmadi',
                'answer': 'Spam papkani tekshiring.',
                'keywords': 'kod, xat, kelmadi, email, spam'
            },
            {
                'category': 'account',
                'icon': '⚠️',
                'question': 'Akkaunt bloklangan',
                'answer': 'Qoidalar buzilgan bo\'lishi mumkin. Support tekshiradi.',
                'keywords': 'bloklangan, block, qoidalar, support'
            },
            {
                'category': 'account',
                'icon': '👤',
                'question': 'Profil muammosi',
                'answer': 'Profilni tahrirlab, saqlab ko\'ring.',
                'keywords': 'profil, muammo, tahrirlash, saqlash'
            },
            {
                'category': 'account',
                'icon': '🔄',
                'question': 'Sozlamalar saqlanmayapti',
                'answer': 'Brauzer ruxsatlarini tekshiring.',
                'keywords': 'sozlamalar, saqlanmayapti, brauzer, ruxsat'
            },
            
            # Payment
            {
                'category': 'payment',
                'icon': '💸',
                'question': 'To\'lov o\'tmadi',
                'answer': 'Karta ma\'lumotlarini tekshiring yoki boshqa usulni sinab ko\'ring.',
                'keywords': 'to\'lov, o\'tmadi, karta, payment, usul'
            },
            {
                'category': 'payment',
                'icon': '💳',
                'question': 'Pul yechildi, lekin xizmat yo\'q',
                'answer': '5–10 daqiqa kuting. Agar ochilmasa, bizga yozing.',
                'keywords': 'pul, yechildi, xizmat, yo\'q, ochilmadi, kutish'
            },
            {
                'category': 'payment',
                'icon': '📊',
                'question': 'Limitlar noto\'g\'ri',
                'answer': 'Sahifani yangilang yoki qayta kiring.',
                'keywords': 'limit, noto\'g\'ri, yangilash, kirish'
            },
            {
                'category': 'payment',
                'icon': '❌',
                'question': 'Obunani bekor qilmoqchiman',
                'answer': '"Akkaunt → Obuna" bo\'limidan bekor qilishingiz mumkin.',
                'keywords': 'obuna, bekor qilish, to\'xtatish, akkaunt'
            },
            
            # Other
            {
                'category': 'other',
                'icon': '🧩',
                'question': 'Funksiya kutilgandek emas',
                'answer': 'Fikr bildirganingiz uchun rahmat! Taklifingizni yozib qoldiring.',
                'keywords': 'funksiya, kutilgan, fikr, taklif'
            },
            {
                'category': 'other',
                'icon': '🚨',
                'question': 'Shoshilinch muammo',
                'answer': 'Iltimos, muammoni batafsil yozing — tezda javob beramiz.',
                'keywords': 'shoshilinch, muammo, tezkor, batafsil'
            },
        ]
        
        created_count = 0
        for faq_data in faqs:
            faq, created = FAQ.objects.get_or_create(
                question=faq_data['question'],
                defaults=faq_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created: {faq.question}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\n✓ Successfully loaded {created_count} FAQs')
        )
