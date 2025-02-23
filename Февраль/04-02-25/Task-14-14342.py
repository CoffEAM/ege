for p in range(36, 2, -1):
    num = int('BO', p) + int('OM', p) + int('BL4', p) == int('CNG', p)
    if num:
        print(p)
        break

