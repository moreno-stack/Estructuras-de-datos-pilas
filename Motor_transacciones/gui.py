import tkinter as tk
from tkinter import ttk

from queue_manager import TransactionQueue
from transaction_engine import TransactionEngine
from failed_transactions import FailedTransactions
from transaction import Transaction


class BankGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Motor de Transacciones Bancarias")
        self.root.geometry("750x500")

        self.queue = TransactionQueue()
        self.engine = TransactionEngine()
        self.failed = FailedTransactions()

        self.counter = 1

        self.create_interface()

    def create_interface(self):

        titulo = tk.Label(self.root, text="Motor de Transacciones Bancarias", font=("Arial",18))
        titulo.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(frame,text="Cuenta Origen").grid(row=0,column=0)
        self.origen = tk.Entry(frame)
        self.origen.grid(row=0,column=1)

        tk.Label(frame,text="Cuenta Destino").grid(row=1,column=0)
        self.destino = tk.Entry(frame)
        self.destino.grid(row=1,column=1)

        tk.Label(frame,text="Monto").grid(row=2,column=0)
        self.monto = tk.Entry(frame)
        self.monto.grid(row=2,column=1)

        boton = tk.Button(frame,text="Agregar Transaccion",command=self.add_transaction)
        boton.grid(row=3,columnspan=2,pady=10)

        self.table = ttk.Treeview(self.root)

        self.table["columns"]=("id","origen","destino","monto")

        self.table.column("#0",width=0)
        self.table.column("id",width=80)
        self.table.column("origen",width=150)
        self.table.column("destino",width=150)
        self.table.column("monto",width=100)

        self.table.heading("id",text="ID")
        self.table.heading("origen",text="Origen")
        self.table.heading("destino",text="Destino")
        self.table.heading("monto",text="Monto")

        self.table.pack(pady=20)

        botones = tk.Frame(self.root)
        botones.pack()

        procesar = tk.Button(botones,text="Procesar Transaccion",command=self.process_transaction)
        procesar.grid(row=0,column=0,padx=10)

        fallidas = tk.Button(botones,text="Ver Fallidas",command=self.show_failed)
        fallidas.grid(row=0,column=1)

        self.resultado = tk.Label(self.root,text="")
        self.resultado.pack(pady=10)

    def add_transaction(self):

        origen = self.origen.get()
        destino = self.destino.get()
        monto = self.monto.get()

        tx = Transaction(self.counter,origen,destino,monto)

        self.queue.enqueue(tx)

        self.table.insert("", "end", values=(tx.id,tx.origen,tx.destino,tx.monto))

        self.counter += 1

        self.origen.delete(0,tk.END)
        self.destino.delete(0,tk.END)
        self.monto.delete(0,tk.END)

    def process_transaction(self):

        tx = self.queue.dequeue()

        if tx is None:
            self.resultado.config(text="No hay transacciones")
            return

        ok = self.engine.process(tx)

        if ok:
            self.resultado.config(text="Transaccion exitosa")
        else:
            self.failed.add(tx)
            self.resultado.config(text="Transaccion fallida")

        self.refresh_table()

    def refresh_table(self):

        for i in self.table.get_children():
            self.table.delete(i)

        for t in self.queue.show():
            self.table.insert("", "end", values=(t.id,t.origen,t.destino,t.monto))

    def show_failed(self):

        ventana = tk.Toplevel(self.root)
        ventana.title("Transacciones Fallidas")

        for t in self.failed.show():
            tk.Label(ventana,text=str(t)).pack()