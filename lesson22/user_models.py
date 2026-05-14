from pydantic import BaseModel, conint, constr

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

user =  User(id=1, name='Dion Konjuhi', age=18, email='dion.konjuhi@example.com')

class User(BaseModel):
    id: int
    name: str
    age: int=0
    email: str = "noemail@example.com"

user1 = User(id=2, name='Egzon Krasniqi',  email='@example.com')
print(user1)

user2 = User(id=3, name='Melina Salihu', age=17)
print(user2)

user3 = User(id=4, name='Festa Rexhepi')
print(user3)


class another_user(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2, max_length=50)


valid_user = another_user(id=1, name="Festa")
print(valid_user)

valid_user1 = another_user(id=0, name="Festa")
print(valid_user1)



































