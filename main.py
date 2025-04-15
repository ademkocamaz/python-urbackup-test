from urbackup import urbackup_server

server = urbackup_server("http://omv.local:55414/x", "ilkadam", "//*-764864")
if server.login():
    print("Login succesful.")
    clients = server.get_status()
    print(clients)
    print(server.get_usage())
else:
    print("Login failed.")
