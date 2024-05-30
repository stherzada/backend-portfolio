from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='sther',
        password='eitalasqueira',
        email='sther@fast_zero.com',
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'sther'))

    assert user.username == 'sther'
