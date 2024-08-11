def is_spam(content):
    spam_keywords = ['prize', 'win', 'free', 'click', 'reward', 'lottery', 'tickets']
    return any(keyword in content.lower() for keyword in spam_keywords)