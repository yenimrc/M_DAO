
from models.user import User
from dao.factory import get_dao_from_config


def main():
    
    dao = get_dao_from_config("config.json")

    # 2. Define a lista de nuevos usuarios
    new_users = [
        
        User(None, "Carlos Perez", "charlyy_p@prueba.com"),
        #User(None, "Carlos Gomez", "carlos.g@prueba.com"),
        #User(None, "Sofia Lopez", "sofia.l@prueba.com")
    ]
    
   
    print("➕ Agregando múltiples usuarios...")
    for user in new_users:
        dao.add_user(user)
        print(f"  - Usuario '{user.name}' agregado con éxito.")
    
    print("✅ Todos los usuarios han sido agregados.")
    print("\n---")

   
    print("📋 Usuarios almacenados (incluyendo los nuevos):")
    for u in dao.get_all_users():
        print(u)

if __name__ == "__main__":
    main()