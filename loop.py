import subprocess
import time
import signal

def main():
    while True:
        print("🔄 Uruchamiam voter...")
        process = subprocess.Popen(
            ["./target/release/voter"],
            stdout=None,  # pokazuje na bieżąco w terminalu
            stderr=None
        )

        try:
            time.sleep(60)
        except KeyboardInterrupt:
            print("🛑 Przerwano ręcznie.")
            process.terminate()
            break

        print("⏹ Zatrzymuję voter...")
        process.send_signal(signal.SIGINT)  # delikatne przerwanie
        time.sleep(3)

        if process.poll() is None:
            print("⚠️ Proces nadal żyje – zabijam na twardo.")
            process.kill()
            process.wait()

if __name__ == "__main__":
    main()
