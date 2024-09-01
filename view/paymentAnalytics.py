import tkinter as tk
from tkinter import ttk
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from control.maincontrol import MainControl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from control.concreteAnalysisStrategy import OperatorAnalysisStrategy, PeakTimesAnalysisStrategy, PaymentMethodAnalysisStrategy, GetTotalAmountStrategy

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

        # total_value = MainControl.get_total_amount()
        get_total_strategy = GetTotalAmountStrategy()
        total_value = MainControl.analyze_transactions(get_total_strategy)
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
        # methods, counts = MainControl.get_payments_by_method()  
        pmas = PaymentMethodAnalysisStrategy()
        methods, counts = MainControl.analyze_transactions(pmas)

        MainControl.analyze_transactions
        plt.style.use('_mpl-gallery')
        # Criar gráfico de pizza
        fig, ax = plt.subplots(figsize=(5, 5))  # Ajusta o tamanho do gráfico
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
        # operators, counts = MainControl.get_transactions_by_operators()
        oas = OperatorAnalysisStrategy()
        operators, counts = MainControl.analyze_transactions(oas)
        plt.style.use('_mpl-gallery')
        
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
        # Obtendo a o dicionario com a contagem de transações por hora
        # hour_counts = MainControl.get_peak_times()
        ptas = PeakTimesAnalysisStrategy()
        hour_counts = MainControl.analyze_transactions(ptas)
        # Preparando os dados para o gráfico
        x = np.array(sorted(hour_counts.keys()))  # Horas ordenadas
        y = np.array([hour_counts[hour] for hour in x])  # Frequência das horas

        # Criando o gráfico de linha
        fig, ax = plt.subplots(figsize=(6, 5))
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
        # Garantir que o eixo y seja de inteiros
        ax.yaxis.get_major_locator().set_params(integer=True)

        # Integrando o gráfico ao Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)