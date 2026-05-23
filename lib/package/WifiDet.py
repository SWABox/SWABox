import socket
import subprocess
import re


class NetworkStatus:
    """网络状态检测类"""
    def __init__(self):
        pass
    def is_internet_connected(self):
        """检测是否连接互联网"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect(("8.8.8.8", 53))
            sock.close()
            return True
        except Exception:
            try:
                result = subprocess.run(
                    ["ping", "-n", "1", "-w", "1000", "8.8.8.8"],
                    capture_output=True, timeout=2
                )
                return result.returncode == 0
            except Exception:
                return False
    
    def get_connection_type(self):
        """获取网络连接类型"""
        try:
            result = subprocess.run(
                ["netsh", "interface", "show", "interface"],
                capture_output=True, text=True, encoding="utf-8", errors="ignore"
            )
            output = result.stdout
            
            ethernet_active = False
            wifi_active = False
            
            lines = output.split('\n')
            for line in lines:
                if '已连接' in line or 'Connected' in line:
                    if '以太网' in line or 'Ethernet' in line:
                        ethernet_active = True
                    elif 'Wi-Fi' in line or 'WLAN' in line:
                        wifi_active = True
            
            if wifi_active:
                wifi_name = self._get_wifi_name()
                return "WiFi", wifi_name
            elif ethernet_active:
                return "Ethernet", None
            else:
                return "Disconnected", None
                
        except Exception:
            return "Unknown", None
    
    def _get_wifi_name(self):
        """获取已连接的WiFi名称"""
        try:
            result = subprocess.run(
                ["netsh", "wlan", "show", "interfaces"],
                capture_output=True, text=True, encoding="utf-8", errors="ignore"
            )
            output = result.stdout
            
            for line in output.split('\n'):
                if 'SSID' in line and 'BSSID' not in line:
                    match = re.search(r':\s*(.+)', line)
                    if match:
                        name = match.group(1).strip()
                        if name:
                            return name
            return None
        except Exception:
            return None


if __name__ == '__main__':
    network = NetworkStatus()
    is_connected = network.is_internet_connected()
    conn_type, wifi_name = network.get_connection_type()
    print(f"Internet: {'Connected' if is_connected else 'Disconnected'}")
    print(f"Connection: {conn_type}" + (f" - {wifi_name}" if wifi_name else ""))