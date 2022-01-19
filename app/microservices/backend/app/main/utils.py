from app import db
from app.models import SimpleTable
def entry_to_json(data):
    dt = []
    for i in data:
        dt.append({
            'username': i.username,
            'email': i.email_id,
            'year_of_birth': i.year_of_birth,
            'age_group': i.age_group
        })
    return dt

def get_age_group(year_of_birth):
    if year_of_birth <= 1995 and year_of_birth >= 1980:
        return 'Adult'
    elif year_of_birth < 1980:
        return 'Old'
    else:
        return 'Child'

def new_entry(username, email_id, year_of_birth):
    year_of_birth = int(year_of_birth)
    try:
        age_group = get_age_group(year_of_birth)
        dt = SimpleTable(username=username, email_id=email_id, year_of_birth=year_of_birth, age_group=age_group)
        db.session.add(dt)
        db.session.commit()
        return [200, 'Success']
    except Exception as e:
        return [500, e]

def delete_entry(email_id):
    try:
        entry = SimpleTable.query.filter_by(email_id=email_id).first()
        if entry:
            db.session.delete(entry)
            db.session.commit()
            return  [200, 'Success']
        else:
            return [404, 'Entry not found']
    except Exception as e:
        return [500, str(e)]

def update_entry(email_id, year_of_birth, username):
    try:
        entry = SimpleTable.query.filter_by(email_id=email_id).first()
        
        if entry:
            entry.year_of_birth = year_of_birth
            entry.username = username
            entry.age_group = get_age_group(year_of_birth)
            entry.email_id = email_id

            db.session.commit()
            return  [200, 'Success']
        else:
            return [404, 'Entry not found']
    except Exception as e:
        return [500, str(e)]