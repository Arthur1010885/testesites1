import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import os
import json
import threading
import sys

class DarkMSIEmulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dark MSI Android Emulator")
        self.root.geometry("1000x700")
        self.root.configure(bg="#1a1a1a")
        
        # Configurações padrão
        self.settings = {
            "device": "Samsung Galaxy S21",
            "resolution": "1080x1920",
            "dpi": "420",
            "ram": "4096",
            "storage": "16384",
            "cpu_cores": "4",
            "gpu_mode": "host",
            "android_version": "11.0"
        }
        
        self.load_settings()
        self.create_ui()
        
    def load_settings(self):
        """Carrega configurações salvas"""
        try:
            if os.path.exists("dark_msi_settings.json"):
                with open("dark_msi_settings.json", "r") as f:
                    saved_settings = json.load(f)
                    self.settings.update(saved_settings)
        except:
            pass
            
    def save_settings(self):
        """Salva configurações"""
        try:
            with open("dark_msi_settings.json", "w") as f:
                json.dump(self.settings, f, indent=4)
        except:
            pass
    
    def create_ui(self):
        """Cria a interface gráfica"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#1a1a1a")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Cabeçalho
        header_frame = tk.Frame(main_frame, bg="#2d2d2d")
        header_frame.pack(fill="x", pady=(0, 20))
        
        title_label = tk.Label(
            header_frame,
            text="DARK MSI ANDROID EMULATOR",
            font=("Arial", 20, "bold"),
            fg="#00ff00",
            bg="#2d2d2d"
        )
        title_label.pack(pady=15)
        
        # Frame de configurações
        config_frame = tk.LabelFrame(
            main_frame,
            text=" Configurações do Emulador ",
            font=("Arial", 12, "bold"),
            fg="#ffffff",
            bg="#2d2d2d",
            bd=2,
            relief="groove"
        )
        config_frame.pack(fill="x", pady=10)
        
        # Dispositivo
        tk.Label(config_frame, text="Modelo do Celular:", 
                fg="#ffffff", bg="#2d2d2d", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.device_var = tk.StringVar(value=self.settings["device"])
        device_combo = ttk.Combobox(config_frame, textvariable=self.device_var, width=30)
        device_combo['values'] = (
            "Samsung Galaxy S21", "Samsung Galaxy S20", "Google Pixel 6", 
            "OnePlus 9", "Xiaomi Mi 11", "Huawei P40", "Customizado"
        )
        device_combo.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        # Resolução
        tk.Label(config_frame, text="Resolução:", 
                fg="#ffffff", bg="#2d2d2d", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.resolution_var = tk.StringVar(value=self.settings["resolution"])
        resolution_combo = ttk.Combobox(config_frame, textvariable=self.resolution_var, width=15)
        resolution_combo['values'] = ("720x1280", "1080x1920", "1440x2560", "Customizado")
        resolution_combo.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        # DPI
        tk.Label(config_frame, text="DPI:", 
                fg="#ffffff", bg="#2d2d2d", font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.dpi_var = tk.StringVar(value=self.settings["dpi"])
        dpi_combo = ttk.Combobox(config_frame, textvariable=self.dpi_var, width=15)
        dpi_combo['values'] = ("320", "420", "480", "560", "640", "Customizado")
        dpi_combo.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        # RAM
        tk.Label(config_frame, text="RAM (MB):", 
                fg="#ffffff", bg="#2d2d2d", font=("Arial", 10)).grid(row=0, column=2, sticky="w", padx=10, pady=5)
        self.ram_var = tk.StringVar(value=self.settings["ram"])
        ram_combo = ttk.Combobox(config_frame, textvariable=self.ram_var, width=15)
        ram_combo['values'] = ("2048", "4096", "8192", "16384", "Customizado")
        ram_combo.grid(row=0, column=3, padx=10, pady=5, sticky="w")
        
        # Armazenamento
        tk.Label(config_frame, text="Armazenamento (MB):", 
                fg="#ffffff", bg="#2d2d2d", font=("Arial", 10)).grid(row=1, column=2, sticky="w", padx=10, pady=5)
        self.storage_var = tk.StringVar(value=self.settings["storage"])
        storage_combo = ttk.Combobox(config_frame, textvariable=self.storage_var, width=15)
        storage_combo['values'] = ("8192", "16384", "32768", "65536", "Customizado")
        storage_combo.grid(row=1, column=3, padx=10, pady=5, sticky="w")
        
        # CPU Cores
        tk.Label(config_frame, text="Núcleos CPU:", 
                fg="#ffffff", bg="#2d2d2d", font=("Arial", 10)).grid(row=2, column=2, sticky="w", padx=10, pady=5)
        self.cpu_var = tk.StringVar(value=self.settings["cpu_cores"])
        cpu_combo = ttk.Combobox(config_frame, textvariable=self.cpu_var, width=15)
        cpu_combo['values'] = ("2", "4", "6", "8", "Customizado")
        cpu_combo.grid(row=2, column=3, padx=10, pady=5, sticky="w")
        
        # Frame de otimizações
        optim_frame = tk.LabelFrame(
            main_frame,
            text=" Otimizações Avançadas ",
            font=("Arial", 12, "bold"),
            fg="#ffffff",
            bg="#2d2d2d",
            bd=2,
            relief="groove"
        )
        optim_frame.pack(fill="x", pady=10)
        
        # GPU Mode
        tk.Label(optim_frame, text="Modo GPU:", 
                fg="#ffffff", bg="#2d2d2d", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.gpu_var = tk.StringVar(value=self.settings["gpu_mode"])
        gpu_combo = ttk.Combobox(optim_frame, textvariable=self.gpu_var, width=15)
        gpu_combo['values'] = ("host", "swiftshader", "angle", "mesa")
        gpu_combo.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        # Android Version
        tk.Label(optim_frame, text="Versão Android:", 
                fg="#ffffff", bg="#2d2d2d", font=("Arial", 10)).grid(row=0, column=2, sticky="w", padx=10, pady=5)
        self.android_var = tk.StringVar(value=self.settings["android_version"])
        android_combo = ttk.Combobox(optim_frame, textvariable=self.android_var, width=15)
        android_combo['values'] = ("9.0", "10.0", "11.0", "12.0", "13.0")
        android_combo.grid(row=0, column=3, padx=10, pady=5, sticky="w")
        
        # Opções de performance
        self.accel_var = tk.BooleanVar(value=True)
        accel_check = tk.Checkbutton(
            optim_frame, 
            text="Aceleração por Hardware", 
            variable=self.accel_var,
            fg="#ffffff", 
            bg="#2d2d2d",
            selectcolor="#1a1a1a",
            font=("Arial", 10)
        )
        accel_check.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        
        self.high_perf_var = tk.BooleanVar(value=True)
        high_perf_check = tk.Checkbutton(
            optim_frame, 
            text="Modo Alto Desempenho", 
            variable=self.high_perf_var,
            fg="#ffffff", 
            bg="#2d2d2d",
            selectcolor="#1a1a1a",
            font=("Arial", 10)
        )
        high_perf_check.grid(row=1, column=2, columnspan=2, sticky="w", padx=10, pady=5)
        
        # Frame de controle
        control_frame = tk.Frame(main_frame, bg="#1a1a1a")
        control_frame.pack(fill="x", pady=20)
        
        # Botões
        self.start_btn = tk.Button(
            control_frame,
            text="▶ INICIAR EMULADOR",
            command=self.start_emulator,
            font=("Arial", 14, "bold"),
            bg="#00aa00",
            fg="#ffffff",
            width=20,
            height=2
        )
        self.start_btn.pack(side="left", padx=10)
        
        self.stop_btn = tk.Button(
            control_frame,
            text="■ PARAR EMULADOR",
            command=self.stop_emulator,
            font=("Arial", 14, "bold"),
            bg="#aa0000",
            fg="#ffffff",
            width=20,
            height=2,
            state="disabled"
        )
        self.stop_btn.pack(side="left", padx=10)
        
        self.settings_btn = tk.Button(
            control_frame,
            text="⚙ SALVAR CONFIGURAÇÕES",
            command=self.save_config,
            font=("Arial", 12, "bold"),
            bg="#0066aa",
            fg="#ffffff",
            width=20,
            height=2
        )
        self.settings_btn.pack(side="left", padx=10)
        
        # Área de log
        log_frame = tk.LabelFrame(
            main_frame,
            text=" Log do Sistema ",
            font=("Arial", 12, "bold"),
            fg="#ffffff",
            bg="#2d2d2d",
            bd=2,
            relief="groove"
        )
        log_frame.pack(fill="both", expand=True, pady=10)
        
        self.log_text = tk.Text(
            log_frame,
            height=10,
            bg="#000000",
            fg="#00ff00",
            font=("Consolas", 10),
            wrap="word"
        )
        scrollbar = tk.Scrollbar(log_frame, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        scrollbar.pack(side="right", fill="y", pady=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="Pronto para iniciar")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief="sunken",
            anchor="w",
            font=("Arial", 10),
            fg="#ffffff",
            bg="#006600"
        )
        status_bar.pack(side="bottom", fill="x")
        
        self.emulator_process = None
        
    def log_message(self, message):
        """Adiciona mensagem ao log"""
        self.log_text.insert("end", f"{message}\n")
        self.log_text.see("end")
        self.root.update()
        
    def save_config(self):
        """Salva as configurações atuais"""
        self.settings.update({
            "device": self.device_var.get(),
            "resolution": self.resolution_var.get(),
            "dpi": self.dpi_var.get(),
            "ram": self.ram_var.get(),
            "storage": self.storage_var.get(),
            "cpu_cores": self.cpu_var.get(),
            "gpu_mode": self.gpu_var.get(),
            "android_version": self.android_var.get()
        })
        self.save_settings()
        messagebox.showinfo("Sucesso", "Configurações salvas com sucesso!")
        self.log_message("Configurações salvas")
        
    def generate_emulator_command(self):
        """Gera o comando para iniciar o emulador"""
        cmd = [
            "emulator",
            "-avd", "DarkMSI_AVD",
            "-skin", self.resolution_var.get(),
            "-dpi-device", self.dpi_var.get(),
            "-memory", self.ram_var.get(),
            "-sdcard", f"{self.storage_var.get()}M",
            "-cores", self.cpu_var.get(),
            "-gpu", self.gpu_var.get(),
            "-no-audio",
            "-no-boot-anim"
        ]
        
        if self.accel_var.get():
            cmd.append("-accel-on")
            
        if self.high_perf_var.get():
            cmd.extend(["-engine", "high_performance"])
            
        return cmd
        
    def start_emulator(self):
        """Inicia o emulador em uma thread separada"""
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.status_var.set("Iniciando emulador...")
        
        thread = threading.Thread(target=self.run_emulator)
        thread.daemon = True
        thread.start()
        
    def run_emulator(self):
        """Executa o emulador"""
        try:
            self.log_message("=" * 50)
            self.log_message("INICIANDO DARK MSI EMULATOR")
            self.log_message("=" * 50)
            self.log_message(f"Dispositivo: {self.device_var.get()}")
            self.log_message(f"Resolução: {self.resolution_var.get()}")
            self.log_message(f"DPI: {self.dpi_var.get()}")
            self.log_message(f"RAM: {self.ram_var.get()}MB")
            self.log_message(f"Armazenamento: {self.storage_var.get()}MB")
            self.log_message(f"CPU Cores: {self.cpu_var.get()}")
            self.log_message(f"GPU Mode: {self.gpu_var.get()}")
            self.log_message(f"Android: {self.android_var.get()}")
            self.log_message("=" * 50)
            
            # Simulação do emulador (substituir pelo comando real)
            cmd = self.generate_emulator_command()
            self.log_message(f"Comando: {' '.join(cmd)}")
            self.log_message("Emulador iniciado com sucesso!")
            self.log_message("Otimizações aplicadas:")
            self.log_message("  ✓ Aceleração de GPU ativada")
            self.log_message("  ✓ Modo alto desempenho ativo")
            self.log_message("  ✓ Memória otimizada")
            self.log_message("  ✓ Renderização acelerada")
            
            self.status_var.set("Emulador em execução - Dark MSI")
            
        except Exception as e:
            self.log_message(f"ERRO: {str(e)}")
            messagebox.showerror("Erro", f"Falha ao iniciar emulador: {str(e)}")
            self.stop_emulator()
            
    def stop_emulator(self):
        """Para o emulador"""
        if self.emulator_process:
            try:
                self.emulator_process.terminate()
            except:
                pass
                
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.status_var.set("Emulador parado")
        self.log_message("Emulador parado pelo usuário")

def main():
    # Verificar se o Android SDK está disponível
    try:
        subprocess.run(["emulator", "-version"], capture_output=True)
    except:
        print("AVISO: Android SDK Emulator não encontrado no PATH")
        print("Este é um simulador de interface para demonstração")
        
    root = tk.Tk()
    app = DarkMSIEmulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()