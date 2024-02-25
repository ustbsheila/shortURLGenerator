from app import db
from app.models.urlmapping import URLMapping
from app.models.accesslog import AccessLog
from datetime import timedelta

def check_original_url_exist(original_url):
    return URLMapping.query.filter_by(original_url=original_url).first()

def get_url_mapping_by_short_url(short_url):
    return URLMapping.query.filter_by(short_url=short_url).first()

def add_url_mapping(original_url, short_url):
    """
    Create a new ShortURL entry and add to DB
    """
    new_url = URLMapping(original_url=original_url, short_url=short_url)
    db.session.add(new_url)
    db.session.commit()

def delete_url_mapping(url_mapping_entry):
    db.session.delete(url_mapping_entry)
    db.session.commit()

def add_access_log(url_mapping_entry):
    """
    Given the short URL information, add the access log to the DB
    """
    access_log = AccessLog(short_url_id=url_mapping_entry.id)
    db.session.add(access_log)
    db.session.commit()

def get_last_24_hour_access_stats(url_mapping_entry, now_ts):
    """
    Given the short URL, return access times for the last 24 hours
    """
    return AccessLog.query.filter_by(short_url_id=url_mapping_entry.id).filter(
        AccessLog.accessed_at >= now_ts - timedelta(hours=24)).count()

def get_past_week_access_stats(url_mapping_entry, now_ts):
    """
    Given the short URL, return access times for the past week
    """
    return AccessLog.query.filter_by(short_url_id=url_mapping_entry.id).filter(
        AccessLog.accessed_at >= now_ts - timedelta(weeks=1)).count()

def get_all_time_access_stats(url_mapping_entry):
    """
    Given the short URL, return all recorded access times
    """
    return AccessLog.query.filter_by(short_url_id=url_mapping_entry.id).count()

