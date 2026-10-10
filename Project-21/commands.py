
def get_device_info(connection, command):
    output = connection.send_command(command)
    return output