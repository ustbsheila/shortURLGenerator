from app import db
from datetime import datetime, timedelta


class URLMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Cascade deletion when URLMapping is deleted
    access_logs = db.relationship('AccessLog', backref='url_mapping', cascade='all, delete-orphan',
                                  passive_deletes=True)

    def __repr__(self):
        return f'<URLMapping {self.id}>'

    def row2dict(row):
        d = {}
        for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))

        return d