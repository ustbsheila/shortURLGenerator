from app import db
from app.models.urlmapping import URLMapping

def get_original_url(original_url):
    return URLMapping.query.filter_by(original_url=original_url).first()

def add_url_mapping(original_url, short_url):
    """
    Create a new ShortURL entry and add to DB
    """
    new_url = URLMapping(original_url=original_url, short_url=short_url)
    db.session.add(new_url)
    db.session.commit()