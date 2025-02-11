import graphene

# ДатаКласс = такой же как юзер в Схеме
class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()

class Query(graphene.ObjectType):
    get_user = graphene.Field(User)

    @staticmethod
    def resolve_get_user(root, info):
        new_user = User()
        new_user.id = 0
        new_user.username = 'Victor'
        return new_user

schema = graphene.Schema(query=Query)
results = schema.execute("""
    query{
        getUser{
            id
            username
            }
        }
""")

print(f'results.data = {results.data}')