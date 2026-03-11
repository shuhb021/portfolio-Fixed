from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# ─── Project ───────────────────────────────────────────────────────────────────
class Project(db.Model):
    __tablename__ = 'project'
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    tech_stack  = db.Column(db.String(500))   # comma-separated
    github_url  = db.Column(db.String(500))
    live_url    = db.Column(db.String(500))
    image_url   = db.Column(db.String(500))
    category    = db.Column(db.String(100), index=True)
    featured    = db.Column(db.Boolean, default=False, index=True)
    order       = db.Column(db.Integer, default=0)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')] if self.tech_stack else []

    def to_dict(self):
        return {
            'id':          self.id,
            'title':       self.title,
            'description': self.description,
            'tech_stack':  self.tech_list(),
            'github_url':  self.github_url,
            'live_url':    self.live_url,
            'image_url':   self.image_url,
            'category':    self.category,
            'featured':    self.featured,
        }

    def __repr__(self):
        return f'<Project {self.id}: {self.title}>'


# ─── Skill ─────────────────────────────────────────────────────────────────────
class Skill(db.Model):
    __tablename__ = 'skill'
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100), nullable=False)
    category    = db.Column(db.String(100), index=True)
    proficiency = db.Column(db.Integer, default=80)   # 0-100
    order       = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Skill {self.name} ({self.category})>'


# ─── Experience ────────────────────────────────────────────────────────────────
class Experience(db.Model):
    __tablename__ = 'experience'
    id          = db.Column(db.Integer, primary_key=True)
    company     = db.Column(db.String(200), nullable=False)
    role        = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    start_date  = db.Column(db.String(50))
    end_date    = db.Column(db.String(50))   # "Present" if current
    location    = db.Column(db.String(200))
    order       = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Experience {self.role} @ {self.company}>'


# ─── Education ─────────────────────────────────────────────────────────────────
class Education(db.Model):
    """
    Stores educational qualifications — degrees, diplomas, courses.
    Shown in the portfolio's About/Education section.
    """
    __tablename__ = 'education'
    id          = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(300), nullable=False)
    degree      = db.Column(db.String(300), nullable=False)  # e.g. B.Tech Computer Science
    field       = db.Column(db.String(200))                   # e.g. Computer Science & Engineering
    grade       = db.Column(db.String(50))                    # e.g. 8.5 CGPA / 85%
    start_year  = db.Column(db.String(20))
    end_year    = db.Column(db.String(20))                    # "Present" if ongoing
    location    = db.Column(db.String(200))
    description = db.Column(db.Text)                          # Coursework, clubs, honours, etc.
    order       = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Education {self.degree} @ {self.institution}>'


# ─── Message ───────────────────────────────────────────────────────────────────
class Message(db.Model):
    __tablename__ = 'message'
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(200), nullable=False)
    email      = db.Column(db.String(200), nullable=False)
    subject    = db.Column(db.String(300))
    message    = db.Column(db.Text, nullable=False)
    is_read    = db.Column(db.Boolean, default=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    def __repr__(self):
        return f'<Message from {self.name} ({self.email})>'


# ─── BlogPost ──────────────────────────────────────────────────────────────────
class BlogPost(db.Model):
    __tablename__ = 'blog_post'
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(300), nullable=False)
    slug        = db.Column(db.String(300), unique=True, nullable=False, index=True)
    summary     = db.Column(db.Text)
    content     = db.Column(db.Text)
    cover_image = db.Column(db.String(500))
    tags        = db.Column(db.String(500))   # comma-separated
    published   = db.Column(db.Boolean, default=False, index=True)
    featured    = db.Column(db.Boolean, default=False)
    read_time   = db.Column(db.Integer, default=5)   # minutes
    views       = db.Column(db.Integer, default=0)   # page view counter
    created_at  = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at  = db.Column(db.DateTime, default=datetime.utcnow)

    def tag_list(self):
        return [t.strip() for t in self.tags.split(',')] if self.tags else []

    def to_dict(self):
        return {
            'id':         self.id,
            'title':      self.title,
            'slug':       self.slug,
            'summary':    self.summary,
            'tags':       self.tag_list(),
            'published':  self.published,
            'featured':   self.featured,
            'read_time':  self.read_time,
            'views':      self.views,
            'created_at': self.created_at.strftime('%d %b %Y'),
        }

    def __repr__(self):
        return f'<BlogPost {self.slug}>'


# ─── Achievement ───────────────────────────────────────────────────────────────
class Achievement(db.Model):
    __tablename__ = 'achievement'
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text)
    issuer      = db.Column(db.String(200))
    date        = db.Column(db.String(50))
    category    = db.Column(db.String(100), index=True)
    icon        = db.Column(db.String(10), default='🏆')
    link        = db.Column(db.String(500))
    order       = db.Column(db.Integer, default=0)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Achievement {self.title}>'


# ─── SiteSettings ──────────────────────────────────────────────────────────────
class SiteSettings(db.Model):
    __tablename__ = 'site_settings'
    id    = db.Column(db.Integer, primary_key=True)
    key   = db.Column(db.String(100), unique=True, nullable=False, index=True)
    value = db.Column(db.Text)

    @staticmethod
    def get(key, default=''):
        s = SiteSettings.query.filter_by(key=key).first()
        return s.value if s else default

    @staticmethod
    def set(key, value):
        """
        Upsert a setting value.
        NOTE: Does NOT call db.session.commit() — the caller must commit
        after all settings are updated, keeping the entire save atomic.
        """
        s = SiteSettings.query.filter_by(key=key).first()
        if s:
            s.value = value
        else:
            s = SiteSettings(key=key, value=value)
            db.session.add(s)

    def __repr__(self):
        return f'<SiteSettings {self.key}={self.value!r}>'
