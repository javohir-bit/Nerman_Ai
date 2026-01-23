from .models import FAQ
from difflib import SequenceMatcher


def search_faq(query):
    query = query.lower().strip()
    
    # First: exact keyword match
    faqs = FAQ.objects.filter(is_active=True)
    matches = []
    
    for faq in faqs:
        keywords = faq.get_keywords_list()
        
        # Check for exact keyword match
        for keyword in keywords:
            if keyword in query or query in keyword:
                matches.append({
                    'faq': faq,
                    'score': 100,
                    'type': 'exact'
                })
                break
    
    # If no exact match, try fuzzy matching
    if not matches:
        for faq in faqs:
            # Check similarity with question
            similarity = SequenceMatcher(None, query, faq.question.lower()).ratio()
            if similarity > 0.5:
                matches.append({
                    'faq': faq,
                    'score': similarity * 100,
                    'type': 'fuzzy'
                })
    
    # Sort by score
    matches.sort(key=lambda x: x['score'], reverse=True)
    
    # Return top 3 matches
    return [match['faq'] for match in matches[:3]]


def format_faq_response(faq):
    return f"{faq.icon} {faq.question}\n\n{faq.answer}"


def get_faqs_by_category(category):
    return FAQ.objects.filter(category=category, is_active=True).order_by('-created_at')


def format_category_faqs(category):
    faqs = get_faqs_by_category(category)
    
    if not faqs:
        return "Bu kategoriyada hozircha savol-javoblar yo'q."
    
    response = ""
    for faq in faqs:
        response += f"{faq.icon} {faq.question}\n{faq.answer}\n\n"
        response += "—" * 20 + "\n\n"
    
    return response.strip()
