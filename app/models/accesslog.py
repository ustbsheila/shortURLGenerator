from app import db
from datetime import datetime
class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_url_id = db.Column(db.Integer, db.ForeignKey('url_mapping.id', ondelete='CASCADE'), nullable=False)
    accessed_at = db.Column(db.DateTime, default=datetime.utcnow)
