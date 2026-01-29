from ldap3 import Server, Connection, ALL, SUBTREE
from app.config import (
    LDAP_URI,
    LDAP_BIND_DN,
    LDAP_PASSWORD,
    LDAP_BASE_DN
)

ATTRIBUTES = ["cn", "mail", "departmentNumber", "ou", "employeeType", "employeeNumber"]


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
    
    
    print(conn.entries)  # Debugging line to print the entries retrieved from LDAP

    for entry in conn.entries:
        people.append({
            "cn": entry.cn.value if entry.cn else "",
            "mail": entry.mail.value if entry.mail else "",
            "employeeType": entry.employeeType.value if entry.employeeType else "",
            "department": (
                entry.departmentNumber.value
                if entry.departmentNumber
                else entry.ou.value if entry.ou else "Unknown"
            ),
            "employeeNumber": entry.employeeNumber.value if entry.employeeNumber else ""
        })

    conn.unbind()
    return people
