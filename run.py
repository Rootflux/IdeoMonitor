from ideomonitor.console_ui import print_banner, print_results, print_error, prompt_file
from ideomonitor.scanner import scan_file

def main():
    print_banner()
    try:
        file_path = prompt_file()
        results = scan_file(file_path)
        print_results(results)
    except Exception as e:
        print_error(str(e))

if __name__ == "__main__":
    main()
