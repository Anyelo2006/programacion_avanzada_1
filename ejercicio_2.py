def main():
    v_base = float(input("Ingrese el valor monetario: "))

    impuesto = v_base  * 0.19
    
    if v_base >= 200000:
        descuento = v_base * 0.10
    else:
        descuento = 0

    total = v_base + impuesto - descuento

    print(f"\nValor base: ${v_base:,.2f}")
    print(f"Impuesto (19%): ${impuesto:,.2f}")
    print(f"Descuento (10%): ${descuento:,.2f}")
    print(f"Total final: ${total:,.2f}")

if __name__ == "__main__":
    main()