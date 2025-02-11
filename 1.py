import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return 'World'


schema = graphene.Schema(query=Query)

schema.execute('''
  query {
    hello
  }
''')

print(schema)
"""== Рез: ==
type Query {
  hello: String
}
"""
