import socket
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

from .log import get_logger

logger = get_logger("WifiDet")


class NetworkStatus:

    def __init__(self):
        self.dns_servers = [
            "114.114.114.114",
            "223.5.5.5",
            "8.8.8.8",
            "1.1.1.1",
            "223.6.6.6",
            "8.8.4.4",
        ]
        self.ping_dns_servers = [
            "114.114.114.114",
            "223.5.5.5",
            "8.8.8.8",
        ]
        self.dns_port = 53
        self.socket_timeout = 0.3
        self.ping_timeout = 300
        self._parallel_workers = 4

    def is_internet_connected(self):
        logger.debug("socket 并行检测开始 (workers=%d)", self._parallel_workers)
        if self._parallel_check(self.dns_servers, self._check_socket):
            return True

        logger.debug("socket 全部失败，降级 ping 并行检测")
        if self._parallel_check(self.ping_dns_servers, self._check_ping):
            return True

        logger.debug("所有检测方式均失败，判定为未联网")
        return False

    def _parallel_check(self, servers, checker):
        with ThreadPoolExecutor(max_workers=self._parallel_workers) as executor:
            futures = {
                executor.submit(checker, srv): srv for srv in servers
            }
            for future in as_completed(futures):
                try:
                    if future.result(timeout=0):
                        logger.debug("%s 命中，判定已联网", futures[future])
                        for f in futures:
                            f.cancel()
                        return True
                except Exception:
                    pass
        return False

    def _check_socket(self, dns_server):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.socket_timeout)
            sock.connect((dns_server, self.dns_port))
            sock.close()
            return True
        except Exception:
            return False

    def _check_ping(self, dns_server):
        try:
            result = subprocess.run(
                ["ping", "-n", "1", "-w", str(self.ping_timeout), dns_server],
                capture_output=True,
                timeout=self.socket_timeout + 0.5,
            )
            return result.returncode == 0
        except Exception:
            return False

    def get_connection_type(self):
        try:
            result = subprocess.run(
                ["netsh", "interface", "show", "interface"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore",
            )
            output = result.stdout

            ethernet_active = False
            wifi_active = False

            lines = output.split("\n")
            for line in lines:
                if "已连接" in line or "Connected" in line:
                    if "以太网" in line or "Ethernet" in line:
                        ethernet_active = True
                    elif "Wi-Fi" in line or "WLAN" in line:
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
        try:
            result = subprocess.run(
                ["netsh", "wlan", "show", "interfaces"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore",
            )
            output = result.stdout

            for line in output.split("\n"):
                if "SSID" in line and "BSSID" not in line:
                    match = re.search(r":\s*(.+)", line)
                    if match:
                        name = match.group(1).strip()
                        if name:
                            return name
            return None
        except Exception:
            return None


if __name__ == "__main__":
    from lib.package.log import setup_logging

    setup_logging()
    network = NetworkStatus()
    is_connected = network.is_internet_connected()
    conn_type, wifi_name = network.get_connection_type()
    logger.info("Internet: %s", "Connected" if is_connected else "Disconnected")
    logger.info("Connection: %s%s", conn_type, f" - {wifi_name}" if wifi_name else "")