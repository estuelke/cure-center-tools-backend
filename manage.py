from backend import create_app
from flask_migrate import Manager, MigrateCommand
from backend import db
from backend.members.models import Member, ListMembership, List, MailchimpTag


manager = Manager(create_app())
manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    m = Member(first_name='Erin', last_name='Stuelke')
    db.session.add(m)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
