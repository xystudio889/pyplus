import pyplus

print(f"pyplus runner\nrunner version:0.1.0\n pyplus version :1.0.8a4\nBy xystudio https://github.com/xystudio889/linecode\n\nPress 'exit' to exit.")

while True:
    code = input(">>> ")
    
    if code in ['exit','quit','exit()','quit()']:
        quit()
    else:
        try:
            exec(code)
        except Exception as e:
            print("Error:",e)