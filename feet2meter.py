def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    v = v.replace('ft', '')
    v = float(v)
    v = v / 3.281
    return v

main()