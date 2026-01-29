# from ldap3 import Server, Connection, ALL, SUBTREE
# from app.config import (
#     LDAP_URI,
#     LDAP_BIND_DN,
#     LDAP_PASSWORD,
#     LDAP_BASE_DN
# )

# ATTRIBUTES = ["cn", "mail", "departmentNumber", "ou"]


# def get_people():
#     # 1️⃣ Créer le serveur LDAP
#     server = Server(LDAP_URI, get_info=ALL)

#     # 2️⃣ Connexion + bind
#     conn = Connection(
#         server,
#         user=LDAP_BIND_DN,
#         password=LDAP_PASSWORD,
#         auto_bind=True
#     )

#     # 3️⃣ Recherche LDAP
#     conn.search(
#         search_base=LDAP_BASE_DN,
#         search_filter="(objectClass=person)",
#         search_scope=SUBTREE,
#         attributes=ATTRIBUTES
#     )

#     people = []

#     # 4️⃣ Traitement des résultats
#     for entry in conn.entries:
#         people.append({
#             "cn": str(entry.cn) if "cn" in entry else "",
#             "mail": str(entry.mail) if "mail" in entry else "",
#             "department": (
#                 str(entry.departmentNumber)
#                 if "departmentNumber" in entry
#                 else str(entry.ou) if "ou" in entry
#                 else "Unknown"
#             )
#         })

#     # 5️⃣ Fermeture connexion
#     conn.unbind()
#     return people


from ldap3 import Server, Connection, ALL, SUBTREE
from app.config import (
    LDAP_URI,
    LDAP_BIND_DN,
    LDAP_PASSWORD,
    LDAP_BASE_DN
)

ATTRIBUTES = ["cn", "mail", "departmentNumber", "ou"]


def get_people():
    server = Server(LDAP_URI, get_info=ALL)

    conn = Connection(
        server,
        user=LDAP_BIND_DN,
        password=LDAP_PASSWORD,
        auto_bind=True
    )

    conn.search(
        search_base=LDAP_BASE_DN,
        search_filter="(&(objectClass=person)(cn=*))",
        search_scope=SUBTREE,
        attributes=ATTRIBUTES
    )

    people = []

    for entry in conn.entries:
        people.append({
            "cn": entry.cn.value if entry.cn else "",
            "mail": entry.mail.value if entry.mail else "",
            "department": (
                entry.departmentNumber.value
                if entry.departmentNumber
                else entry.ou.value if entry.ou else "Unknown"
            )
        })

    conn.unbind()
    return people
