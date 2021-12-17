nums = [3,4,7,8]
formula = ["+", "-", "*", "/"]

arr = []

def calc(a,b,c,d):
    for x1 in formula:
        for x2 in formula:
            for x3 in formula:
                li = []
                li.append(f"{a} {x1} {b} {x2} {c} {x3} {d}")

                li.append(f"({a} {x1} {b}) {x2} {c} {x3} {d}")
                li.append(f"({a} {x1} {b} {x2} {c}) {x3} {d}")
                li.append(f"({a} {x1} ({b} {x2} {c})) {x3} {d}")
                li.append(f"(({a} {x1} {b}) {x2} {c}) {x3} {d}")

                li.append(f"{a} {x1} {b} {x2} ({c} {x3} {d})")
                li.append(f"{a} {x1} ({b} {x2} {c} {x3} {d})")
                li.append(f"{a} {x1} ({b} {x2} ({c} {x3} {d}))")
                li.append(f"{a} {x1} (({b} {x2} {c}) {x3} {d})")

                li.append(f"{a} {x1} ({b} {x2} {c}) {x3} {d}")
                arr.extend(li)
                for x in li:
                    try:
                        if eval(x) == 10:
                            print(f"{x} = 10")
                    except:
                            (f'ZeroDivisionError: division by zero {x}')

for a in nums:
    for b in nums:
        if a == b:
            continue
        for c in nums:
            if c in [a,b]:
                continue
            for d in nums:
                if d in [a, b, c]:
                    continue
                calc(a, b, c, d)

print(f"total formula count - {len(arr)}")

