"""One-line joke entry: writes the chosen line to /output/entry.txt."""

LINE = "I told my boss I work best under pressure, so now he just stands behind me breathing loudly all day."

def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
