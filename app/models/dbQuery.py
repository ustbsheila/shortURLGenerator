from app import db
from app.models.urlmapping import URLMapping
from app.models.accesslog import AccessLog

def check_original_url_exist(original_url):
    return URLMapping.query.filter_by(original_url=original_url).first()

def retrieve_original_url(short_url):
    return URLMapping.query.filter_by(short_url=short_url).first()

def add_url_mapping(original_url, short_url):
    """
    Create a new ShortURL entry and add to DB
    """
    new_url = URLMapping(original_url=original_url, short_url=short_url)
    db.session.add(new_url)
    db.session.commit()

def add_access_log(url_mapping_entry):
    """
    Given the short URL information, add the access log to the DB
    """
    access_log = AccessLog(short_url_id=url_mapping_entry.id)
    db.session.add(access_log)
    db.session.commit()