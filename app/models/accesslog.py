from app import db
from datetime import datetime
class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_url_id = db.Column(db.Integer, db.ForeignKey('url_mapping.id'), nullable=False)
    accessed_at = db.Column(db.DateTime, default=datetime.utcnow)
    short_url = db.relationship('URLMapping', backref='access_logs', primaryjoin='AccessLog.short_url_id == URLMapping.id')
