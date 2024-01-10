import socket

class SimpleRmiDiscoverer:
    def __init__(self, reg_ip, reg_port, ignore_endpoint=False, dump_only=False):
        self.reg_ip = reg_ip
        self.reg_port = reg_port
        self.ignore_endpoint = ignore_endpoint
        self.dump_only = dump_only
        self.end_p_ip = ""
        self.end_p_port = 0
        self.reg_s = None
        self.end_s = None

    def connect_registry(self):
        try:
            self.reg_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.reg_s.connect((self.reg_ip, self.reg_port))
        except Exception as e:
            print(f"[!] Tidak dapat terhubung ke RMI Registry: {e}")
            return False
        return True

    def rmi_handshake(self, s):
        h_shake1 = b'\x4A\x52\x4D\x49\x00\x02\x4B'
        h_shake2 = b'\x00\x09\x31\x32\x37\x2E\x30\x2E\x30\x2E\x31\x00\x00\x00\x00'
        
        try:
            s.sendall(h_shake1)
            response = s.recv(1024)
            if response[0] != 0x4E:
                print("[!] Handshake gagal, respons buruk. Kemungkinan bukan RMI.")
                return False
            s.sendall(h_shake2)
        except Exception as e:
            print(f"[!] Handshake gagal, Kesalahan dalam Komunikasi RMI: {e}")
            return False
        return True

    def invoke_object(self, s):
        try:
            # Ganti dengan logika konkret untuk pemanggilan objek di sini
            # Misalnya, s.sendall(data) dan response = s.recv(1024)
            # Lakukan operasi yang diperlukan sesuai kebutuhan aplikasi Anda
            # Contoh sederhana:
            data = b'This is an example request'
            s.sendall(data)
            response = s.recv(1024)
            print("[+] Objek dipanggil dengan sukses!")
            print("[+] Respons dari objek:", response.decode())
        except Exception as e:
            print(f"[-] Kesalahan saat memanggil objek: {e}")

    def connect_endpoint(self, ignore_endpoint):
        try:
            if not ignore_endpoint:
                # Ganti dengan logika konkret untuk koneksi endpoint dari informasi yang telah diekstrak
                # Misalnya, self.end_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # dan self.end_s.connect((self.end_p_ip, self.end_p_port))
                # Lakukan operasi yang diperlukan sesuai kebutuhan aplikasi Anda
                print("[+] Menghubungkan ke Endpoint Dinamis...")
            else:
                # Ganti dengan logika konkret jika Anda memilih untuk mengabaikan endpoint
                # Misalnya, self.end_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # dan self.end_s.connect((self.reg_ip, self.end_p_port))
                # Lakukan operasi yang diperlukan sesuai kebutuhan aplikasi Anda
                print("[+] Mengabaikan endpoint dan menghubungkan ke RMI Registry...")

            # Setelah koneksi berhasil, Anda dapat mengakses self.end_s untuk berkomunikasi dengan endpoint
            print("[+] Koneksi ke Endpoint Dinamis berhasil!")
        except Exception as e:
            print(f"[-] Kesalahan saat menghubungkan ke endpoint: {e}")

    def invoke_dynamic_object(self, s):
        try:
            # Ganti dengan logika konkret untuk pemanggilan objek dinamis di sini
            # Misalnya, s.sendall(data) dan response = s.recv(1024)
            # Lakukan operasi yang diperlukan sesuai kebutuhan aplikasi Anda
            # Contoh sederhana:
            data = b'This is an example dynamic object request'
            s.sendall(data)
            response = s.recv(1024)
            print("[+] Objek Dinamis dipanggil dengan sukses!")
            print("[+] Respons dari objek dinamis:", response.decode())
        except Exception as e:
            print(f"[-] Kesalahan saat memanggil objek dinamis: {e}")

    def close_socket(self, s):
        try:
            s.close()
        except Exception as e:
            pass

    def start(self):
        is_connected = self.connect_registry()
        if not is_connected:
            print("[-] Aborting Connection to RMI Registry! Quitting!")
            self.close_socket(self.reg_s)
            return -1

        is_h_shaked = self.rmi_handshake(self.reg_s)
        if not is_h_shaked:
            print("[-] Aborting handshaking with RMI Registry! Quitting!")
            self.close_socket(self.reg_s)
            return -2

        is_invoked = self.invoke_object(self.reg_s)
        if not is_invoked:
            print("[-] Object Calling Error, RMI Registry! Quitting")
            self.close_socket(self.reg_s)
            return -2

        print("[+] RMI Registry contacted successfully!")
        print("[+] Extracted Endpoint Name / IP Address:", self.end_p_ip)
        print("[+] Extracted Endpoint Dynamic TCP Port:", self.end_p_port)

        self.close_socket(self.reg_s)

        if self.dump_only:
            print("[+] RMI Registry Dump Completed Successfully!")
            return 0

        is_e_connected = self.connect_endpoint(self.ignore_endpoint)
        if not is_e_connected:
            print("[-] Aborting!")
            return -3

        is_h_shaked = self.rmi_handshake(self.end_s)
        if not is_h_shaked:
            print("[-] Cannot handShake with the dynamic Endpoint!")
            self.close_socket(self.end_s)
            return -2

        is_d_invoked = self.invoke_dynamic_object(self.end_s)
        if not is_d_invoked:
            print("[-] Cannot Invoke RMIServerImpl_Stub on the dynamic Endpoint!")
            self.close_socket(self.end_s)
            return -4

        self.close_socket(self.end_s)
        return 1

# Contoh Penggunaan
rmi_discoverer = SimpleRmiDiscoverer("127.0.0.1", 1099)
result = rmi_discoverer.start()
print(result)
