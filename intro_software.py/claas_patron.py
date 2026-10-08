class patron:
    def __init__(self, name, email):
        self.name = name
        self.email = email


patron1 = patron ("Ana", "ana@example.com")
patron2 = patron ("Luis", "luis@example.com")

print("nObjeto patron 1")
print("nombre:" + patron1.name)
print("email:" + patron1.email)

print("nObjeto patron 2")
print("name:" + patron2.name)
print("email:" + patron2.email)

if patron1 == patron1.email:
    print("El correo electrónico pertenece a patron1")
