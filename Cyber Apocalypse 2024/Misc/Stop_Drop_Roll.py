import socket
import traceback

def handle_command(command):
    if command == "GORGE":
        return "STOP"
    elif command == "PHREAK":
        return "DROP"
    elif command == "FIRE":
        return "ROLL"
    else:
        return "Unknown command"

def main():
    host = '94.237.54.152'  # Change this to the appropriate host
    port = 49402  # Change this to the appropriate port

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()

            print("Waiting for connection...")
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                conn.sendall(b'y')

                commands_received = []
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    command = data.decode().strip()
                    commands_received.append(command)

                    if len(commands_received) >= 3:
                        output = "-".join(handle_command(cmd) for cmd in commands_received)
                        print("Output:", output)
                        commands_received = []

    except Exception as e:
        print("An error occurred:", e)
        print("Traceback:")
        traceback.print_exc()

if __name__ == "__main__":
    main()
