'''
Name: Prachi santosh Kolte
Description: This is simple port scanner which is designed to scan the ports of the inputed IP system and it gives you the output
whether the port is open or close.
Simple database is used to store the data with timestamp so that everytime last availaibilty of the port can be seen and updated
Assumption:
1.default IP is given as local host

'''



import tkinter as tk
import socket as sk
import sqlite3 as db
import time
from tkinter import *
from socket import *



class PortScannerDAL:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.data_file = 'PortScanner.sqlite3'
        self.__connect_()


    def __connect_(self):
        self.conn = db.connect(self.data_file)
        self.cur = self.conn.cursor()

    def read_host(self, host_ip, host_name=None):
        self.cur.execute('SELECT * FROM Host WHERE HostIP=:host_ip or HostName=:host_name',
                         {"host_ip": host_ip, "host_name": host_name})
        return self.cur.fetchone()

    def create_host(self, host_ip, host_name):
        stored_host = self.read_host(host_ip, host_name)
        if stored_host == None:
            self.cur.execute("INSERT INTO Host(HostIP, HostName) Values(?,?)", (host_ip, host_name))
            self.conn.commit()
            stored_host = self.read_host(host_ip, host_name)
        return stored_host

    def create_scan(self, host_id):
        self.cur.execute("INSERT INTO Scan(HostId, ScanStartTime) Values (?,?)", (host_id, time.strftime("%c")));
        self.conn.commit()
        scan_id = self.cur.lastrowid
        self.cur.execute('SELECT * FROM Scan WHERE ScanId=:scan_id', {"scan_id": scan_id})
        return self.cur.fetchone()

    def update_scan_end_time(self, scan_id):
        scan_end_time = time.strftime("%c")
        self.cur.execute('UPDATE Scan set ScanEndTime=:scan_end_time where ScanId=:scan_id',
                         {"scan_end_time": scan_end_time, "scan_id": scan_id})
        self.conn.commit()
        self.cur.execute('SELECT * FROM Scan WHERE ScanId=:scan_id', {"scan_id": scan_id})
        return self.cur.fetchone()


    def read_port_status(self, host_ip, host_name):
        self.cur.execute(
            'SELECT ps.*, s.ScanStartTime FROM PortStatus ps JOIN Scan s on ps.ScanId = s.ScanId JOIN Host h on h.HostID = s.HostId WHERE h.HostIP = :host_ip AND h.HostName = :host_name',
            {"host_ip": host_ip, "host_name": host_name})
        return self.cur.fetchall()


    def create_port_status(self, scan_id, port, is_open):
        self.cur.execute("INSERT INTO PortStatus(ScanId, PortNumber, IsPortOpen) Values (?, ?, ?)",
                         (scan_id, port, is_open));
        self.conn.commit()


    def __close_connection_(self):
        self.conn.close()


    def __del__(self):
        print("Desytoing DB")
        self.__close_connection_()



class ResultsDialog(tk.Toplevel):
    def __init__(self, master, host_ip, host_name):
        self.dal = PortScannerDAL()

        self.root = Tk()
        self.root.title("Result Dialog")
        self.root.geometry("500x500")

        self.text = tk.Text(self.root, height=6, width=40)
        self.vsb = tk.Scrollbar(self.root, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

        port_status_data = self.dal.read_port_status(host_ip, host_name)
        self.add_result(port_status_data)

    def add_result(self, port_status_data):
        self.text.insert("end", "ScanId     PortNumber      Is Open      Scan Time" + "\n")
        self.text.see("end")
        for port_status in port_status_data:
            is_open_text = "YES" if port_status[2] else "NO"
            self.text.insert("end", str(port_status[0]) + '             ' + str(
                port_status[1]) + "             " + is_open_text + '        ' + str(port_status[3]) + "\n")
            self.text.see("end")


class PortScanner:
    def __init__(self):
        self.min_port = 1
        self.max_port = 10
        self.ip_address = "127.0.0.1"
        self.host_name = None
        self.__init_gui()
        self.master.mainloop()

    def __init_gui(self):
        self.master = tk.Tk()
        self.master.title("Port Design")
        self.master.geometry("300x150")
        self.result_dialog = None
        self.scanner_status_text = StringVar()
        self.scanner_status_text.set('Scanner is idle')

        # print("Default called")
        self.action_frame = Frame(self.master)
        self.action_frame.pack(side=TOP)

        self.status_frame = Frame(self.master)
        self.status_frame.pack(side=BOTTOM)

        self.host_ip_ent = Entry(self.action_frame)
        self.host_ip_ent.grid(row=0, column=1)
        self.lbl1 = Label(self.action_frame, text="Host IP:").grid(row=0, column=0, sticky=E)
        self.lbl2 = Label(self.action_frame, text="Host name:").grid(row=1, column=0, sticky=E)

        self.host_name_lbl = Label(self.action_frame, text="Not selected")
        self.host_name_lbl.grid(row=1, column=1, sticky=E)
        self.scan_btn = Button(self.action_frame, text=" Scan ", command=self.__start_scanner)
        self.results_btn = Button(self.action_frame, text=" View results ", command=self.__view_results)
        self.scan_btn.grid(row=3, column=1)
        self.results_btn.grid(row=4, column=1)

        self.scanner_status_lbl = Label(self.status_frame, textvariable=self.scanner_status_text)
        self.scanner_status_lbl.grid(row=0, column=1, sticky=E)

        self.port_scanner_dal = PortScannerDAL()
        self.__update_host_name()

    def __start_scanner(self):
        # Comment the follwoing in to get it dynamically
        self.scan_btn['state'] = tk.DISABLED
        if self.__update_host_name() != None:
            self.start_scanner()
        self.scan_btn['state'] = tk.NORMAL


    def start_scanner(self):
        host = self.port_scanner_dal.create_host(self.ip_address, self.host_name)
        print("Host Is:", host)
        scan = self.port_scanner_dal.create_scan(host[0])
        print("At start, Scan Is:", scan)
        for port in range(self.min_port, self.max_port):
            self.scan_port(port, scan[0])

        scan = self.port_scanner_dal.update_scan_end_time(scan[0])
        print("At end, Scan Is:", scan)
        self.scanner_status_text.set('Scanner is Complete')

    def scan_port(self, port, scan_id):

        self.scanner_status_text.set('Scaning port number ' + str(port))
        self.master.update_idletasks()  # this is needed to force update the view
        time.sleep(0.3)

        s = sk.socket(AF_INET, SOCK_STREAM)
        is_port_open = s.connect_ex((self.ip_address, port)) == 0
        self.port_scanner_dal.create_port_status(scan_id, port, is_port_open)
        s.close()

    def __view_results(self):
        self.result_dialog = ResultsDialog(self.master, self.ip_address, self.host_name)

    def __update_host_name(self):
        try:
            self.ip_address = self.host_ip_ent.get() if self.host_ip_ent.get() != '' else self.ip_address
            self.host_name = sk.gethostbyaddr(self.ip_address)[0]
            self.host_name_lbl['text'] = self.host_name
            self.host_ip_ent.delete(0, END)
            self.host_ip_ent.insert(0, self.ip_address)
            return self.host_name
        except sk.herror:
            self.host_name = None
            self.host_name_lbl['text'] = "Error finding the host"
            print("Error finding the host")
            return None


if __name__ == '__main__':
    ps = PortScanner()

