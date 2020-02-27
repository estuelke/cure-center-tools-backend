from backend import db


list_memberships = db.Table(
    'list_memberships',
    db.Column('list_id', db.Integer, db.ForeignKey('list.id'), nullable=False),
    db.Column(
        'member_id', db.Integer, db.ForeignKey('member.id'), nullable=False
    )
)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    institution = db.Column(db.String(120), nullable=False)
    is_executive_assistant = db.Column(db.Boolean)
    is_archived = db.Column(db.Boolean)
    executive_assistant_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    executive_assistant = db.relationship(
        'Member',
        backref='member_executive_assistant',
        uselist=False,
        remote_side=[id],
        lazy=True
    )
    emails = db.relationship('Email', backref='member', lazy=True)
    phone_numbers = db.relationship('PhoneNumber', backref='member', lazy=True)
    lists = db.relationship(
        'List',
        secondary=list_memberships,
        backref=db.backref('members', lazy=True),
        lazy=True
    )
    cure_center_profile = db.relationship(
        'CureCenterProfile',
        backref='member',
        uselist=False
    )

    def __repr__(self):
        return f"<Member(first='{self.first_name}', last='{self.last_name}')>"


class CureCenterProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(
        db.Integer, db.ForeignKey('member.id'), nullable=False
    )
    member_name = db.relationship('Member', uselist=False, lazy=True)
    nick_name = db.Column(db.String(30))
    suffix = db.Column(db.String(30))
    birthday = db.Column(db.Date())
    group_id = db.Column(
        db.Integer, db.ForeignKey('group.id'), nullable=False
    )
    group = db.relationship(
        'Group',
        backref='member_group',
        uselist=False,
        lazy=True
    )
    is_internal = db.Column(db.Boolean)
    is_qura_funded = db.Column(db.Boolean)
    image_url = db.Column(db.String(120))
    onyen = db.Column(db.String(30))
    staff_designation = db.Column(db.String(30))
    positions = db.relationship('Position', backref='member', lazy=True)

    def __repr__(self):
        return f"<CureCenterProfile(member='{self.member_name}')>"


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(
        db.Integer, db.ForeignKey('member.id'), nullable=False
    )
    email_address = db.Column(db.String(50), nullable=False)
    label = db.Column(db.String(30))

    def __repr__(self):
        return f"<Email(email_address='{self.email_address}')>"


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(
        db.Integer, db.ForeignKey('member.id'), nullable=False
    )
    contact = db.relationship(
        'Member',
        backref='group_contact',
        uselist=False,
        lazy=True
    )
    name = db.Column(db.String(30), nullable=False)
    members = db.relationship('Member', backref='group', lazy=True)

    def __repr__(self):
        return f"<Group(name='{self.name}')>"


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    list_type = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<List(name='{self.name}')>"


class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(
        db.Integer, db.ForeignKey('member.id'), nullable=False
    )
    phone_number = db.Column(db.String(15), nullable=False)
    label = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"<PhoneNumber(phone_number='{self.phone_number}')>"


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cure_center_profile_id = db.Column(
        db.Integer, db.ForeignKey('cure_center_profile.id'), nullable=False
    )
    title = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50))

    def __repr__(self):
        return f"<Position(title='{self.title}', department='{self.department}')>"
