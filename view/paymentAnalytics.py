import tkinter as tk
from tkinter import ttk
import numpy as np
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt
from control.maincontrol import MainControl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PaymentAnalytics:
    def __init__(self, root):
        self.root = root

    def analytics(self):
        # Criação da janela de popup
        popup = tk.Toplevel(self.root)
        popup.title("Analytics")
        popup.geometry('600x800')
        popup.configure(bg='light blue')

        # Criar um canvas para permitir a rolagem
        canvas = tk.Canvas(popup, bg='light blue')
        scrollbar = ttk.Scrollbar(popup, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        # Configuração do scrollable frame
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        # Adicionando o scrollable frame ao canvas
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        # Configurando a barra de rolagem
        canvas.configure(yscrollcommand=scrollbar.set)
        # Posicionando o canvas e a barra de rolagem
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Frame para exibir a soma de todos os valores pagos
        frame_total_value = ttk.Frame(scrollable_frame, padding="10", relief="solid")
        frame_total_value.pack(pady=10)

        total_value = MainControl.get_total_amount()
        label_total_value = ttk.Label(frame_total_value, text=f"Soma de todos os valores pagos: R${total_value:.2f}")
        label_total_value.pack()

        # Frame para o gráfico de horários
        frame_hours = ttk.Frame(scrollable_frame, padding="10", relief="solid")
        frame_hours.pack(pady=10, fill=tk.BOTH, expand=True)
        self.hour_graph(frame_hours)

        # Frame para o gráfico de operadores
        frame_operator = ttk.Frame(scrollable_frame, padding="10", relief="solid")
        frame_operator.pack(pady=10, fill=tk.BOTH, expand=True)
        self.operator_graph(frame_operator)

        # Frame para o gráfico de métodos de pagamento
        frame_payment_methods = ttk.Frame(scrollable_frame, padding="10", relief="solid")
        frame_payment_methods.pack(pady=10, fill=tk.BOTH, expand=True)
        self.method_graph(frame_payment_methods)
    
    def method_graph(self, frame):
        # Simulação da função para obter as transações (deve ser adaptada para o seu código real)
        toll_payments = MainControl.get_all_transactions()  # Obtenha todas as transações
        # Contar as ocorrências de cada método de pagamento
        method_counts = Counter()
        for payment in toll_payments:
            if payment.method:  # Verifica se o método de pagamento existe
                method_counts[payment.method] += 1
        methods = list(method_counts.keys())
        counts = list(method_counts.values())
        plt.style.use('_mpl-gallery')
        
        # Criar gráfico de pizza
        fig, ax = plt.subplots(figsize=(6, 5))  # Ajusta o tamanho do gráfico
        wedges, texts, autotexts = ax.pie(
            counts,
            labels=methods,
            autopct='%1.1f%%',
            startangle=140,
            colors=plt.cm.Paired(range(len(methods))),
            pctdistance=0.85
        )
        ax.set_title('Distribuição dos Métodos de Pagamento')
        # Melhorar a legibilidade dos rótulos
        for text in texts:
            text.set_fontsize(10)
        for autotext in autotexts:
            autotext.set_fontsize(10)
        # Ajustar layout para evitar sobreposição de elementos
        plt.tight_layout()
        # Integrar o gráfico ao Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def operator_graph(self, frame):
        toll_payments = MainControl.get_all_transactions()
        # Analisar as transações por operador
        operator_counts = Counter()
        # Contando as ocorrências de cada operador
        for payment in toll_payments:
            if payment.operator and payment.operator.name:  # Verifica se o operador existe e tem nome
                operator_counts[payment.operator.name] += 1

        operators = list(operator_counts.keys())
        counts = list(operator_counts.values())
        plt.style.use('_mpl-gallery')
        # Gerar dados para o gráfico
        x = np.arange(len(operators))  # Eixo x
        y = counts  # Eixo y com as contagens
        # Criar gráfico de barras com ajuste de tamanho
        fig, ax = plt.subplots(figsize=(5, 5))  # Aumenta o tamanho do gráfico
        ax.bar(x, y, color='blue', edgecolor='black', alpha=0.7)
        # Adicionar rótulos
        ax.set_xticks(x)
        ax.set_xticklabels(operators, rotation=90, ha='center')  # Rotaciona os rótulos dos operadores para 90 graus
        ax.set_xlabel('Operadores')
        ax.set_ylabel('Quantidade de Transações')
        ax.set_title('Quantidade de Transações por Operador')
        ax.grid(axis='y')

        # Ajustar layout para evitar sobreposição de elementos
        plt.tight_layout()
        # Integrando o gráfico ao Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def hour_graph(self, frame):
        # Obtendo a lista de pagamentos da camada de controle
        toll_payments = MainControl.get_all_transactions()
        # Extraindo as horas das transações
        hours = [datetime.strptime(payment.date, "%Y-%m-%d %H:%M:%S").hour for payment in toll_payments]
        # Contabilizando a frequência de cada hora
        hour_counts = Counter(hours)
        # Preparando os dados para o gráfico
        x = np.array(sorted(hour_counts.keys()))  # Horas ordenadas
        y = np.array([hour_counts[hour] for hour in x])  # Frequência das horas

        # Criando o gráfico de linha
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot(x, y, marker='o', linestyle='-', color='blue')
        # Adicionando linhas verticais nos pontos
        ax.vlines(x, ymin=0, ymax=y, color='gray', linestyle='dashed', alpha=0.5)
        # Adicionando título e rótulos
        ax.set_title("Picos de Movimento por Hora")
        ax.set_xlabel("Hora do Dia")
        ax.set_ylabel("Número de Transações")
        # Ajustando os ticks e os limites dos eixos
        ax.set_xticks(x)
        ax.set_xlim(0, 23)
        ax.set_ylim(0, max(y) + 1)
        # Garantir que os ticks no eixo y sejam inteiros
        ax.yaxis.get_major_locator().set_params(integer=True)

        # Integrando o gráfico ao Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)