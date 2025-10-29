
from models.user import User
from dao.factory import get_dao_from_config


def main():
    # 1. Get the configured DAO (e.g., UserDAOExcel)
    dao = get_dao_from_config("config.json")

    # 2. Define a list of new users
    new_users = [
        # Pass arguments POSITIONALLY: (id, name, email)
        User(None, "Mike Williams", "mikyy_w@prueba.com"),
        #User(None, "Carlos Gomez", "carlos.g@prueba.com"),
        #User(None, "Sofia Lopez", "sofia.l@prueba.com")
    ]
    
    # 3. Insert each new user record by iterating through the list
    print("➕ Agregando múltiples usuarios...")
    for user in new_users:
        dao.add_user(user)
        print(f"  - Usuario '{user.name}' agregado con éxito.")
    
    print("✅ Todos los usuarios han sido agregados.")
    print("\n---")

    # 4. Display all stored users to confirm insertion
    print("📋 Usuarios almacenados (incluyendo los nuevos):")
    for u in dao.get_all_users():
        print(u)

if __name__ == "__main__":
    main()